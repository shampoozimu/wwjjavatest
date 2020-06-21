from datetime import datetime
from enum import Enum, unique, IntEnum

from testCase.component.utils import Random


@unique
class EnumCategory(IntEnum):
    默认分类 = 942


@unique
class EnumUnit(Enum):
    瓶 = {"name": "瓶", "id": 2963}
    打 = {"id": 2965, "name": "打", "conversion": "12"}
    箱 = {"id": 2966, "name": "箱", "conversion": "48"}
    多单位 = {"single_units": "瓶", "id": 2964, "children": ["打", "箱"]}


class ProductUnit:
    def __init__(self, name):
        self.dict_unit = EnumUnit[name].value
        self.id = self.dict_unit["id"]
        if self.dict_unit.get("single_units"):
            self.__multi()
        else:
            self.__single()

    def __single(self):
        self.name = self.dict_unit["name"]
        self.conversion = self.dict_unit.get("conversion") or 1

    def __multi(self):
        self.single_units = ProductUnit(self.dict_unit["single_units"])
        self.name = self.single_units.name
        self.children = [ProductUnit(child) for child in self.dict_unit["children"]]

    # def get(self, str_business):
    #     return {
    #
    #     }


class Info:
    def __init__(self, enum_type, **kwargs):
        # 非必填项
        self.enum_type = enum_type
        self.kwargs = kwargs
        # 获取响应后补充项
        self.id = 0
        self.default_product_attr_group = 0
        # 名称
        self.title = self.kwargs.get("title") or Random().return_sample(20)
        self.amount = self.kwargs.get("amount") or 999
        self.description = Random().return_sample(99)
        self.apply_body = {}

        def set_response(self, dic_response):
            self.id = dic_response["id"]
            self.default_product_attr_group = dic_response["default_product_attr_group"]

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


class Product(Info):
    # 单数形式
    singular = "product"
    # 复数形式
    plural = "products"
    # 产品编号
    org_id = 5500180
    # 规格编号
    category_id = EnumCategory.默认分类.value
    # 单位编号
    unit_id = 2964


class Sale:
    def __init__(self, **kwargs):
        # 非必填项
        self.kwargs = kwargs
        self.enum_type = EnumSale[kwargs["类型"]]

        # 订单流水号
        self.number = self.kwargs.setdefault("编号", Random().return_sample(17))
        self.description = Random().return_sample(99)

        self._product = self._product_class(name=self.kwargs["产品名称"], price=self.kwargs["单价"], quantity=self.kwargs["数量"])
        self._product.warehouse = EnumWarehouse[self.kwargs["仓库"]]

        # 其他费用总和，默认0
        self.total_fee_amount = 0
        # 折扣前总金额=含税价格+其他费用
        self._total_amount = self._product.amount_with_tax + self.total_fee_amount
        # 折扣率，默认0
        self.discount = 0
        # 折扣金额=折扣前总金额*折扣率%
        self.deduction = self._total_amount * self.discount / 100
        # 应付金额=折扣前总金额-折扣金额
        self.amount = self._total_amount - self.deduction

        self.apply_body = {
            # 订单编号
            "number": self.number,
            "customer_id": EnumCustomer[self.kwargs["客户"]].value,
            "seller_id": EnumSeller[self.kwargs["销售员"]].value,
            # 合同编号：貌似是固定值
            "contact_id:": 4166,
            "status": "approving",
            "total_quantity": self._product.quantity,
            "total_base_quantity": self._product.quantity,
            "total_deduction": self._product.deduction,
            "total_tax_amount": self._product.tax_amount,
            "total_amount": self._product.amount,
            "total_amount_with_tax": self._product.amount_with_tax,
            "discount": self.discount,
            "deduction": self.deduction,
            "amount": self.amount,
            # 默认项
            "contact_name": "张海艳",
            "contact_mobile": "13681876857",
            "contact_phone": "",
            "contact_address": "",
            "customer_address": "星创科技广场",
        }

        self.apply_body.update(self._product.get())

        self.approve_body = {
            "approved_level": 1,
            "reason": self.description,
            # 默认项
            "resume_executing": False,
            "allow_negative_inventory": False,
            "gt_order_quantity": False
        }

    def approve(self, enum_status):
        self.approve_body.update({
            "status": enum_status.value,
        })
        return self.approve_body

    class Product:
        items_prefix = "product_items_attributes[0][%s]"

        def __init__(self, name, price, quantity, **kwargs):
            # 从参数导入枚举和字典
            # self.dict_product = {k: "" for k in ["parent_id", "spec", "batch_number", "produced_at", "expired_at", "note", "company_name", "tracking_number"]}
            self.dict_product=EnumProduct[name].value
            self.dict_product.update(kwargs)
            self.price = price
            self.quantity = quantity
            # 用字典装填属性，计算金额
            [self.__setattr__(k, v) for k, v in self.dict_product.items()]
            self.price_with_tax = self.price
            # 未折扣总价
            self.__total = self.price_with_tax * self.quantity
            # 折扣金额
            self.deduction = self.__total * self.discount / 100
            self.amount = self.__total - self.deduction
            self.amount_with_tax = self.amount
            self.warehouse = EnumWarehouse.上海仓
            # 计算完成后，重新装填原始字典
            self.dict_product["price"] = self.price
            self.dict_product["quantity"] = self.quantity
            self.dict_product["price_with_tax"] = self.price_with_tax
            self.dict_product["amount"] = self.amount
            self.dict_product["amount_with_tax"] = self.amount_with_tax
            self.dict_product["warehouse_id"] = self.warehouse.value

        def get(self):
            return {self.items_prefix % k: v for k, v in self.dict_product.items()}



    class Order(Product):
        items_perfix = "order_items_attributes[0][%s]"


class Outbound(Sale):
    # 单数形式
    # singular = "sale"
    # 复数形式
    plural = "sales"

    def __init__(self, **kwargs):
        self._product_class = self.Product
        super().__init__(**kwargs)

    def apply(self, user):
        self.apply_body.update({
            # 出入库标志
            "category": "out",
            "io_at": self.kwargs["日期"],
            # 上传附件
            "document_addition_attributes[copy_to][]": 1000013612,
            "total_fee_amount": self.total_fee_amount,

            "express_order_attributes[company_name]": "",
            "express_order_attributes[tracking_number]": "",
        })

        return self.apply_body


class ReturnForm(Sale):
    # 单数形式
    # singular = "sale"
    # 复数形式
    plural = "sales"

    def __init__(self, **kwargs):
        self._product_class = self.Product
        super().__init__(**kwargs)

    def apply(self, user):
        self.apply_body.update({
            # 出入库标志
            "category": "in",
            "io_at": self.kwargs["日期"],
            "total_fee_amount": self.total_fee_amount,
            "express_order_attributes[company_name]": "",
            "express_order_attributes[tracking_number]": "",
        })
        return self.apply_body


class Order(Sale):
    # 单数形式
    # singular = "sale"
    # 复数形式
    plural = "sale_orders"
    coefficient = 0

    def __init__(self, **kwargs):
        self._product_class = self.Order
        super().__init__(**kwargs)

    def apply(self, user):
        self.apply_body.update({
            # 订单日期
            "documented_at": self.kwargs["documented_at"],
            # 发货日期
            "delivered_at": self.kwargs["delivered_at"],
        })

        return self.apply_body


@unique
class EnumSale(Enum):
    出库单 = Outbound
    退货单 = ReturnForm
    销售订单 = Order


@unique
class EnumBusiness(Enum):
    # 基础资料
    产品 = Product
    # 销售管理
    销售管理 = EnumSale


@unique
class EnumCustomer(IntEnum):
    张海艳 = 6799


@unique
class EnumSeller(IntEnum):
    张海艳 = 1000013611
    施亮赜 = 1000013625
    王乐 = 1000013612


@unique
class EnumWarehouse(IntEnum):
    上海仓 = 314
    江苏仓 = 315


@unique
class EnumProduct(Enum):
    报表测试专用产品001 = {"product_attr_group_id": 6078, "product_id": 3999, "product_unit_id": 5111, "name": "报表测试专用产品001", "product_number": "BBCS001", "attr_names": "屎黄色", "unit": "瓶", "discount": 0,
                   "tax_rate": 0, "tax_amount": 0, "modified": "quantity", "position": 0}


@unique
class EnumStatus(Enum):
    通过 = "approving"
    驳回 = "rejected"


class BusinessFactory:
    @classmethod
    def get_instance(cls, business_type, **kwargs):
        return business_type.value(**kwargs)


class SaleManagerStatistic:
    # 把provider对象转换成数组
    def __init__(self, kwargs, data_frame):
        self.data_frame = data_frame
        self.kwargs = kwargs
        [self.__setattr__(k, v) for k, v in self.kwargs.items()]
        self.日期 = datetime.strptime(self.日期, "%Y-%m-%d")
        self.product = Sale.Product({"name": self.产品名称, "price": self.单价, "quantity": self.数量})
        # 系数
        self.coefficient = 1 if "出库单" == self.类型 else -1

    def get_data_frame(self):
        pass

    def get_provider(self):
        return {
            "日期": self.日期,
            "出库单": self.类型 == "出库单",
            "退货单": self.类型 == "退货单",
            "产品名称": self.产品名称,
            "出库数量": (self.coefficient == 1) * self.product.quantity,
            "退货数量": (self.coefficient == -1) * self.product.quantity,
            # 带正负号进入统计
            "数量合计": self.coefficient * self.product.quantity,
            "出库金额": (self.coefficient == 1) * self.product.amount,
            "退货金额": (self.coefficient == -1) * self.product.amount,
            "金额合计": self.coefficient * self.product.amount,
            "客户": self.客户,
            "销售员": self.销售员,
            "仓库": self.仓库
        }
