import logging
import unittest2

from parameterized import parameterized

from crm.pojo import EnumBusiness, BusinessFactory
from crm.report_center import provider
from testCase.component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum, Context, Configure


class ReportCenterDriver(unittest2.TestCase):
    # 初始化环境参数
    enum_server = ServerEnum.CRM
    enum_environment = EnvironmentEnum.TEST
    enum_platform = PlatformEnum.PC
    enum_business = EnumBusiness.合同

    @classmethod
    def setUpClass(cls):
        logging.info("====执行全局初始化程序====")

    @classmethod
    def tearDownClass(cls):
        logging.info("====执行全局销毁程序====")

    def setUp(self):
        logging.info("====执行setUp模拟初始化固件====")
        # 初始化业务类型
        # self.__business = BusinessFactory.get_instance(self.enum_business)
        # 初始化全局配置
        configure = Configure(self.enum_server, self.enum_environment, self.enum_platform)
        # 初始化环境参数
        Context.instance(configure, provider)
        # 取任一用户
        self.__user_current = None

    def tearDown(self):
        logging.info("====调用tearDown模拟销毁固件====")

    # 测试驱动：生成测试数据
    @parameterized.expand(input=provider.data)
    def test_data_init(self, provider):
        authority = provider.pop("authority")
        # 实例化test_case
        business = BusinessFactory.get_instance(self.enum_business, **provider)
        Context.user_factory.find_authority_user(authority).session.build(business).apply()
