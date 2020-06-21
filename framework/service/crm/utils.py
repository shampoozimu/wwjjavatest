import re
import time
from enum import IntEnum, Enum
import logging
# 通用功能模块
# 审批人类型

from bs4 import BeautifulSoup

from component.oauth import BaseSession, HeaderFactory
from service.crm.pojo import dict_result


class SettingSwitch(IntEnum):
    OFF = 0
    ON = 1


class Session(BaseSession):
    def __init__(self, user):
        super().__init__(user)

    # 获取审批状态
    def get_business_info(self, business):
        url = "%s/%s" % (self._server.domain, business.plural)
        body = {"scope": "all_own", "per_page": 10, "type": "advance", "section_only": True}
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM)
        self.http_response = self.get(url, body=body)
        return BeautifulSoup(self.http_response.text, "html5lib").select("table>tbody>tr[data-id=\"%s\"]>td[data-column=\"approve_status_i18n\"]>div.value" % self.business.id).pop().text.strip()

    # 审批设置开关
    def setting_on_off(self, switch):
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM, HeaderFactory.XCsrfToken.dynamic(self.csrf))
        url = self._server.domain + "/settings/%s_approve/update" % self.business.singular
        body = {
            "%s_approve[enable_%s_approve]" % (self.business.singular, self.business.singular): switch.value
        }
        self.http_response = self.put(url, body=body)

    # 审批级数设置
    def approval_setting(self, approve_flow):
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM, HeaderFactory.XCsrfToken.dynamic(self.csrf))
        url = self._server.domain + "/settings/%s_approve/update" % self.business.singular
        self.http_response = self.put(url, body=self.business.setting(self.csrf, approve_flow))

    # 新增商机
    def apply(self):
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM)
        url = "%s/api/%s" % (self._server.domain, self.business.plural)
        self.http_response = self.post(url, body=self.business.apply(self.csrf, self.user))
        logging.info("新增%s：%s" % (self.business.enum_type.name, self.business.title))
        self.business.id = self.http_response.as_json("data", "id").get()

    # 执行审批
    def approval(self, approval_step):
        logging.info("审批%s：%s" % (self.business.enum_type.name, self.business.title))
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM)
        url = "%s/api/approvals/%s/%s" % (self._server.domain, self.business.id, dict_result[approval_step.str_result])
        return self.post(url, body=self.business.approve(approval_step.int_num, self.csrf))

    # 消息通知
    def notifications(self):
        url = "%s/notifications" % self._server.domain
        self.http_response = self.get(url)
        return [node.text.strip() for node in BeautifulSoup(self.http_response.text, "html5lib").select("section#notification_table tbody>tr>td>a.text-primary[href$=\"%s\"]" % self.business.id)]

    # 跟进
    def revisit(self, **kwargs):
        logging.info("跟进")
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM)
        url = "%s/api/%s/%s/revisit_logs" % (self._server.domain, self.business.plural, self.business.id)
        self.http_response = self.post(url, body=self.business.revisit(self.csrf, **kwargs))


# 私有化环境
class PrivateDeploy(Session):
    def __init__(self, user):
        super().__init__(user)
        self.token = None

    # 私有化环境登录方式
    def login(self):
        self.get(self._server.domain)
        # time.sleep(2)
        self.csrf = self.get_csrf()
        # 然后，以csrf作为参数
        # 用phone和pwd登录
        body = {
            "utf8": "✓",
            "authenticity_token": self.csrf,
            "user[login]": self.user.phone,
            "user[password]": self.user.password,
            "commit": "登 录"
        }
        self.http_response = self.post(self._server.domain + "/users/sign_in", body=body)
        # 获取最终的cookie和csrf
        self.cookie = self.get_cookies()
        self.csrf = self.get_csrf()
        return self


# 钉钉测试环境
class DingdingDeploy(Session):
    def login(self):
        time.sleep(2)
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM, HeaderFactory.XRequestedWith.XML)
        body = {
            "login": self.user.phone,
            "password": self.user.password,
            "device": "web"
        }
        # verify=False:不验证ssl
        self.http_response = self.post(url=self._server.domain + "/api/v2/auth/login", body=body)
        self.token = self.get_json_property("data", "user_token")
        # self.user.id = self.get_json_property("data", "user_id")

        url = self._server.domain + "/dingtalk/sessions/new"
        body = {"user_token": self.token}
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM, HeaderFactory.XRequestedWith.XML)
        self.get(url, body=body)
        soup = BeautifulSoup(self.http_response.text, "html5lib")
        self.csrf = self.get_csrf()
        self.token = re.findall(r"window.current_user_token\s+=\s+\'(\w+)\';", soup.text).pop()
        # self.str_user_info = re.findall(r"window.current_user\s+=(.*?);", soup.text, re.DOTALL).pop()
        # self.user.uid = re.findall(r"uid:\s+(\d+?),", self.str_user_info).pop()
        # self.user.name = re.findall(r"name:\s+\'(.+?)\'", self.str_user_info).pop()
        logging.info("钉钉登陆成功：用户信息：phone=%s;name=%s" % (self.user.phone, self.user.dto.name))
        return self

    # 签到
    def checkin(self):
        logging.info("签到%s：%s" % (self.business.enum_type.name, self.business.title))
        self._clear_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.JSON)
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        url = "%s/api/v2/checkins" % (self._server.domain)
        logging.info(self.business.checkin())
        self.http_response = self.post(url, json=self.business.checkin(), verify=False)


class AndroidDeploy(Session):
    def login(self):
        # self._set_head(Accept.HTML, ContentType.FORM)
        body = {"device": "android", "login": self.user.phone, "password": self.user.password, "corp_id": "wwjupSAg8YPnH24E71ZF"}

        self.http_response = self.post(url=self._server.domain + "/api/v2/auth/login", body=body)
        self.token = self.http_response.as_json("data", "user_token")
        return self

    # 新增商机
    def apply(self):
        logging.info("新增%s：%s" % (self.business.enum_type.name, self.business.title))
        time.sleep(5)
        self._set_head(HeaderFactory.Accept.JSON, HeaderFactory.ContentType.FORM, HeaderFactory.XRequestedWith.XML)
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        url = "%s/api/v2/%s" % (self._server.domain, self.business.plural)
        self.http_response = self.post(url, body=self.business.apply(self.user))
        self.business.id = self.http_response.as_json("data", "id")

    # 获取商机审批状态
    def get_business_info(self, business):
        url = "%s/api/v2/%s/%s" % (self._server.domain, business.plural, business.id)
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        self.http_response = self.get(url)
        return self.http_response.as_json("data", "approve_status_i18n")

    # 执行审批
    def approval(self, approval_step):
        time.sleep(3)
        logging.info("审批%s：%s" % (self.business.enum_type.name, self.business.title))
        self.set_authorization(token=self.token, device=self._server.device, version_code=self._server.version_code)
        url = "%s/api/v2/approvals/%s/%s" % (self._server.domain, self.business.id, dict_result[approval_step.str_result])
        self.http_response = self.post(url, body=self.business.approve(approval_step.int_step, self.csrf))
        approval_step.test_step.call(self.user)


class PcDeploy(Session):
    def login(self):
        super().login()
        self.uid = self.http_response.as_json("data","uid").get()
        self.ticket = self.http_response.as_json("data", "ticket").get()
        self._set_head(HeaderFactory.Accept.HTML, HeaderFactory.ContentType.FORM, HeaderFactory.XRequestedWith.XML)
        self.http_response = self.get(self._server.domain, body={"st": self.ticket})
        self.cookie = self.get_cookies()
        self.csrf = self.get_csrf()
        return self


class EnumOauth(Enum):
    Oauth = Session
    PrivateDeploy = PrivateDeploy
    DingdingDeploy = DingdingDeploy
    AndroidDeploy = AndroidDeploy
    PcDeploy = PcDeploy
