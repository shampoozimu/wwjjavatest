import logging
import unittest2
from parameterized import parameterized

from crm.approvals import provider
from crm.approvals.framework import ApprovalTestCase, ResultEnum
from crm.pojo import EnumBusiness, BusinessFactory
from crm.utils import SettingSwitch, PcDeploy
from testCase.component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum, Context, Configure


# 审批流程测试驱动器
# 合同/商机/客户 通用型
class ApprovalDriver(unittest2.TestCase):
    # 初始化环境参数
    enum_server = ServerEnum.CRM
    enum_environment = EnvironmentEnum.TEST
    enum_platform = PlatformEnum.ANDROID
    enum_business = EnumBusiness.客户

    @classmethod
    def setUpClass(cls):
        logging.info("====执行全局初始化程序====")

    @classmethod
    def tearDownClass(cls):
        logging.info("====执行全局销毁程序====")

    def setUp(self):
        logging.info("====执行setUp模拟初始化固件====")
        # # 初始化业务类型
        # self.__business = BusinessFactory.get_instance(self.enum_business, approve_status="applying")
        # configure = Configure(self.enum_server, self.enum_environment, self.enum_platform)
        #
        # # 执行初始化环境
        # Context.instance(configure, provider)
        # [user.session.build(self.__business) for user in Context.user_factory.users]
        #
        # self.__user_applier = Context.user_factory.find_authority_user("applier")
        # self.__user_super = Context.user_factory.find_authority_user("super")
        #
        # self.__user_pc = Context.user_factory.find_authority_user("pc")
        # self.__user_current = None

    def tearDown(self):
        logging.info("====调用tearDown模拟销毁固件====")

    def __user_shift(self, user):
        logging.info("切换操作人：%s" % user)
        self.__user_current = user

    # 测试驱动：商机审批
    @parameterized.expand(input=provider.data)
    def test_opportunity(self, provider):
        test_case = ApprovalTestCase(provider)
        logging.info("开始执行用例!")
        test_case.log()
        self.setting(test_case)
        self.apply()
        [self.approve_step(test_step) for test_step in test_case.test_step_list]
        self.assert_notifications(test_case.test_step_list)

    # 设置审批类型
    def setting(self, test_case):
        logging.info("设置%s审批" % EnumBusiness(self.enum_business).name)
        # 设置审批级数，切换到admin
        self.__user_shift(self.__user_pc)
        # 清除所有已存在的审批
        self.__clear_all()

        self.__user_current.session.approval_setting(test_case)
        logging.info("成功！设置%s级审批" % len(test_case.list_approval_settings))
        logging.info("审批设置详情：%s" % len(test_case.list_approval_settings))

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
    def approve_step(self, test_step):
        # 遍历步骤中的所有用户
        for approval_step in test_step.approval_step_list:
            logging.info(approval_step)
            # 第一步，切换用户
            self.__user_shift(approval_step.user)
            # 检查审批单状态
            response = self.__user_current.session.approval(approval_step)
            # 验证审批后状态
            self.assert_status(approval_step.get_exp_str())
            # 处理无权限情况
            if ResultEnum.无权限 == test_step.enum_result:
                self.assertFalse(response.ok)
                logging.info("无权限审批未完成验证通过")

    def assert_status(self, exp):
        expected = exp
        actual = self.__user_super.session.get_business_info(self.__business)
        self.assertEqual(expected, actual)
        logging.info("状态验证通过：title:%s;status:%s" % (self.__business.title, actual))

    def assert_notifications(self, test_step_list):
        logging.info("消息通知验证%s" % self.__business.title)

        self.__user_applier.oauth_class = PcDeploy
        self.__user_applier.login()

        list_expected = list()
        [list_expected.extend(step.get_str_notifications()) for step in test_step_list]
        list_actual = self.__user_applier.session.notifications()
        list_actual.reverse()

        for expexted, actual in zip(list_expected, list_actual):
            logging.info("预期值：%s；实际值：%s" % (expexted, actual))
            self.assertTrue(expexted in actual)
