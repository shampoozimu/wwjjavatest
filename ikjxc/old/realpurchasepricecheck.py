# -*- coding: utf-8 -*-
__author__ = 'wl'
import order0405
from decimal import Decimal as D
import requests


class RealPurchasePriceCheck:
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


    def check_purchase_price(self, real_price, expect_price, print_content):
        if self.check_same(real_price, expect_price):
            print print_content+u" real_price is right."
        else:
            print print_content+u"real_price is wrong", real_price, expect_price
            f=open('price.txt','a')
            a = str(self.current_case) + ': '+ print_content+ "real_price is wrong " + str(real_price) + ' ' +  str( expect_price)
            f.write(a + '\n')
            f.close()

    def check_same(self, base_value1, base_value2):
        # print type(base_value1), type(base_value2)
        base = D(str(base_value1)) - D(str(base_value2))

        if abs(base) < D(0.01):
            return True
        else:
            return False

    def check_count(self, base_value1, base_value2):
        # print type(base_value1), type(base_value2)
        base = D(str(base_value1)) - D(str(base_value2))

        if abs(base) < D(0.01):
            return True
        else:
            return False

    def check_goods_count(self, real_goods_count, expect_goods_count, print_content):
        if self.check_count(real_goods_count, expect_goods_count):
            print print_content+u" real_goods_count is right."
        else:
            print print_content+u"real_goods_count is wrong", real_goods_count, expect_goods_count
            f=open('price.txt','a')
            a = str(self.current_case) + ': '+ print_content+ "real_goods_count " + str(real_goods_count) + ' ' +  str( expect_goods_count)
            f.write(a + '\n')
            f.close()

    def set_cookie(self, cookie):
        self.cookie_given = cookie

    def set_csrf(self, csrf):
        self.csrf = csrf

    def login(self, username='15600000000', password='111111'):
        if len(self.cookie) == 0:
            self.get_csrf_and_cookie()
        if len(self.cookie) == 0:
            print 'get csrf and cookie error'
            return
        self.username = username
        self.password = password
        url = self.base_url + "users/sign_in"
        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'user[login]': username,
            'user[password]': password,
            'user[remember_me]': 0,
            'commit': '登 录'
        }

        s = requests.session()
        s.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        s.headers.update({'Accept-Encoding': 'gzip, deflate'})
        s.headers.update({'Accept-Language': 'zh-CN,zh;q=0.8'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'Cookie': self.cookie})
        response = s.post(url=url, data=body)
        if response.status_code == 200:
            print 'login success'
            self.cookie = response.headers['set-cookie']
        else:
            print 'login error'

    def case_1(self):
        self.current_case = 'case 1'
        #a_real_price = order0405.OrderPurchase()
        #a_real_price.login()
        print self.warehouses_id_list[0]
        product_id= a_real_price.add_product()
        print product_id
        a_real_price.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        order_id = a_real_price.purchase_order_id
        print order_id
        a_real_price.get_purchase_orders_detail(order_id)
        a_real_price.verify_purchase_orders_first(order_id)
        a_real_price.verify_purchase_orders_sec(order_id)
        a_real_price.verify_purchase_orders_pass(order_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=3,price=10.0000)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
                #print item['quantity']
                warehouses_count = item['quantity']
        print product_info['inventories'][0]['inventory_in_warehouses']
        print product_info['counts']['all_warehouses_total_quantity']
        print product_info['counts']['total_cost_amount']
        print product_info['inventories'][0]['cost_price']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],30,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],3,'goods count')
        self.check_goods_count(warehouses_count,3,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_2(self):
        self.current_case = 'case 2'
        product_id= a_real_price.add_product()
        print product_id
        a_real_price.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =10.0000)
        order_id = a_real_price.purchase_order_id
        a_real_price.get_purchase_orders_detail(order_id)
        a_real_price.verify_purchase_orders_first(order_id)
        a_real_price.verify_purchase_orders_sec(order_id)
        a_real_price.verify_purchase_orders_pass(order_id)
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=3,price=10.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],30,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],3,'goods count')
        self.check_goods_count(warehouses_count,3,'warehouse%s goods count'% self.warehouses_id_list[0] )
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=2,price=5.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
            #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],8,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],40,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0] )
        a_real_price.purchase_order_in_cancel(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
            #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],30,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],3,'goods count')
        self.check_goods_count(warehouses_count,3,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_3(self):
        self.current_case = 'case 3'
        #a_real_price = order0405.OrderPurchase()
        #a_real_price.login()
        product_id= a_real_price.add_product()
        print product_id
        a_real_price.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =10.0000)
        order_id = a_real_price.purchase_order_id
        a_real_price.get_purchase_orders_detail(order_id)
        a_real_price.verify_purchase_orders_first(order_id)
        a_real_price.verify_purchase_orders_sec(order_id)
        a_real_price.verify_purchase_orders_pass(order_id)
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=3,price=10.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],30,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],3,'goods count')
        self.check_goods_count(warehouses_count,3,'warehouse%s goods count'% self.warehouses_id_list[0] )
        a_real_price.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=6,price =8.0000)
        order_id = a_real_price.purchase_order_id
        a_real_price.get_purchase_orders_detail(order_id)
        a_real_price.verify_purchase_orders_first(order_id)
        a_real_price.verify_purchase_orders_sec(order_id)
        a_real_price.verify_purchase_orders_pass(order_id)
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=6,price=8.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],8.67,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],78,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],9,'goods count')
        self.check_goods_count(warehouses_count,9,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_4(self):
        self.current_case = 'case 4'
        product_id= a_real_price.add_product()
        print product_id
        a_real_price.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =10.0000)
        order_id = a_real_price.purchase_order_id
        a_real_price.get_purchase_orders_detail(order_id)
        a_real_price.verify_purchase_orders_first(order_id)
        a_real_price.verify_purchase_orders_sec(order_id)
        a_real_price.verify_purchase_orders_pass(order_id)
        bill_id = a_real_price.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=5,price=10.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price1')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price1')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count1')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count1'% self.warehouses_id_list[0] )
        back_order = a_real_price.post_new_purchase_back_order(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=2,price =8.0000,purchase_back_order_id=bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count2')
        a_real_price.verify_purchase_orders_back_pass(back_order)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0] :
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],11.33,'real price3')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],34,'totle price3')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],3,'goods count3')
        self.check_goods_count(warehouses_count,3,'warehouse%s goods count3'% self.warehouses_id_list[0])
        a_real_price.purchase_order_back_cancel(purchase_order_back_id=back_order)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0])

    def case_5(self):
            self.current_case = 'case 5'
            product_id= a_real_price.add_product()
            print product_id
            storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=100,price =10.0000)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
            a_real_price.verify_other_orders_in_pass(storageio_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
            a_real_price.verify_other_orders_in_pass(storageio_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
            a_real_price.verify_other_orders_in_pass(storageio_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            for item in product_info['inventories'][0]['inventory_in_warehouses'] :
                if item['warehouse_id'] == self.warehouses_id_list[0]:
                    #print item['quantity']
                    warehouses_count = item['quantity']
            self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
            self.check_purchase_price(product_info['counts']['total_cost_amount'],1000,'totle price')
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],100,'goods count')
            self.check_goods_count(warehouses_count,100,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_6(self):
        self.current_case = 'case 6'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=100,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],100,'goods count')
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=20,price =3.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],100,'goods count')
        a_real_price.verify_other_orders_in_pass(storageio_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],8.83,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],1060,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],120,'goods count')
        self.check_goods_count(warehouses_count,120,'warehouse%s goods count'% self.warehouses_id_list[0] )
        a_real_price.other_order_cancel(storageio_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],1000,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],100,'goods count')
        self.check_goods_count(warehouses_count,100,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_7(self):
        self.current_case = 'case 7'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        profit_id = a_real_price.post_inventory_profit(product_id=product_id, warehouse_id=self.warehouses_id_list[0],add_amount=3)
        a_real_price.get_product_items_for_profit(profit_id)
        profit_in_id =a_real_price.post_profit_other_order_in(total_quantity=3,price =8.0000,profit_id=profit_id)
        a_real_price.verify_other_orders_in_fir(profit_in_id)
        a_real_price.verify_other_orders_in_sec(profit_in_id)
        a_real_price.verify_other_orders_in_pass(profit_in_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.53,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],124,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],13,'goods count')
        self.check_goods_count(warehouses_count,13,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_8(self):
        self.current_case = 'case 8'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        profit_id = a_real_price.post_inventory_profit(product_id=product_id, warehouse_id=self.warehouses_id_list[0],add_amount=10)
        a_real_price.get_product_items_for_profit(profit_id)
        profit_in_id =a_real_price.post_profit_other_order_in(total_quantity=3,price =8.0000,profit_id=profit_id)
        a_real_price.verify_other_orders_in_fir(profit_in_id)
        a_real_price.verify_other_orders_in_sec(profit_in_id)
        a_real_price.verify_other_orders_in_pass(profit_in_id)
        profit_in_id =a_real_price.post_profit_other_order_in(total_quantity=5,price =9.0000,profit_id=profit_id)
        a_real_price.verify_other_orders_in_fir(profit_in_id)
        a_real_price.verify_other_orders_in_sec(profit_in_id)
        a_real_price.verify_other_orders_in_pass(profit_in_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.38,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],169,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],18,'goods count')
        self.check_goods_count(warehouses_count,18,'warehouse%s goods count'% self.warehouses_id_list[0])
        a_real_price.other_order_cancel(profit_in_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.53,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],124,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],13,'goods count')
        self.check_goods_count(warehouses_count,13,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_9(self):
        self.current_case = 'case 9'
        product_id= a_real_price.add_product()
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[1],total_quantity=5,price =8.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        #storage_transfer_id =a_real_price.post_storage_transfers_order(total_quantity=3,from_warehouse_id=self.warehouses_id_list[0],to_warehouse_id=self.warehouses_id_list[1],product_id=product_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                warehouses_count = item['quantity']
            if item['warehouse_id'] == self.warehouses_id_list[1]:
                warehouses_count1 = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.33,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],140,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],15,'goods count')
        self.check_goods_count(warehouses_count,10,'warehouse%s goods count'% self.warehouses_id_list[0] )
        self.check_goods_count(warehouses_count1,5,'warehouse%s goods count'% self.warehouses_id_list[1] )
        #a_real_price.verify_storage_transfers_pass(storage_transfer_id)
        #product_info = a_real_price.get_product_price_warehouse_info(product_id)
        #for item in product_info['inventories'][0]['inventory_in_warehouses'] :
        #    if item['warehouse_id'] == self.warehouses_id_list[0]:
        #        warehouses_count = item['quantity']
        #    if item['warehouse_id'] == self.warehouses_id_list[1]:
        #        warehouses_count1 = item['quantity']
        #self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.33,'real price')
        #self.check_purchase_price(product_info['counts']['total_cost_amount'],140,'totle price')
        #self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],15,'goods count')
        #self.check_goods_count(warehouses_count,7,'warehouse%s goods count'% self.warehouses_id_list[0] )
        #self.check_goods_count(warehouses_count1,8,'warehouse%s goods count'% self.warehouses_id_list[1] )
        #storage_transfer_id =a_real_price.post_storage_transfers_order(total_quantity=3,from_warehouse_id=self.warehouses_id_list[0],to_warehouse_id=self.warehouses_id_list[1],product_id=product_id)
        #a_real_price.verify_storage_transfers_pass(storage_transfer_id)
        #product_info = a_real_price.get_product_price_warehouse_info(product_id)
        #for item in product_info['inventories'][0]['inventory_in_warehouses'] :
        #    if item['warehouse_id'] == self.warehouses_id_list[0]:
        #        warehouses_count = item['quantity']
        #    if item['warehouse_id'] == self.warehouses_id_list[1]:
        #        warehouses_count1 = item['quantity']
        #self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.33,'real price')
        #self.check_purchase_price(product_info['counts']['total_cost_amount'],140,'totle price')
        #self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],15,'goods count')
        #self.check_goods_count(warehouses_count,4,'warehouse%s goods count'% self.warehouses_id_list[0] )
        #self.check_goods_count(warehouses_count1,11,'warehouse%s goods count'% self.warehouses_id_list[1] )
        #a_real_price.storage_transfers_order_cancel(storage_transfer_id)
        #product_info = a_real_price.get_product_price_warehouse_info(product_id)
        #for item in product_info['inventories'][0]['inventory_in_warehouses'] :
        #    if item['warehouse_id'] == self.warehouses_id_list[0]:
        #        warehouses_count = item['quantity']
        #    if item['warehouse_id'] == self.warehouses_id_list[1]:
        #        warehouses_count1 = item['quantity']
        #self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.33,'real price')
        #self.check_purchase_price(product_info['counts']['total_cost_amount'],140,'totle price')
        #self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],15,'goods count')
        #self.check_goods_count(warehouses_count,7,'warehouse%s goods count'% self.warehouses_id_list[0] )
        #self.check_goods_count(warehouses_count1,8,'warehouse%s goods count'% self.warehouses_id_list[1] )

    def case_10(self):
        self.current_case = 'case 10'
        product_id= a_real_price.add_product()
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.post_new_sale_order(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_sale_orders_first(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_sec(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_pass(order_id=a_real_price.sale_id)
        a_real_price.make_new_sale_order_out(sale_order_id =a_real_price.sale_id,total_quantity=2,price=8.0000)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],10,'goods count')
        a_real_price.verify_sale_orders_out_pass(sale_order_out_id=a_real_price.sale_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses']:
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],80,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
        self.check_goods_count(warehouses_count,8,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_11(self):
        self.current_case = 'case 11'
        product_id= a_real_price.add_product()
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.post_new_sale_order(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =8.0000)
        a_real_price.verify_sale_orders_first(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_sec(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_pass(order_id=a_real_price.sale_id)
        a_real_price.make_new_sale_order_out(sale_order_id =a_real_price.sale_id,total_quantity=2,price=10.0000)
        a_real_price.verify_sale_orders_out_pass(sale_order_out_id=a_real_price.sale_out_id)
        a_real_price.make_new_sale_order_out(sale_order_id =a_real_price.sale_id,total_quantity=8,price=5.0000)
        a_real_price.verify_sale_orders_out_pass(sale_order_out_id=a_real_price.sale_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses']:
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price') #不确定为10还是0
        self.check_purchase_price(product_info['counts']['total_cost_amount'],0,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
        self.check_goods_count(warehouses_count,0,'warehouse%s goods count'% self.warehouses_id_list[0] )
        a_real_price.sale_order_out_cancel(sale_order_out_id=a_real_price.sale_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses']:
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price') #不确定为10还是0
        self.check_purchase_price(product_info['counts']['total_cost_amount'],80,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
        self.check_goods_count(warehouses_count,8,'warehouse%s goods count'% self.warehouses_id_list[0] )

    def case_12(self):
        self.current_case = 'case 12'
        product_id= a_real_price.add_product()
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.post_new_sale_order(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =8.0000)
        a_real_price.verify_sale_orders_first(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_sec(order_id=a_real_price.sale_id)
        a_real_price.verify_sale_orders_pass(order_id=a_real_price.sale_id)
        a_real_price.make_new_sale_order_out(sale_order_id =a_real_price.sale_id,total_quantity=5,price=8.0000)
        a_real_price.verify_sale_orders_out_pass(sale_order_out_id=a_real_price.sale_out_id)
        sale_back_order = a_real_price.post_new_purchase_sale_order_back( warehouse_id=self.warehouses_id_list[0],total_quantity=4,price =9.0000,sale_out_order_id=a_real_price.sale_out_id)
        a_real_price.get_sale_orders_back_detail(sale_back_order)
        a_real_price.verify_sale_orders_back_fir(sale_back_order)
        a_real_price.verify_sale_orders_back_sec(sale_back_order)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_purchase_price(product_info['counts']['all_warehouses_total_quantity'],5,'goods count1')
        a_real_price.verify_sale_orders_back_thi(sale_back_order)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses']:
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price2')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],90,'totle price2')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],9,'goods count2')
        self.check_goods_count(warehouses_count,9,'warehouse%s goods count2'% self.warehouses_id_list[0] )
        a_real_price.sale_order_out_cancel(sale_order_out_id=sale_back_order)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0])
        
    def case_13(self):
        self.current_case = 'case 13'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        losses_id = a_real_price.post_inventory_losses(product_id=product_id, warehouse_id=self.warehouses_id_list[0],reduce_amount=-5)
        losses_out_id = a_real_price.post_lose_other_order_out(total_quantity=5,price =1000.0000,lose_id =losses_id )
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],10,'goods count1')
        a_real_price.verify_other_orders_in_pass(losses_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price1')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price1')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count1')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count3'% self.warehouses_id_list[0] )

    def case_14(self):
        self.current_case = 'case 14'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        losses_id = a_real_price.post_inventory_losses(product_id=product_id, warehouse_id=self.warehouses_id_list[0],reduce_amount=-5)
        losses_out_id = a_real_price.post_lose_other_order_out(total_quantity=2,price =1000.0000,lose_id =losses_id )
        a_real_price.verify_other_orders_in_pass(losses_out_id)
        losses_out_id = a_real_price.post_lose_other_order_out(total_quantity=2,price =1000.0000,lose_id =losses_id )
        a_real_price.verify_other_orders_in_pass(losses_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],60,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],6,'goods count')
        self.check_goods_count(warehouses_count,6,'warehouse%s goods count'% self.warehouses_id_list[0])
        a_real_price.other_order_cancel(losses_out_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price1')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],80,'totle price1')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count1')
        self.check_goods_count(warehouses_count,8,'warehouse%s goods count3'% self.warehouses_id_list[0] )

    def case_15(self):
        self.current_case = 'case 15'
        product_id= a_real_price.add_product()
        print product_id
        bill_id = a_real_price.post_new_purchase_order_in(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =10.0000)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],0,'goods count')
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0])
        bill_id = a_real_price.post_new_purchase_order_in(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=3,price =8.0000)
        a_real_price.audit_purchasee_m(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],9.25,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],74,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
        self.check_goods_count(warehouses_count,8,'warehouse%s goods count'% self.warehouses_id_list[0])
        a_real_price.purchase_order_in_cancel(purchase_order_in_id=bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
        self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0])

    def case_16(self):
        self.current_case = 'case 16'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        bill_id =a_real_price.post_new_sale_order_out(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=3,price =8.0000)
        a_real_price.verify_sale_orders_out_pass(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],70,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],7,'goods count')
        self.check_goods_count(warehouses_count,7,'warehouse%s goods count'% self.warehouses_id_list[0])
        a_real_price.sale_order_out_cancel(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],100,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],10,'goods count')
        self.check_goods_count(warehouses_count,10,'warehouse%s goods count'% self.warehouses_id_list[0])

    def case_17(self):
        self.current_case = 'case 17'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=5,price =5.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        bill_id =a_real_price.post_purchase_back_order_not_association(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=3,price =10.0000)
        a_real_price.verify_purchase_orders_back_pass(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],7.91,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],95,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],12,'goods count')
        self.check_goods_count(warehouses_count,12,'warehouse%s goods count'% self.warehouses_id_list[0])

    def case_18(self):
        self.current_case = 'case 18'
        product_id= a_real_price.add_product()
        print product_id
        storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        a_real_price.verify_other_orders_in_pass(storageio_id)
        bill_id =a_real_price.post_new_sale_order_out_not_association(product_id=product_id, warehouse_id=self.warehouses_id_list[0],total_quantity=3,price =8.0000)
        a_real_price.verify_sale_orders_out_pass(bill_id)
        a_real_price.verify_sale_orders_out_pass(bill_id)
        a_real_price.verify_sale_orders_out_pass(bill_id)
        product_info = a_real_price.get_product_price_warehouse_info(product_id)
        for item in product_info['inventories'][0]['inventory_in_warehouses'] :
            if item['warehouse_id'] == self.warehouses_id_list[0]:
                #print item['quantity']
                warehouses_count = item['quantity']
        self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
        self.check_purchase_price(product_info['counts']['total_cost_amount'],130,'totle price')
        self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],13,'goods count')
        self.check_goods_count(warehouses_count,13,'warehouse%s goods count'% self.warehouses_id_list[0])
    #其他出库单2次后，第二次作废
    def case_19(self):
            self.current_case = 'case 19'
            product_id= a_real_price.add_product()
            print product_id
            storageio_id = a_real_price.post_other_order_in(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=10,price =10.0000)
            a_real_price.verify_other_orders_in_pass(storageio_id)
            a_real_price.verify_other_orders_in_pass(storageio_id)
            a_real_price.verify_other_orders_in_pass(storageio_id)
            storageio_out_id = a_real_price.post_other_order_out(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=2,price =8.0000)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],10,'goods count')
            a_real_price.verify_other_orders_in_pass(storageio_out_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            for item in product_info['inventories'][0]['inventory_in_warehouses'] :
                if item['warehouse_id'] == self.warehouses_id_list[0]:
                    #print item['quantity']
                    warehouses_count = item['quantity']
            self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
            self.check_purchase_price(product_info['counts']['total_cost_amount'],80,'totle price')
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
            self.check_goods_count(warehouses_count,8,'warehouse%s goods count'% self.warehouses_id_list[0] )
            storageio_out_id = a_real_price.post_other_order_out(product_id=product_id,warehouse_id=self.warehouses_id_list[0],total_quantity=3,price =5.0000)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
            a_real_price.verify_other_orders_in_pass(storageio_out_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            for item in product_info['inventories'][0]['inventory_in_warehouses'] :
                if item['warehouse_id'] == self.warehouses_id_list[0]:
                    #print item['quantity']
                    warehouses_count = item['quantity']
            self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
            self.check_purchase_price(product_info['counts']['total_cost_amount'],50,'totle price')
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],5,'goods count')
            self.check_goods_count(warehouses_count,5,'warehouse%s goods count'% self.warehouses_id_list[0] )
            a_real_price.other_order_cancel(storageio_out_id)
            product_info = a_real_price.get_product_price_warehouse_info(product_id)
            for item in product_info['inventories'][0]['inventory_in_warehouses'] :
                if item['warehouse_id'] == self.warehouses_id_list[0]:
                    #print item['quantity']
                    warehouses_count = item['quantity']
            self.check_purchase_price(product_info['inventories'][0]['cost_price'],10,'real price')
            self.check_purchase_price(product_info['counts']['total_cost_amount'],80,'totle price')
            self.check_goods_count(product_info['counts']['all_warehouses_total_quantity'],8,'goods count')
            self.check_goods_count(warehouses_count,8,'warehouse%s goods count'% self.warehouses_id_list[0] )


    def _ok(self):
        self.check_goods_count(1,3,'warehouse%s goods count'% 1 )


if __name__ == '__main__':
    a_real_price = order0405.OrderPurchase()
    a_opeation = RealPurchasePriceCheck(warehouses_id_list=[3907,3903])
    a_real_price.csrf = 'cOC8grWptak98VaueUg5Ob01ix71Km9G940k3mbWIEXTw3H3de5dnZmqqwqvB581AmIg4LoQkttsIf8tNB1lMA=='
    a_real_price.cookie = '_invoicing_session=RFQ0M2dTMm9YbmtZVEdiQlZ6MFpHNzRpcDdJK3R0RFBpaVp1NXlkcVFjWklFMUh3OC9xWjhiV242R3NHMVptN3R5Mzg5Zkg0RUtzajNxZWU4VVZZMm50TFhiZk5FNUN6dmVaOUQycU9vRS9Pc21nRlB4TXAzM2FWaS80TFNkUzJaYnpuWlZVVjNLQUN4eko3TXc3NWhtVThUM1NGeGd4eEJ4MzNGSDJXYjkrbHNjLzhsZnBoZGRNK29hWnRxcTRJUDRuS2dwWjFIMEhvMWxTWXpyeW0zRWs4cFZWMCtzekdhemtDUkViMEY5M3ZOZmFxUVpIeDhpSE11WC8xbDkzL3FhS0Z4Sk8wUnVXY0ZQNTVrWkp2SXlpZFM1Yi9ZQXNvY2lNUWtMVGVUYU9PamVkdUlHSVFPR2xmY04xUEhkenEtLVlJQW9taVM5djZrVmM3Z1NMKzh6Z3c9PQ%3D%3D--514b2a1f66c8a925a08ca46b1f71d1a1b0035c83; path=/; HttpOnly'
    a_real_price.set_cookie(a_real_price.cookie)
    a_real_price.set_csrf(a_real_price.csrf)
    a_opeation.case_1() #单个采购单单次入库
    a_opeation.case_2() #单个采购单多次入库，第二次作废
    a_opeation.case_3() #多个采购单多次入库
    a_opeation.case_4() #单个采购单入库后退货退货成功再作废
    a_opeation.case_5() #其他入库单单次入库
    a_opeation.case_6() #其他入库单多次入库，第二次作废
    a_opeation.case_7() #盘盈单单次入库
    a_opeation.case_8() #盘盈单多次入库，第二次作废
    a_opeation.case_9() #库存调拨单2次后，第二次作废
    a_opeation.case_10() #销售出库
    a_opeation.case_11() #销售出库多次,第二次作废
    a_opeation.case_12() #销售出库后退货成功后再作废
    a_opeation.case_13() #盘亏单单次出库
    a_opeation.case_14() #盘亏单多次出库，第二次作废
    a_opeation.case_15()  #直接生成采购入库单2次再作废
    a_opeation.case_16()  #直接生成销售出库单再作废
    a_opeation.case_17()  #直接生成采购退货单
    a_opeation.case_18()  #直接生成销售退货单
    a_opeation.case_19() #其他出库单2次后，第二次作废





    # 缺（没有关联采购入库单的）采购退货 （没有关联销售出库）销售退货  单据作废
