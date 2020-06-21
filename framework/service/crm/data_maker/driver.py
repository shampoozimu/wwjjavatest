import logging
from os import path
import unittest2

from parameterized import parameterized

from service.crm.pojo import EnumBusiness, BusinessFactory, UserPo, EnumCategory, EnumStatus
from component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum, Context, ServerConfig
from service.crm.utils import EnumOauth


class DataMakerDriver(unittest2.TestCase):
    # 初始化环境参数
    business = BusinessFactory.get_instance(type=EnumBusiness.线索)

    @classmethod
    def setUpClass(cls):
        cls.config = ServerConfig(path=path.join(path.dirname(__file__), "..", "config.yaml"), enum_oauths=EnumOauth)
        Context.instance(server_config=cls.config, user_po_clazz=UserPo)
        cls.user_factory = Context.user_factory
        [user.session.builder(business=cls.business) for user in cls.user_factory.users]
        logging.info("====执行全局初始化程序====")

    @classmethod
    def tearDownClass(cls):
        logging.info("====执行全局销毁程序====")

    def setUp(self):
        logging.info("====执行setUp模拟初始化固件====")
        # 初始化全局配置
        # 初始化环境参数


    def tearDown(self):
        logging.info("====调用tearDown模拟销毁固件====")

    # 测试驱动：生成测试数据
    # @parameterized.expand(input=provider.data)
    #  测试驱动改成excel形式
    @parameterized.expand(input=[(0,)])
    @unittest2.skip
    def test_data_init(self, provider):
        # authority = provider.pop("authority")
        # 实例化test_case
        # business = BusinessFactory.get_instance(self.enum_business, **provider)
        self.user_factory.find_any().session.apply()
        [user.session.revisit(category="电话", status="初访") for user in self.user_factory.users]

    # def test_sign(self):
    #     self.user_factory.find_any().session.apply()
    #     [user.session.checkin() for user in self.user_factory.users]

    # def test_apply(self):
    #     [user.session.apply() for user in self.user_factory.users]

    def test_revisit(self):
        self.user_factory.find_any().session.apply()
        [user.session.revisit(category=EnumCategory.电话, status=EnumStatus.初访) for user in self.user_factory.users]
