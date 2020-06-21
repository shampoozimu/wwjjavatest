# -*- coding: utf-8 -*-
__author__ = 'wl'
import order0405
from decimal import Decimal as D
import requests

class FundsManagementCheck:
    def __init__(self, warehouses_id_list=[3907,3903]):
        self.purchase_order_id = 0
        self.purchase_id = 0
        self.username = '15600000000'
        self.password = '111111'
        self.purchase_order = {}
        self.warehouses = []
        self.suppliers = []
        self.products = []
        self.members = []
        self.purchase = {}
        self.warehouses_id_list =warehouses_id_list

    def check_price(self, real_price, expect_price, print_content):
        if self.check_same(real_price, expect_price):
            print print_content+u" real_price is right."
        else:
            print print_content+u"real_price is wrong", real_price, expect_price
            f=open('funds.txt','a')
            a = str(self.current_case) + ': '+ print_content+ "funds is wrong " + str(real_price) + ' ' +  str( expect_price)
            f.write(a + '\n')
            f.close()

    def check_same(self, base_value1, base_value2):
        # print type(base_value1), type(base_value2)
        base = D(str(base_value1)) - D(str(base_value2))
        if abs(base) < D(0.01):
            return True
        else:
            return False

    def case_1(self,total_quantity,price,pay_funds,fund_account_amount):
        self.current_case = 'case 1'
        print self.warehouses_id_list[0]
        product_id= a_funds_manage.add_product()
        print product_id
        a_funds_manage.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =20.0000)
        order_id = a_funds_manage.purchase_order_id
        print order_id
        a_funds_manage.audit_purchase_order(order_id)
        bill_id = a_funds_manage.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=total_quantity,price=price)
        a_funds_manage.audit_purchasee_m(bill_id)
        a_funds_manage.audit_purchase(bill_id)
        pay_id =a_funds_manage.get_funds_payment()
        result_list = a_funds_manage.get_funds_payment_list(bill_id)  #total_amount =result_list[0] ,exist_amount = result_list[1],unpaid_amount=result_list[2]
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')  #
        self.check_price(result_list[1], 0.00, 'exist_amount')
        self.check_price(result_list[2], total_quantity*price*1.1733, 'unpaid_amount')
        paymentflow_id = a_funds_manage.funds_payments(payments_ids=pay_id,pay_funds=pay_funds,fund_account_amount = fund_account_amount)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], pay_funds, 'exist_amount')
        self.check_price(result_list[2], total_quantity*price*1.1733-pay_funds, 'unpaid_amount')
        a_funds_manage.funds_payments_delete(paymentflow_id=paymentflow_id)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], 0.00, 'exist_amount')
        self.check_price(result_list[2], total_quantity*price*1.1733, 'unpaid_amount')
        paymentflow_id = a_funds_manage.funds_payments(payments_ids=pay_id,pay_funds=pay_funds,fund_account_amount = fund_account_amount)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], total_quantity*price*1.1733, 'exist_amount')
        self.check_price(result_list[2], 0.00, 'unpaid_amount')
        a_funds_manage.withdraw_force_close(pay_id)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], total_quantity*price*1.1733, 'exist_amount')
        self.check_price(result_list[2], 0.00, 'unpaid_amount')
        a_funds_manage.force_close(pay_id)

    def case_2(self,total_quantity,price,pay_funds,fund_account_amount):
        self.current_case = 'case 2'
        print self.warehouses_id_list[0]
        product_id= a_funds_manage.add_product()
        print product_id
        a_funds_manage.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =20.0000)
        order_id = a_funds_manage.purchase_order_id
        print order_id
        a_funds_manage.audit_purchase_order(order_id)
        a_funds_manage.get_purchase_orders_detail(order_id)
        a_funds_manage.verify_purchase_orders_first(order_id)
        a_funds_manage.verify_purchase_orders_sec(order_id)
        a_funds_manage.verify_purchase_orders_pass(order_id)
        bill_id = a_funds_manage.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=total_quantity,price=price)
        a_funds_manage.audit_purchasee_m(bill_id)
        a_funds_manage.audit_purchase(bill_id)
        pay_id =a_funds_manage.get_funds_payment()
        result_list = a_funds_manage.get_funds_payment_list(bill_id)  #total_amount =result_list[0] ,exist_amount = result_list[1],unpaid_amount=result_list[2]
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')  #
        self.check_price(result_list[1], 0.00, 'exist_amount')
        self.check_price(result_list[2], total_quantity*price*1.1733, 'unpaid_amount')
        paymentflow_id = a_funds_manage.funds_payments(payments_ids=pay_id,pay_funds=pay_funds,fund_account_amount = fund_account_amount)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], pay_funds, 'exist_amount')
        self.check_price(result_list[2], total_quantity*price*1.1733-pay_funds, 'unpaid_amount')

        paymentflow_id = a_funds_manage.funds_payments(payments_ids=pay_id,pay_funds=pay_funds,fund_account_amount = fund_account_amount)
        result_list = a_funds_manage.get_funds_payment_list(bill_id)
        print result_list
        self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        self.check_price(result_list[1], total_quantity*price*1.1733, 'exist_amount')
        self.check_price(result_list[2], 0.00, 'unpaid_amount')
        #a_funds_manage.withdraw_force_close(pay_id)
        #result_list = a_funds_manage.get_funds_payment_list(bill_id)
        #print result_list
        #self.check_price(result_list[0], total_quantity*price*1.1733, 'total_amount')
        #self.check_price(result_list[1], total_quantity*price*1.1733, 'exist_amount')
        #self.check_price(result_list[2], 0.00, 'unpaid_amount')
        #a_funds_manage.force_close(pay_id)







if __name__ == '__main__':
    a_funds_manage = order0405.OrderPurchase()
    a_opeation = FundsManagementCheck(warehouses_id_list=[3907,3903])
    a_funds_manage.csrf = 'cOC8grWptak98VaueUg5Ob01ix71Km9G940k3mbWIEXTw3H3de5dnZmqqwqvB581AmIg4LoQkttsIf8tNB1lMA=='
    a_funds_manage.cookie = '_invoicing_session=RFQ0M2dTMm9YbmtZVEdiQlZ6MFpHNzRpcDdJK3R0RFBpaVp1NXlkcVFjWklFMUh3OC9xWjhiV242R3NHMVptN3R5Mzg5Zkg0RUtzajNxZWU4VVZZMm50TFhiZk5FNUN6dmVaOUQycU9vRS9Pc21nRlB4TXAzM2FWaS80TFNkUzJaYnpuWlZVVjNLQUN4eko3TXc3NWhtVThUM1NGeGd4eEJ4MzNGSDJXYjkrbHNjLzhsZnBoZGRNK29hWnRxcTRJUDRuS2dwWjFIMEhvMWxTWXpyeW0zRWs4cFZWMCtzekdhemtDUkViMEY5M3ZOZmFxUVpIeDhpSE11WC8xbDkzL3FhS0Z4Sk8wUnVXY0ZQNTVrWkp2SXlpZFM1Yi9ZQXNvY2lNUWtMVGVUYU9PamVkdUlHSVFPR2xmY04xUEhkenEtLVlJQW9taVM5djZrVmM3Z1NMKzh6Z3c9PQ%3D%3D--514b2a1f66c8a925a08ca46b1f71d1a1b0035c83; path=/; HttpOnly'
    a_funds_manage.set_cookie(a_funds_manage.cookie)
    a_funds_manage.set_csrf(a_funds_manage.csrf)
    a_opeation.case_1(total_quantity =10,price =10,pay_funds=117.3300,fund_account_amount=117.3300 ) #付款成功后删除流水，再付款成功，反结案，再结案.
    a_opeation.case_2(total_quantity =10,price =10,pay_funds=117.3300/2,fund_account_amount=117.3300/2 ) #付款一半后，再付款一半。
    #a_opeation.case_1(total_quantity =10,price =10,pay_funds=293.3250,fund_account_amount=293.3250 )
    #a_opeation.case_2(total_quantity =10,price =10,pay_funds=117.3300,fund_account_amount=117.3300 )
