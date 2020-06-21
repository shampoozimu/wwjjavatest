import logging
import unittest2

from parameterized import parameterized

from lixiaojxc.pojo import EnumBusiness, BusinessFactory
from lixiaojxc.info import provider
from testCase.component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum, Context, Configure


class InfoDriver(unittest2.TestCase):
    # 初始化环境参数
    enum_server = ServerEnum.JXC
    enum_environment = EnvironmentEnum.TEST
    enum_platform = PlatformEnum.钉钉
    enum_business = EnumBusiness.产品

    @classmethod
    def setUpClass(cls):
        logging.info("====执行全局初始化程序====")

    @classmethod
    def tearDownClass(cls):
        logging.info("====执行全局销毁程序====")

    def setUp(self):
        logging.info("====执行setUp模拟初始化固件====")
        # 初始化业务类型
        self.__business = BusinessFactory.get_instance(self.enum_business)
        # 初始化全局配置
        configure = Configure(self.enum_server, self.enum_environment, self.enum_platform, self.__business)
        # 初始化环境参数
        Context.instance(configure, provider)

    def tearDown(self):
        logging.info("====调用tearDown模拟销毁固件====")

    # 测试驱动：生成基础资料
    # @parameterized.expand(input=provider.data)
    # def test_data_init(self, provider):
    #     authority = provider.pop("authority")
    #     # 获取业务对象
    #     business = BusinessFactory.get_instance(self.enum_business, **provider)
    #     # 查找用户，注入业务对象，申请请求
    #     Context.user_factory.find_authority_user(authority).session.build(business).apply()


