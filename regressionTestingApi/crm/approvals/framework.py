import logging
import random
from enum import Enum

from testCase.component.confiuration import Context


class MultistepEnum(Enum):
    # 负责人主管
    负责人主管 = "superior"
    # 上一级审批人主管
    上一级审批人主管 = "previous_superior"
    # 任意一人
    任意一人 = "specified"
    # 多人会签
    多人会签 = "specified_jointly"
    超管 = 0


class ResultEnum(Enum):
    通过 = "approve"
    否决 = "deny"
    撤销 = "revert"
    驳回 = 0
    无权限 = 1


# 描述每一级别审批详情
class ApprovalSetting:
    def __init__(self, int_step, enum_step, user_list=None):
        # 当前审批级数
        self.int_step = int_step
        self.enum_step = enum_step
        self.user_list = user_list or tuple()

    def get_body(self):
        dict_body = dict()
        dict_body["step"] = str(self.int_step)
        dict_body["enable"] = "1"
        dict_body["type"] = self.enum_step.value
        dict_body["user_ids]["] = "" if self.enum_step in [MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管] else [user.id for user in self.user_list]
        return dict_body

    def __str__(self):
        return "%s级审批：审批类型：%s" % (self.int_step, self.enum_step.name)


class ApprovalTestCase:
    def __init__(self, test_case):
        self.test_case = list(test_case)

        # provider最后一个参数标识：中断步骤编号
        self.int_interrupt = self.test_case.pop()
        # provider最后第二个参数标识：最终审批状态
        self.enum_result = self.test_case.pop()
        # pop后，数组长度==审批级数
        # 如果中断点不在索引范围内，默认全流程
        # 如果终端类型为“通过”则默认全流程
        if self.int_interrupt - 1 not in range(len(self.test_case)) or self.enum_result in [ResultEnum.通过, ResultEnum.驳回]:
            self.int_interrupt = len(self.test_case)
        # 撤销操作只能发生在第一步
        elif ResultEnum.撤销 == self.enum_result:
            self.int_interrupt = 1
        # 储存上一步的审批人列表
        # 以便后续通过主管关系层层向上操作
        # self.__user_of_step_list = list()

        # 组装步骤
        self.test_step_list = list()
        self.list_approval_settings = list()
        self.__builder()

    def __builder(self):
        ats_test_step = None
        for step_num, step_type in enumerate(self.test_case):
            test_step_users = None

            # 1.按照步骤设置情况，安排登录审核人员
            if MultistepEnum.负责人主管 == step_type:
                # 设置时为空数组
                self.list_approval_settings.append(ApprovalSetting(step_num + 1, step_type))
                # 运行时
                test_step_users = [Context.user_factory.find_authority_user("applier").director]
            elif MultistepEnum.上一级审批人主管 == step_type:
                # 设置时为空数组
                self.list_approval_settings.append(ApprovalSetting(step_num + 1, step_type))
                # 运行时，取上一运行时（上一次循环）实际审批人的主管
                test_step_users = [ats_test_step.user_list[0].director]
            elif MultistepEnum.任意一人 == step_type:
                list_users = Context.user_factory.find_authority_users("normal")
                # 所有nomal成员（实际为两人）
                self.list_approval_settings.append(ApprovalSetting(step_num + 1, step_type, list_users))
                # 随机取一人
                test_step_users = random.choices(list_users)
            elif MultistepEnum.多人会签 == step_type:
                list_users = Context.user_factory.find_authority_users("normal")
                # 运行时=设置时
                self.list_approval_settings.append(ApprovalSetting(step_num + 1, step_type, list_users))
                # 任一人否决，流程即结束
                test_step_users = list_users
            elif MultistepEnum.超管 == step_type:
                # 超管用例，审批级数设置为任意一人
                self.list_approval_settings.append(ApprovalSetting(step_num + 1, MultistepEnum.任意一人, Context.user_factory.find_authority_users("normal")))
                # 取超管中的一人
                test_step_users = [Context.user_factory.find_authority_user("super")]

            if step_num + 1 <= self.int_interrupt:
                ats_test_step = ApprovalTestStep(self, step_num + 1, test_step_users)
                self.test_step_list.append(ats_test_step)

    def log(self):
        logging.info("审批设置:级数：%s" % len(self.list_approval_settings))
        [logging.info(apv) for apv in self.list_approval_settings]
        logging.info("审批运行设置：级数：%s" % len(self.test_step_list))
        [logging.info(test_step) for test_step in self.test_step_list]


class ApprovalTestStep:
    def __init__(self, test_case, int_step, user_list):
        self.test_case = test_case
        self.int_step = int_step
        # 首先赋值enum_result：__get_user_list依赖enum_result做判断
        # 除了最后一步，所有步骤都通过
        self.enum_result = self.test_case.enum_result if self.test_case.int_interrupt == self.int_step else ResultEnum.通过
        # 然后赋值user_list：self.__checks需要遍历user_list
        self.user_list = self.__get_user_list(user_list)
        self.__checks = dict(zip([id(user) for user in self.user_list], [False] * len(self.user_list)))

        self.approval_step_list = list()
        for i, user in enumerate(self.user_list):
            self.approval_step_list.append(ApprovalUserStep(self, i, user))
            if ResultEnum.驳回 == self.enum_result:
                self.approval_step_list.append(RejectUserStep(self, user))

    def __get_user_list(self, user_list):
        if ResultEnum.撤销 == self.enum_result:
            # 如果是撤销操作，将操作人改成申请人
            return [Context.user_factory.find_authority_user("applier")]
        elif ResultEnum.无权限 == self.enum_result:
            return [Context.user_factory.find_authority_user("illegal")]
        else:
            return user_list

    def call(self, user):
        self.__checks[id(user)] = True

    # 是否所有用户都操作完成
    def is_step_finished(self):
        return all(self.__checks.values())

    def get_str_notifications(self):
        if ResultEnum.驳回 == self.enum_result:
            return ["%s级审批人 %s 审批通过了你的" % (self.int_step, self.user_list[-1].name), "%s审批驳回了你的" % self.user_list[-1].name]
        else:
            return ["%s级审批人 %s 审批%s了你的" % (self.int_step, self.user_list[-1].name, self.enum_result.name)]

    def __str__(self):
        return "%s级审批；审批类型：%s；审批操作：%s" % (self.int_step, self.enum_result.name, ",".join([approval.__str__() for approval in self.approval_step_list]))

# 每个用户的审批情况
# 用于多人会签的代码优化
class ApprovalUserStep:
    def __init__(self, test_step, user_step_number, user):
        self.test_step = test_step
        self.user = user
        # 驳回操作：通过->否决
        # 如果是会签，且否决，则，最后一人否决，之前所有人都通过
        self.enum_result = ResultEnum.通过 if user_step_number + 1 < len(self.test_step.user_list) or ResultEnum.驳回 == self.test_step.enum_result else self.test_step.enum_result

        self.int_step = self.test_step.int_step

    def get_exp_str(self):
        str_expected = None
        # 至少一个用户微操作未完成
        if not self.test_step.is_step_finished():
            str_expected = "待%s级审批" % self.int_step
        elif ResultEnum.无权限 == self.enum_result:
            str_expected = "待%s级审批" % self.int_step
        # 当前处于最后一步
        elif self.test_step.test_case.int_interrupt == self.int_step:
            str_expected = "已%s" % self.enum_result.name
        else:
            str_expected = "待%s级审批" % (self.int_step + 1)
        return str_expected

    def __str__(self):
        return "step:%s;user:%s" % (self.int_step, self.user)


class RejectUserStep(ApprovalUserStep):
    def __init__(self, test_step, user):
        self.test_step = test_step
        self.user = user
        self.enum_result = ResultEnum.否决

        self.int_step = self.test_step.int_step

        def get_exp_str(self):
            return "已否决"
