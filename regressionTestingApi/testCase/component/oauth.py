import json
import logging, requests
from enum import Enum
from bs4 import BeautifulSoup


class ContentType(Enum):
    FORM = "application/x-www-form-urlencoded; charset=UTF-8"
    JSON = "application/json; charset=UTF-8"
    HTML = "text/html; charset=utf-8"


class Accept(Enum):
    HTML = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    JSON = "application/json, text/javascript, */*; q=0.01"


class Header(Enum):
    X_REQUESTED_WITH = {"X-Requested-With": "XMLHttpRequest"}
    APP_TOKEN = {"appToken": "f6620ff6729345c8b6101174e695d0ab"}
    PLATFORM = {"platform": "IK"}


# http_session基类
class BaseOauth:
    def __init__(self, server):
        self._server = server
        self.domain = self._server.domain
        self._str_domain = self.domain.str_domain
        self._http_session = requests.session()
        # self._business = self._server.config.business
        self.cookie = None
        self.csrf = None
        # self.user = None
        # self.token = None
        # self.ticket = None
        # self.uid = None
        # self.http_response = None

    # 设置消息头
    def _set_head(self, accept, content, *headers):
        self._http_session.headers.update({"Accept": accept.value})
        self._http_session.headers.update({"Content-Type": content.value})
        self._http_session.headers.update({'X-CSRF-Token': self.csrf})
        self._http_session.headers.update({'Cookie': self.cookie})
        [self._http_session.headers.update(header.value) for header in headers]

    def set_authorization(self, **kwargs):
        token_value = "Token " + ",".join(["%s=\"%s\"" % (k, v) for k, v in kwargs.items()])
        self._http_session.headers.update({"Authorization": token_value})

    # 响应校验
    def _assert_response(self):
        if self.http_response.status_code not in [200, 204]:
            logging.error("请求url：%s失败，status_code：%s" % (self.http_response.url, self.http_response.status_code))
        else:
            logging.info("请求url：%s成功" % self.http_response.url)
        return self.http_response

    def build(self, business):
        self._business = business
        return self

    # get请求
    def get(self, url, body=None, accept=Accept.HTML, content_type=ContentType.FORM, *headers):
        self._set_head(accept, content_type, *headers)
        self.http_response = self._http_session.get(url, data=body)
        return self._assert_response()

    # post请求
    def post(self, url, body=None, accept=Accept.HTML, content_type=ContentType.FORM, *headers):
        self._set_head(accept, content_type, *headers)
        self.http_response = self._http_session.get(url, data=body)
        return self._assert_response()

    # 获取cookie
    def get_cookies(self):
        return self.http_response.headers['Set-Cookie']

    # 获取csrf
    def get_csrf(self):
        return BeautifulSoup(self.http_response.text, "html5lib").select("head>meta[name=\"csrf-token\"]").pop().attrs["content"]

    def get_json_property(self, *args):
        property = json.loads(self.http_response.content)
        for arg in args:
            property = property[arg]
        return property


# 登录uc
class UcDeploy(BaseOauth):
    def login(self, user):
        self.user = user
        self._set_head(Accept.JSON, ContentType.JSON, Header.APP_TOKEN, Header.PLATFORM)
        url = self.domain.str_login + "/api/sso/login"
        body = {
            "noticeType": "other",
            "password": self.user.password,
            "phone": self.user.username,
            "type": "login"
        }
        self.http_response = self._http_session.post(url=url, data=json.dumps(body))
        self._assert_response()
        self.uid = self.http_response.json()['data']['uid']
        self.ticket = self.http_response.json()['data']['ticket']

        self.http_response = self.get(self._str_domain, {"st": self.ticket}, Accept.HTML, ContentType.FORM, Header.X_REQUESTED_WITH)
        self.cookie = self.get_cookies()
        self.csrf = self.get_csrf()
        return self


class User:
    def __init__(self, dict_user, factory):
        self.director = None
        self.session = None
        self.factory = factory

        # self.server = server
        # 将user从dictionary转化为对象
        self.dict_user = dict_user
        # 登录密码统一默认值
        self.password = "Ik123456"
        [self.__setattr__(k, v) for k, v in dict_user.items()]
        if not hasattr(self, "oauth_class"):
            # 如果本身包含oauth，则使用oauth
            # 否则使用server提供的oauth
            self.oauth_class = self.factory.oauth_class

    # 必须用builder
    # init步骤将dict转化成User对象
    # builder通过find_user查找director
    def builder(self):
        # 通过属性查找director对象
        self.director = self.factory.find_user(self.director)
        # 由于Server.builder中定义了uc_domain
        # user不能再User.__init__()中创建登录session
        # 实例化登录session
        return self

    def login(self):
        self.session = self.oauth_class(self.factory.server).login(self)
        return self

    # 判断属性列表是否与本user对象匹配
    def match(self, dict_attr):
        return all([self.dict_user.get(key) == value for key, value in dict_attr.items()])

    # 判断权限是否匹配与本user对象匹配
    def match_authority(self, authority):
        return hasattr(self, "authority") and authority in self.authority

    # 默认打印所有属性
    def __str__(self):
        return ";".join(["%s:%s" % (key, value) for key, value in self.dict_user.items()])
