# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'

from commons import common
from commons.const import const
from testCase.login import testLogin as login
from testCase.basicdata import testAdd as testAdd
from testCase.basicdata import testGetinfo
from testCase.purchase import testAddpurchase_orders
from testCase.purchase import testapproved
from testCase.reportCenter import Report_get_info
from testCase.sale import testAddsales as testAddsales


class ProductReport:
    def __init__(self,uid,token):
        self.uid = uid
        self.token = token
        self.testAdd = testAdd.Basic(uid,token)
        self.testGetinfo =testGetinfo.Getinfo(uid,token)
        self.testAddpurchase =testAddpurchase_orders.Testadd_purchase(uid,token)
        self.testApprove =testapproved.Test_Approved(uid,token)
        self.Report_get_info = Report_get_info.Repoer_get_info(uid,token)
        self.testAddsales = testAddsales.Sale(uid,token)
        self.porduct_id =''
        # self.porduct_number ='wl-test-auto-1347'
        pass

    def case_1(self):
        porduct_id =self.testAdd.add_product()
        # self.porduct_id=porduct_id[0]
        # self.porduct_number=porduct_id[1]
        # print(self.porduct_id)
        id =self.testAddsales.sale_return_product(ProduceId=porduct_id[0],total_quantity=2.00,discount=55.00,price = 300.00,warehouse_id =315)
        self.testApprove.purchase_verify(purchase_order_id=id, module='sales')
        # #4136wangle仓库id
        # purchase_order_id =self.testAddpurchase.post_new_purchase_order_new_produce(product_id=self.porduct_id, warehouse_id=4136, total_quantity=3, price=10.0000)
        # print(purchase_order_id)
        # self.testApprove.purchase_verify(purchase_order_id=purchase_order_id,module='purchase_orders')
        # purchases_in_id =self.testAddpurchase.make_new_purchase(purchase_order_id=purchase_order_id,total_quantity=3, price=10)
        # print(purchases_in_id)
        # self.testApprove.purchase_verify(purchase_order_id=purchases_in_id,module='purchases')
        # self.Report_get_info.Product_invernory_flow(self.porduct_number)










