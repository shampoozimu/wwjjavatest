import logging
from os import path

import unittest2
from parameterized import parameterized

from service.crm.pojo import EnumBusiness, BusinessFactory, UserPo, ApproveFlow
from service.crm.utils import SettingSwitch, EnumOauth
from component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum, Context, Provider, ServerConfig


# 审批流程测试驱动器
# 合同/商机/客户 通用型


class ApprovalDriver(unittest2.TestCase):
    # 初始化环境参数
    business = BusinessFactory.get_instance(EnumBusiness.合同, approve_status="applying")
    int_approve_level = 0
    provider = Provider(workbook_path=path.join(path.dirname(__file__), "..", "approve.xlsx"))

    @classmethod
    def setUpClass(cls):
        cls.config = ServerConfig(path=path.join(path.dirname(__file__), "..", "config.yaml"), enum_oauths=EnumOauth)
        logging.info("====执行全局初始化程序====")
        Context.instance(server_config=cls.config, user_po_clazz=UserPo)
        cls.user_factory = Context.user_factory
        [user.session.builder(business=cls.business) for user in cls.user_factory.users]

    @classmethod
    def tearDownClass(cls):
        logging.info("====执行全局销毁程序====")

    def setUp(self):
        logging.info("====执行setUp模拟初始化固件====")
        self.__user_applier = self.user_factory.find_authority_user("applier")
        self.__user_super = self.user_factory.find_authority_user("super")
        self.__user_pc = self.user_factory.find_authority_user("pc")
        self.__user_current = None

    def tearDown(self):
        logging.info("====调用tearDown模拟销毁固件====")

    def __user_shift(self, user):
        logging.info("切换操作人：%s" % user)
        self.__user_current = user

    # 测试驱动：商机审批
    @parameterized.expand(input=provider.record_provider(str(int_approve_level) + "级审批"))
    # @unittest2.skip
    def test_opportunity(self, provider):
        work_flow = ApproveFlow(provider, self.user_factory)
        self.setting(work_flow)
        self.apply()
        [self.approve_step(step) for step in work_flow]

    # 设置审批类型
    def setting(self, approve_flow):
        logging.info("设置%s审批" % self.business.enum_type.name)
        # 设置审批级数，切换到admin
        self.__user_shift(self.__user_pc)
        # 清除所有已存在的审批
        self.__clear_all()

        self.__user_current.session.approval_setting(approve_flow)
        logging.info("成功！设置%s级审批" % len(approve_flow.list_settings))
        logging.info("审批设置详情：%s" % len(approve_flow.list_settings))

    # 清除所有已存在的审批
    def __clear_all(self):
        self.__user_current.session.setting_on_off(SettingSwitch.OFF)
        self.__user_current.session.setting_on_off(SettingSwitch.ON)

    # 新增商机
    def apply(self):
        # 生成商机随机名称
        self.__user_shift(self.__user_applier)
        self.__user_current.session.apply()
        self.assert_status("待1级审批")

    # 审批步骤
    def approve_step(self, step):
        # 遍历步骤中的所有用户
        for approval_step in step:
            logging.info(approval_step)
            # 第一步，切换用户
            self.__user_shift(approval_step.user)
            # 检查审批单状态
            response = self.__user_current.session.approval(approval_step)
            # 验证审批后状态
            self.assert_status(approval_step.str_expect)
            # 处理无权限情况
            if "无权限" == step.str_result:
                self.assertFalse(response.ok)
                logging.info("无权限审批未完成验证通过")

    def assert_status(self, exp):
        expected = exp
        actual = self.__user_super.session.get_business_info(self.business)
        self.assertEqual(expected, actual)
        logging.info("状态验证通过：title:%s;status:%s" % (self.business.title, actual))

    def assert_notifications(self, test_step_list):
        logging.info("消息通知验证%s" % self.business.title)

        # self.__user_applier.oauth_clazz = PcDeploy
        # self.__user_applier.login()

        list_expected = list()
        [list_expected.extend(step.get_str_notifications()) for step in test_step_list]
        list_actual = self.__user_applier.session.notifications()
        list_actual.reverse()

        for expexted, actual in zip(list_expected, list_actual):
            logging.info("预期值：%s；实际值：%s" % (expexted, actual))
            self.assertTrue(expexted in actual)
