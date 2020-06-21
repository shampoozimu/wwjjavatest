import logging
from enum import Enum, IntEnum, unique
import random
import arrow
import collections

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship, backref

from component.confiuration import Context
from component.oauth import BaseUserPo
from component.utils import Random

Base = declarative_base()
db_config = Context.config.server.environment.platform.db


# ———————————————————数据持久化对象———————————————————

class UserDto(Base):
    @declared_attr
    def __tablename__(self):
        return db_config.table_name[self.__name__]

    id = Column(Integer, primary_key=True)
    superior_id = Column(Integer)
    name = Column(String)
    phone = Column(String)

    @declared_attr
    def organization_id(self):
        return Column(Integer, ForeignKey("%s.id" % db_config.table_name["OrganizationDto"]))

    @declared_attr
    def organization(self):
        return relationship("OrganizationDto", backref=backref(self.__tablename__, uselist=False))

    @declared_attr
    def departments(self):
        return relationship("UserDepDto", back_populates="user")


class DepartmentDto(Base):
    @declared_attr
    def __tablename__(self):
        return db_config.table_name[self.__name__]

    id = Column(Integer, primary_key=True)
    name = Column(String)
    organization_id = Column(Integer)
    parent_id = Column(Integer)

    @declared_attr
    def users(self):
        return relationship("UserDepDto", back_populates="department")


class UserDepDto(Base):
    @declared_attr
    def __tablename__(self):
        return db_config.table_name[self.__name__]

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("%s.id" % db_config.table_name["UserDto"]), primary_key=True)

    @declared_attr
    def department_id(self):
        return Column(Integer, ForeignKey("%s.id" % db_config.table_name["DepartmentDto"]), primary_key=True)

    @declared_attr
    def user(self):
        return relationship("UserDto", back_populates="departments")

    @declared_attr
    def department(self):
        return relationship("DepartmentDto", back_populates="users")


class OrganizationDto(Base):
    @declared_attr
    def __tablename__(self):
        return db_config.table_name[self.__name__]

    id = Column(Integer, primary_key=True)
    name = Column(String)


class UserPo(BaseUserPo):
    def _get_user_dto(self, organization):
        Base.metadata = db_config.metadata
        return self.db_session.query(UserDto).join(OrganizationDto).filter(UserDto.phone == self.phone).filter(OrganizationDto.name == organization["name"]).first()


# ———————————————————CRM枚举对象———————————————————
@unique
class EnumCategory(IntEnum):
    电话 = 323050
    QQ = 323051
    微信 = 323052
    拜访 = 323053
    邮件 = 323054
    短信 = 323055
    其他 = 323056


@unique
class EnumStatus(IntEnum):
    初访 = 322937
    意向 = 322938
    报价 = 322939
    成交 = 322940
    暂时搁置 = 322941
    # lead
    未处理 = 242719


@unique
class EnumMultistep(Enum):
    # 负责人主管
    负责人主管 = "superior"
    越级主管 = -1
    # 上一级审批人主管
    上一级审批人主管 = "previous_superior"
    # 任意一人
    任意一人 = "specified"
    # 多人会签
    多人会签 = "specified_jointly"
    超管 = 0


dict_result = {"通过": "approve", "否决": "deny", "撤销": "revert", "驳回": "deny", "无权限": "approve"}


# ———————————————————CRM业务对象———————————————————
class CRM:
    def __init__(self, enum_type, **kwargs):
        # 非必填项
        self.random = Random()
        self.enum_type = enum_type
        self.kwargs = kwargs

        self.time = arrow.now()

        # 名称
        self.telephone = Random(boolean_lower_case=False, boolean_upper_case=False).return_sample(11)
        self.amount = self.kwargs.get("amount") or 999
        self.description = Random().return_sample(99)
        self.apply_body = {
            "utf8": "✓",
        }

        # 如果相同，可以与reject合并
        self.approve_body = {
            "utf8": "✓",
            "_method": "put",
            "key": self.singular,
            "%s[approve_description]" % self.singular: self.description,
        }

        self.revisit_body = {
            "utf8": "✓",

            # request_ticket:1c70d800-94e9-4946-b617-7c3225eee818

            # contacts_ids[]:
        }

        self.checkin_body = {"checkin":
                                 {"message": "", "checkin_name": "111", "address_attributes":
                                     {"off_distance": 39, "detail_address": "123", "lng": 121.602001, "lat": 31.200028}
                                  }, "update_entity_address": False}

        self.setting_body = {
            "utf8": "✓",
            "_method": "put",
            "%s_approve[editable][enable]" % self.singular: "1",
            "%s_approve[editable][policy]" % self.singular: "can",
        }

    # 提交合同/商机/客户
    def apply(self, str_csrf, user):
        # 每一次apply生成不同的title
        self.title = self.kwargs.get("title") or Random().return_sample(20)
        self.apply_body.update({
            "authenticity_token": str_csrf,
            "%s[title]" % self.singular: self.title,
            "%s[total_amount]" % self.singular: self.amount,
            "%s[user_id]" % self.singular: user.dto.id,
            "%s[want_department_id]" % self.singular: user.dto.departments[0].department.id,
            "%s[contract_token]" % self.singular: user.session.csrf
        })
        if "approve_status" in self.kwargs:
            self.apply_body["%s[approve_status]" % self.singular] = self.kwargs["approve_status"]
        if "sign_date" in self.kwargs:
            self.apply_body["%s[sign_date]" % self.singular] = self.kwargs["sign_date"]
        if "start_at" in self.kwargs:
            self.apply_body["%s[start_at]" % self.singular] = self.kwargs["start_at"]
        if "end_at" in self.kwargs:
            self.apply_body["%s[end_at]" % self.singular] = self.kwargs["end_at"]

        return self.apply_body

    def setting(self, str_csrf, approve_flow):
        self.setting_body.update({"authenticity_token": str_csrf})
        for key, value in approve_flow.setting_body.items():
            self.setting_body["%s%s" % (self.singular, key)] = value
        return self.setting_body

    # 审批合同/商机/客户
    def approve(self, int_step, str_csrf):
        self.approve_body.update({"%s[step]" % self.singular: int_step, "authenticity_token": str_csrf})
        return self.approve_body

    # 跟进
    def revisit(self, str_csrf, **kwargs):
        action = "revisit_log"
        self.revisit_body.update({
            "lead_id": self.id,
            "authenticity_token": str_csrf,
            "%s[category]" % action: kwargs.setdefault("category", EnumCategory.电话).value,
            "%s[loggable_attributes][status]" % action: kwargs.setdefault("status", EnumStatus.初访).value,
            "%s[content]" % action: self.description,
            "%s[loggable_attributes][id]:" % action: self.id,
            "%s[real_revisit_at]" % action: self.time.format("YYYY-MM-DD HH:mm:ss"),
            "%s[remind_at]" % action: self.time.format("YYYY-MM-DD HH:mm:ss")
        })
        return self.revisit_body

    # 签到
    def checkin(self, **kwargs):
        self.checkin_body["checkin"].update({
            "checkable_type": self.singular.capitalize(),
            "checkable_id": self.id,
        })

        return self.checkin_body


class Contract(CRM):
    # 合同
    # 单数形式
    singular = "contract"
    # 复数形式
    plural = "contracts"


class Opportunity(CRM):
    # 单数形式
    singular = "opportunity"
    # 复数形式
    plural = "opportunities"


class Customer(CRM):
    # 单数形式
    singular = "customer"
    # 复数形式
    plural = "customers"

    def apply(self, str_csrf, user):
        # 每一次apply生成不同的title
        self.title = self.kwargs.get("title") or Random().return_sample(20)
        self.apply_body.update({
            "authenticity_token": str_csrf,
            "%s[name]" % self.singular: self.title,
            "%s[user_id]" % self.singular: user.dto.id,
            "%s[want_department_id]" % self.singular: user.dto.departments[0].department.id,
            "%s[customer_token]" % self.singular: user.session.csrf,
        })
        if "approve_status" in self.kwargs:
            self.apply_body["%s[approve_status]" % self.singular] = self.kwargs["approve_status"]

        return self.apply_body


class Lead(CRM):
    # 线索
    # 单数形式
    singular = "lead"
    # 复数形式
    plural = "leads"

    def apply(self, str_csrf, user):
        # 每一次apply生成不同的title
        self.title = self.kwargs.get("title") or Random().return_sample(20)
        self.apply_body.update({
            "authenticity_token": str_csrf,
            "%s[is_draft]" % self.singular: False,
            "%s[name]" % self.singular: self.title,
            "%slead[address_attributes][tel]" % self.singular: self.telephone,
            "china_tag_id": 4,
            "%s[address_attributes][country_id] % self.singular": 4,
            "%s[user_id]" % self.singular: user.dto.id,
            "%s[want_department_id]" % self.singular: user.dto.departments[0].department.id,
        })
        if "status" in self.kwargs:
            self.apply_body["%s[status]" % self.singular] = EnumStatus[self.kwargs["status"]].value

        return self.apply_body


class EnumBusiness(Enum):
    合同 = Contract
    商机 = Opportunity
    客户 = Customer
    线索 = Lead


class BusinessFactory:
    @classmethod
    def get_instance(cls, type, **kwargs):
        return type.value(type, **kwargs)


# ———————————————————审批业务对象———————————————————
class ApproveFlow:
    def __init__(self, kwargs, user_factory):
        self.kwargs = kwargs
        self.user_factory = user_factory
        self.str_result = self.kwargs.pop("result")
        # 运行的审批级数
        self.int_interrupt = self.kwargs.pop("interrupt")
        if "无权限" == self.str_result:
            self.int_interrupt = 1
        elif self.str_result not in ("通过", "驳回"):
            self.int_interrupt = len(self.kwargs)
        # 排序后的执行序列
        self.list_steps = sorted([(int(k[0]), EnumMultistep[v]) for k, v in self.kwargs.items()],
                                 key=lambda item: item[0])
        # 该数组将反复用到
        # setting_body通过该数组生成
        # approve每个步骤都要依赖list_settings进行比对
        # 所以用变量替代属性
        self.list_settings = [self.SettingStep(self, int_num, step) for int_num, step in self.list_steps]
        # self.list_settings已生成完毕，对list_approve_steps进行切片操作
        self.list_approve_steps = self.list_steps[:self.int_interrupt]
        # 驳回处理方案：
        # 1.ApproveFlow层，self.list_approve_steps最后一步*2，形成类似[步骤1，步骤2，步骤3.步骤3]的结构
        # 2.ApproveStep迭代时，第一次遇到步骤3，因为has_next == True，会按照通过方案执行
        # 3.第二次遇到步骤3，has_next==false，将会按照驳回/否决方案执行
        if "驳回" == self.str_result:
            self.list_approve_steps.append(self.list_approve_steps[-1])

        logging.info(self.__str__())

    @property
    def setting_body(self):
        return collections.ChainMap(*[step.body for step in self.list_settings])

    @property
    def business_finished(self):
        return ("驳回" == self.str_result and self.has_next <= 1) or not self.has_next

    @property
    def has_next(self):
        return len(self.list_approve_steps)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next:
            raise StopIteration()
        return self.ApproveStep(self, *self.list_approve_steps.pop(0))

    def __str__(self):
        return "设置审批级别：%s；实际审批级别：%s；最终审批结果：%s" % (len(self.list_settings), self.int_interrupt, self.str_result)

    class SettingStep:
        # 审批设置对象：提供设置审批级数的功能
        def __init__(self, flow, int_num, enum_step):
            self.flow = flow
            self.user_factory = self.flow.user_factory
            #  当前审批级数
            # x级审批，截取第一个字符，转换成数字
            self.int_num = int_num
            # 步骤类型
            # 如果测试超管，则设置成任意一人
            self.enum_step = EnumMultistep.任意一人 if EnumMultistep.超管 == enum_step else enum_step
            self.enum_step = EnumMultistep.负责人主管 if EnumMultistep.越级主管 == enum_step else enum_step

        @property
        def list_users(self):
            if self.enum_step in (EnumMultistep.负责人主管, EnumMultistep.上一级审批人主管):
                return tuple()
            else:
                return self.user_factory.find_authority_users("normal")

        @property
        def body(self):
            return {
                "_approve[multistep][%s][step]" % self.int_num: str(self.int_num),
                "_approve[multistep][%s][enable]" % self.int_num: "1",
                "_approve[multistep][%s][type]" % self.int_num: self.enum_step.value,
                "_approve[multistep][%s][user_ids][]" % self.int_num: [user.dto.id for user in self.list_users] if self.list_users else ""
            }

    class ApproveStep:
        def __init__(self, flow, int_num, enum_step):
            self.flow = flow
            self.int_num = int_num
            self.enum_step = enum_step
            self.str_result = self.flow.str_result
            self.setting = self.flow.list_settings[int_num - 1]
            self.user_factory = self.flow.user_factory
            # 将当前步骤user存入flow，供下一步骤作为before_user使用
            self._get_users()
            # 迭代时，list_users会被pop
            self.flow.step_user = self.list_users.copy()

        def _get_users(self):
            if EnumMultistep.负责人主管 == self.enum_step:
                self.list_users = self.user_factory.find_authority_user("applier").list_superiors
            elif EnumMultistep.上一级审批人主管 == self.enum_step:
                # 业务上，上一级审批人主管的前一步骤不允许会签，因此必定只有一人
                self.list_users = self.flow.step_user[0].list_superiors
            elif EnumMultistep.任意一人 == self.enum_step:
                # 随机选择一人，choices以数组形式返回
                self.list_users = random.choices(self.setting.list_users)
            elif EnumMultistep.多人会签 == self.enum_step:
                self.list_users = self.setting.list_users
            elif EnumMultistep.超管 == self.enum_step:
                self.list_users = self.user_factory.find_authority_users("super")[:1]
            elif EnumMultistep.越级主管 == self.enum_step:
                self.list_users = self.user_factory.find_authority_user("applier").list_superiors[0].list_superiors

            if "撤销" == self.str_result:
                self.list_users = self.user_factory.find_authority_users("applier")[:1]
            elif "无权限" == self.str_result:
                # 切片操作，取第一个元素，以数组形式返回
                self.list_users = self.user_factory.find_authority_users("illegal")[:1]
            elif "驳回" == self.str_result and not self.flow.has_next:
                # 随机抽取上一步骤的审批人，执行驳回操作
                self.list_users = random.choices(self.flow.step_user)
            elif "否决" == self.str_result and not self.flow.has_next:
                # 否决操作，从本步骤标准操作取一个用户
                self.list_users = random.choices(self.list_users)

        @property
        def has_next(self):
            # 该审批级别是否有下一个操作人
            return len(self.list_users)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.has_next:
                raise StopIteration()
            return self.UserStep(self, self.list_users.pop(0))

        class UserStep:
            # 实现功能：每一个User提交approve的具体参数
            # 对外暴露内容：步骤数/状态枚举
            def __init__(self, approve_step, user):
                self.approve_step = approve_step
                self.user = user
                # 会签是否完成
                self.int_num = self.approve_step.int_num

            @property
            def str_result(self):
                # 有下一级审批，则该级别审批设置为通过状态
                return "通过" if self.approve_step.flow.has_next else self.approve_step.str_result

            @property
            def str_expect(self):
                if "撤销" == self.str_result:
                    return "已撤销"
                elif "无权限" == self.str_result or self.approve_step.has_next:
                    # 未完成会签 或无权限
                    return "待%s级审批" % self.int_num
                elif not self.approve_step.has_next and self.str_result in ("否决", "驳回"):
                    return "已否决"
                elif self.approve_step.flow.business_finished:
                    # 当前处于最后一步，所有操作（驳回除外）已完成
                    return "已通过"
                else:
                    return "待%s级审批" % (self.int_num + 1)

            @property
            def str_notifications(self):
                if "驳回" == self.str_result:
                    return ["%s级审批人 %s 审批通过了你的" % (self.int_num, self.user.dto.name), "%s审批驳回了你的" % self.dto.name]
                else:
                    return ["%s级审批人 %s 审批%s了你的" % (self.int_num, self.user.dto.name, self.str_result)]

            def __str__(self):
                return "步骤编号：%s；操作人：%s；操作类型：%s" % (
                    self.int_num, self.user.__str__(), self.str_result)
