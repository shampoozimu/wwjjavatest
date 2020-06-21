import json
import re
import time
from enum import IntEnum
import logging
# 通用功能模块
# 审批人类型

from bs4 import BeautifulSoup


from testCase.component.oauth import BaseOauth, Accept, ContentType, Header, UcDeploy


class SettingSwitch(IntEnum):
    OFF = 0
    ON = 1


class Oauth(BaseOauth):
    # 获取商机审批状态
    def get_business_info(self, business):
        url = "%s/%s" % (self._str_domain, business.plural)
        body = {"scope": "all_own", "per_page": 10, "type": "advance", "section_only": True}
        self._set_head(Accept.JSON, ContentType.FORM)
        self.http_response = self._http_session.get(url, data=body)
        self._assert_response()
        return BeautifulSoup(self.http_response.text, "html5lib").select("table>tbody>tr[data-id=\"%s\"]>td[data-column=\"approve_status_i18n\"]>div.value" % self._business.id).pop().text.strip()

    # 审批设置开关
    def setting_on_off(self, switch):
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        url = self._str_domain + "/settings/%s_approve/update" % self._business.singular
        body = {
            "%s_approve[enable_%s_approve]" % (self._business.singular, self._business.singular): switch.value
        }
        self.http_response = self._http_session.put(url, data=body)
        return self._assert_response()

    # 审批级数设置
    def approval_setting(self, test_case):
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        url = self._str_domain + "/settings/%s_approve/update" % self._business.singular
        list_approval_settings = test_case.list_approval_settings
        self.http_response = self._http_session.put(url, data=self._business.setting(self.csrf, list_approval_settings))
        return self._assert_response()

    # 新增商机
    def apply(self):
        logging.info("新增%s：%s" % (self._business.enum_type.name, self._business.title))
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        url = "%s/api/%s" % (self._str_domain, self._business.plural)
        self.http_response = self._http_session.post(url, data=self._business.apply(self.user))
        self._business.id = json.loads(self.http_response.text)["data"]["id"]
        return self._assert_response()

    # 执行审批
    def approval(self, approval_step):
        logging.info("审批%s：%s" % (self._business.enum_type.name, self._business.title))
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        url = "%s/api/approvals/%s/%s" % (self._str_domain, self._business.id, approval_step.enum_result.value)
        self.http_response = self._http_session.post(url, data=self._business.approve(approval_step.int_step, self.csrf))
        approval_step.test_step.call(self.user)
        return self._assert_response()

    # 消息通知
    def notifications(self):
        url = "%s/notifications" % self._str_domain
        self.http_response = self._http_session.get(url)
        self._assert_response()
        return [node.text.strip() for node in BeautifulSoup(self.http_response.text, "html5lib").select("section#notification_table tbody>tr>td>a.text-primary[href$=\"%s\"]" % self._business.id)]


# 私有化环境
class PrivateDeploy(Oauth):
    def __init__(self, setting):
        super().__init__(setting)
        self.token = None

    # 私有化环境登录方式
    def login(self, user):
        self.user = user
        self.get(self._str_domain)
        # time.sleep(2)
        self.csrf = self.get_csrf()
        # 然后，以csrf作为参数
        # 用username和pwd登录
        body = {
            "utf8": "✓",
            "authenticity_token": self.csrf,
            "user[login]": self.user.username,
            "user[password]": self.user.password,
            "commit": "登 录"
        }
        self.http_response = self._http_session.post(self._str_domain + "/users/sign_in", data=body)
        self._assert_response()
        # 获取最终的cookie和csrf
        self.cookie = self.get_cookies()
        self.csrf = self.get_csrf()
        return self


# 钉钉测试环境
class DingdingDeploy(Oauth):
    def login(self, user):
        self.user = user
        self._set_head(Accept.JSON, ContentType.FORM, Header.AUTHORIZATION, Header.X_REQUESTED_WITH)
        body = {
            "login": self.user["username"],
            "password": self.user["password"],
            "device": "web"
        }
        self.http_response = self._http_session.post(url=self._str_domain + "/api/v2/auth/login", data=body)
        self.token = self._assert_response().json()["data"]["user_token"]

        url = self._str_domain + "/dingtalk/sessions/new"
        body = {"user_token": self.token}
        self.get(url, body, Accept.JSON, ContentType.FORM, Header.AUTHORIZATION, Header.X_REQUESTED_WITH)
        soup = BeautifulSoup(self.http_response.text, "html5lib")
        self.csrf = self.get_csrf()
        self.token = re.findall(r"window.current_user_token\s+=\s+\'(\w+)\';", soup.text).pop()
        return self


class AndroidDeploy(Oauth):
    def login(self, user):
        self.user = user
        # self._set_head(Accept.HTML, ContentType.FORM)
        body = {"device": "android", "login": user.username, "password": user.password, "corp_id": "wwjupSAg8YPnH24E71ZF"}

        self.http_response = self._http_session.post(url=self._str_domain + "/api/v2/auth/login", data=body)
        self.token = self._assert_response().json()["data"]["user_token"]
        return self

    # 新增商机
    def apply(self):
        logging.info("新增%s：%s" % (self._business.enum_type.name, self._business.title))
        time.sleep(5)
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        url = "%s/api/v2/%s" % (self._str_domain, self._business.plural)
        self.http_response = self._http_session.post(url, data=self._business.apply(self.user))
        self._business.id = json.loads(self.http_response.text)["data"]["id"]
        return self._assert_response()

    # 获取商机审批状态
    def get_business_info(self, business):
        url = "%s/api/v2/%s/%s" % (self._str_domain, business.plural, business.id)
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        self.http_response = self._http_session.get(url)
        self._assert_response()
        return self.http_response.json()["data"]["approve_status_i18n"]

    # 执行审批
    def approval(self, approval_step):
        time.sleep(3)
        logging.info("审批%s：%s" % (self._business.enum_type.name, self._business.title))
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        url = "%s/api/v2/approvals/%s/%s" % (self._str_domain, self._business.id, approval_step.enum_result.value)
        self.http_response = self._http_session.post(url, data=self._business.approve(approval_step.int_step, self.csrf))
        approval_step.test_step.call(self.user)
        return self._assert_response()


class PcDeploy(Oauth, UcDeploy):
    pass
