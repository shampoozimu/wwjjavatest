from enum import Enum

from testCase.component.utils import Random


class CRM:
    def __init__(self, enum_type, **kwargs):
        # 非必填项
        self.enum_type = enum_type
        self.kwargs = kwargs
        # 名称
        self.title = self.kwargs.get("title") or Random().return_sample(20)
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

        self.setting_body = {
            "utf8": "✓",
            "_method": "put",
            "%s_approve[editable][enable]" % self.singular: "1",
            "%s_approve[editable][policy]" % self.singular: "can",
        }

    def apply(self, user):
        self.apply_body.update({
            "%s[title]" % self.singular: self.title,
            "%s[total_amount]" % self.singular: self.amount,
            "%s[user_id]" % self.singular: user.id,
            "%s[want_department_id]" % self.singular: user.department,
            "%s[contract_token]" % self.singular: user.session.csrf,
            "%s[customer_id]" % self.singular: user.factory.server.approval.customer.id
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

    def setting(self, str_csrf, list_settings):
        self.setting_body.update({"authenticity_token": str_csrf})

        for setting in list_settings:
            dict_setting_body = setting.get_body()
            for key, value in dict_setting_body.items():
                self.setting_body["%s_approve[multistep][%s][%s]" % (self.singular, dict_setting_body["step"], key)] = value
        return self.setting_body

    def approve(self, int_step, str_csrf):
        self.approve_body.update({"%s[step]" % self.singular: int_step, "authenticity_token": str_csrf})
        return self.approve_body


class Contract(CRM):
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

    def apply(self, user):
        self.apply_body.update({
            "%s[name]" % self.singular: self.title,
            "%s[user_id]" % self.singular: user.id,
            "%s[want_department_id]" % self.singular: user.department,
            "%s[contract_token]" % self.singular: user.session.csrf,
        })
        if "approve_status" in self.kwargs:
            self.apply_body["%s[approve_status]" % self.singular] = self.kwargs["approve_status"]

        return self.apply_body


class EnumBusiness(Enum):
    合同 = Contract
    商机 = Opportunity
    客户 = Customer


class BusinessFactory:
    @classmethod
    def get_instance(cls, type, **kwargs):
        return type.value(type, **kwargs)
