from enum import IntEnum, unique
from testCase.component.oauth import User


@unique
class EnvironmentEnum(IntEnum):
    TEST = 1
    STAGE = 2
    私有化 = 99


@unique
class PlatformEnum(IntEnum):
    钉钉 = 1
    企业微信 = 2
    PC = 3
    ANDROID = 4
    IOS = 5


@unique
class ServerEnum(IntEnum):
    UC = 0
    CRM = 1
    JXC = 2


class Context:
    # 上下文类，全局容器
    # configure：包含server/environment/platform
    # server：包含被加工的setting信息
    # users：user及其oauth对象信息
    setting = {
        ServerEnum.UC: {
            EnvironmentEnum.TEST: {
                PlatformEnum.PC: {
                    "domain": "https://uc-test.weiwenjia.com",
                }
            },
            EnvironmentEnum.STAGE: {
                PlatformEnum.PC: {
                    "domain": "https://uc-staging.weiwenjia.com",
                }
            }
        },
        ServerEnum.CRM: {
            EnvironmentEnum.私有化: {
                PlatformEnum.IOS: {
                    "domain": "http://crm-private-deploy.ikcrm.com",
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "ios",
                    "approval": {"customer": {"id": "104"}}
                },
                PlatformEnum.ANDROID: {
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "android"
                },
                PlatformEnum.PC: {
                    "attr_pointer": PlatformEnum.IOS
                }
            },
            EnvironmentEnum.TEST: {
                PlatformEnum.钉钉: {
                    "domain": "https://ding-test.ikcrm.com",
                    "attr_pointer": PlatformEnum.钉钉,
                    "approval": {"customer": {"id": "1234734"}}
                },
                PlatformEnum.IOS: {
                    "domain": "https://ik-test.ikcrm.com",
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "ios",
                    "approval": {"customer": {"id": "1365828"}}
                },
                PlatformEnum.ANDROID: {
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "android"
                },
                PlatformEnum.PC: {
                    "attr_pointer": PlatformEnum.IOS
                }
            },
            EnvironmentEnum.STAGE: {
                PlatformEnum.IOS: {
                    "domain": "https://ik-staging.ikcrm.com",
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "ios",
                    "approval": {"customer": {"id": "254370"}}
                },
                PlatformEnum.ANDROID: {
                    "attr_pointer": PlatformEnum.IOS,
                    "version_code": "3.31.1",
                    "device": "android"
                },
                PlatformEnum.PC: {
                    "attr_pointer": PlatformEnum.IOS
                }
            }
        },
        ServerEnum.JXC: {
            EnvironmentEnum.TEST: {
                PlatformEnum.IOS: {
                    "domain": "http://lixiaojxc-test.ikcrm.com",
                    "attr_pointer": PlatformEnum.IOS
                },
                PlatformEnum.钉钉: {
                    "attr_pointer": PlatformEnum.IOS
                }

            },
        }
    }
    configure = None
    server = None
    user_factory = None

    @classmethod
    def instance(cls, config, provider):
        cls.configure = config
        # server依赖configure
        cls.server = Server(cls.configure)
        # user依赖server
        cls.user_factory = UserFactory(cls.server, provider.users[config.enum_environment][cls.server.attr_pointer], provider.oauth_classes[config.enum_environment][config.enum_platform])


class UserFactory:
    def __init__(self, server, users, oauth_class):
        self.server = server
        self.oauth_class = oauth_class
        self.users = [User(user, self) for user in users]
        [user.builder().login() for user in self.users]

    # 查找属性匹配的用户
    def find_users(self, dict_attr):
        return [user for user in self.users if user.match(dict_attr)]

    def find_user(self, dict_attr):
        return self.find_users(dict_attr).pop() if dict_attr else None

    # 查找权限匹配的用户
    def find_authority_users(self, authority):
        return [user for user in self.users if user.match_authority(authority)]

    def find_authority_user(self, authority):
        list_users = self.find_authority_users(authority)
        return list_users.pop() if list_users else None

    def find_any(self):
        return self.users[0]


class Server:
    def __init__(self, config):
        self.config = config
        self.enum_server = config.enum_server
        self.enum_environment = config.enum_environment
        self.enum_platform = config.enum_platform
        # 自动设置attr_pointer/version_code/device/approval等属性
        [self.__setattr__(k, v) for k, v in Context.setting[self.enum_server][self.enum_environment][self.enum_platform].items()]
        # uc系统url
        self.str_domain = Context.setting[self.enum_server][self.enum_environment][self.attr_pointer]["domain"]
        self.str_uc_domain = Context.setting[ServerEnum.UC][self.enum_environment][PlatformEnum.PC]["domain"]
        self.domain = Server.Domain(self.str_domain, self.str_uc_domain)
        # attr_pointer：属性指针，pc/android等平台的属性都作为公共属性储存在ios平台中
        # approval属性转化对象
        self.approval = Approval(Context.setting[self.enum_server][self.enum_environment][self.attr_pointer].get("approval"))

    class Domain:
        def __init__(self, str_domain, str_login=None):
            self.str_domain = str_domain
            self.str_login = str_login or self.str_domain


class Approval:
    # 审批所需的一些属性
    def __init__(self, dict_approval):
        if dict_approval:
            if "customer" in dict_approval:
                self.customer = Approval.Customer(dict_approval.get("customer"))

    class Customer:
        # 审批请求所需要的用户属性
        def __init__(self, dict_proto):
            self.dict_proto = dict_proto
            [self.__setattr__(attr, value) for attr, value in self.dict_proto.items()]


class Configure:
    def __init__(self, enum_server, enum_environment, enum_platform):
        self.enum_server = enum_server
        self.enum_environment = enum_environment
        self.enum_platform = enum_platform
