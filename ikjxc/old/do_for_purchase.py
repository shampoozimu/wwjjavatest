# -*- coding: utf-8 -*-
__author__ = 'lwang'


class DoForPurchase:
    def __init__(self):
        self.purchase_order_id = 0
        self.purchase_id = 0
        self.username = '15600000000'
        self.password = '111111'
        self.user = Ikjxc()
        self.user.login(self.username, self.password)
        self.purchase_order = {}
        self.warehouses = []
        self.suppliers = []
        self.products = []
        self.members = []
        self.purchase = {}

    def get_today_str(self):
        today = datetime.datetime.now()
        return today.strftime('%Y-%m-%d')

    def get_random_int(self, max_num):
        tmp = random.randint(0, max_num)
        if tmp < max_num:
            return tmp
        else:
            return tmp - 1

    def prepare_for_purchase(self):
        if len(self.warehouses) == 0:
            self.warehouses = self.user.get_warehouses()
        if len(self.suppliers) == 0:
            self.suppliers = self.user.get_suppliers_for_purchase()
        if len(self.products) == 0:
            self.products = self.user.get_product_attr_groups()
        if len(self.members) == 0:
            self.members = self.user.get_members()

    def make_new_purchase_order(self, supplier_id='', product_id='', warehouse_id=''):
        # 如果不指定供应商，商品及仓库，才使用随机组合
        self.prepare_for_purchase()
        self.purchase_order = self.user.get_purchase_new()['purchase_order']
        self.purchase_order.pop('deleted_at')
        self.purchase_order.pop('order_id')
        self.purchase_order.pop('approved_level')
        self.purchase_order.pop('created_at')
        self.purchase_order.pop('updated_at')
        self.purchase_order.pop('creator_id')
        self.purchase_order['documented_at'] = self.get_today_str()
        self.purchase_order['delivered_at'] = self.get_today_str()
        self.purchase_order['status'] = 'approving'

        # 设置供应商及联系人信息
        if len(supplier_id) == 0:
            random_index = self.get_random_int(len(self.suppliers))
            self.purchase_order['supplier_id'] = self.suppliers[random_index]['id']
        else:
            self.purchase_order['supplier_id'] = supplier_id
        supplier = self.user.get_supplier_detail(self.purchase_order['supplier_id'])
        self.purchase_order['supplier_address'] = supplier['address']
        self.purchase_order['purchase_member_id'] = supplier['member_id']

        if len(supplier['contacts']) == 0:
            contact = self.members[0]
        else:
            contact = supplier['contacts'][0]
        self.purchase_order['contact_id'] = contact['id']
        self.purchase_order['contact_name'] = contact['name']
        self.purchase_order['contact_mobile'] = contact['mobile']
        if 'telephone' in contact:
            self.purchase_order['contact_phone'] = contact['telephone']
        else:
            self.purchase_order['contact_phone'] = ''
        if 'address' in contact:
            self.purchase_order['contact_address'] = contact['address']
        else:
            self.purchase_order['contact_address'] = ''

        # 设置仓库
        if len(warehouse_id) == 0:
            tmp_warehouse = self.warehouses[self.get_random_int(len(self.warehouses))]
            self.purchase_order['warehouse_id'] = tmp_warehouse['id']
        else:
            self.purchase_order['warehouse_id'] = warehouse_id

        #设置商品
        if len(product_id) == 0:
            tmp_product = self.products[self.get_random_int(len(self.products))]
            self.purchase_order['order_items_attributes[0][product_attr_group_id]'] = tmp_product['id']
            self.purchase_order['order_items_attributes[0][product_number]'] = tmp_product['product_number']
            self.purchase_order['order_items_attributes[0][product_unit_id]'] = tmp_product['product_unit_id']
            self.purchase_order['order_items_attributes[0][attr_names]'] = tmp_product['product_attr_names']
            self.purchase_order['order_items_attributes[0][product_id]'] = tmp_product['product_id']
            self.purchase_order['order_items_attributes[0][modified]'] = 'quantity'
            self.purchase_order['order_items_attributes[0][name]'] = tmp_product['product_name']
            self.purchase_order['order_items_attributes[0][spec]'] = tmp_product['product_spec']
            self.purchase_order['order_items_attributes[0][unit]'] = tmp_product['product_unit_name']
            self.purchase_order['order_items_attributes[0][quantity]'] = 1.0
            self.purchase_order['order_items_attributes[0][price]'] = tmp_product['price_policy']['purchase_price']
            self.purchase_order['order_items_attributes[0][price_with_tax]'] = float(tmp_product['price_policy']['purchase_price']) * (1 + 0.1733)
            self.purchase_order['order_items_attributes[0][discount]'] = 0
            self.purchase_order['order_items_attributes[0][batch_number]'] = ''
            self.purchase_order['order_items_attributes[0][produced_at]'] = ''
            self.purchase_order['order_items_attributes[0][expired_at]'] = ''
            self.purchase_order['order_items_attributes[0][deduction]'] = 0
            self.purchase_order['order_items_attributes[0][amount]'] = tmp_product['price_policy']['purchase_price']
            self.purchase_order['order_items_attributes[0][tax_rate]'] = 17.33
            self.purchase_order['order_items_attributes[0][tax_amount]'] = float(tmp_product['price_policy']['purchase_price']) * 0.1733
            self.purchase_order['order_items_attributes[0][amount_with_tax]'] = float(tmp_product['price_policy']['purchase_price']) * (1 + 0.1733)
            self.purchase_order['order_items_attributes[0][note]'] = 0

        self.purchase_order['total_amount'] = self.purchase_order['order_items_attributes[0][amount]']
        self.purchase_order['discount'] = 0.0
        self.purchase_order['deduction'] = 0.0
        self.purchase_order['amount'] = self.purchase_order['order_items_attributes[0][amount_with_tax]']
        self.purchase_order['total_tax_amount'] = self.purchase_order['order_items_attributes[0][tax_amount]']
        self.purchase_order['total_amount_with_tax'] = self.purchase_order['order_items_attributes[0][amount_with_tax]']
        self.purchase_order['total_deduction'] = 0.0

        self.purchase_order['total_quantity'] = 1
        self.purchase_order['note'] = ''
        self.purchase_order['id'] = ''

        for k, v in self.purchase_order.iteritems():
            if v is None:
                self.purchase_order[k] = ''
        print u'purchase.order%s' % self.purchase_order
        purchase_reponse = self.user.post_new_purchase_order(self.purchase_order)
        print purchase_reponse
        if purchase_reponse['status']['code'] == '200':
            self.purchase_order = purchase_reponse['purchase_order']
            print self.purchase_order['id']

    def audit_purchase_order(self, id=''):
        if len(str(id)) == 0:
            purchase_order_id = self.purchase_order['id']
        else:
            purchase_order_id = id
        for i in range(3):
                self.user.audit_purchase_orders(purchase_order_id)

    def make_new_purchase(self, purchase_order_id=''):
        if len(str(purchase_order_id)) == 0:
            purchase_order_id = self.purchase_order['id']
        purchase = self.user.get_purchases_new(purchase_order_id)['purchase']
        product_info = self.user.get_product_items_for_purchase(purchase_order_id)

        for k, v in purchase.iteritems():
            if v is None:
                purchase[k] = ''

        purchase.pop('updated_at')

        purchase['status'] = 'approving'
        purchase['purchase_member_id'] = product_info['purchase_member']['id']
        purchase['supplier_id'] = product_info['supplier']['id']
        purchase['warehouse_id'] = product_info['warehouse']['id']
        purchase['entry_at'] = self.get_today_str()
        purchase['total_quantity'] = 1.0

        key_list = ['id', 'product_attr_group_id', 'order_item_id', 'product_id', 'name', 'product_number',
                    'attr_names', 'spec', 'unit', 'quantity', 'price', 'discount', 'deduction', 'amount',
                    'price_with_tax', 'tax_rate', 'tax_amount', 'amount_with_tax', 'note', 'batch_number',
                    'product_unit_id', 'produced_at', 'expired_at', 'modified']
        for key in key_list:
            new_key = 'product_items_attributes[0][%s]' % key
            if product_info['product_items'][0][key] is None:
                purchase[new_key] = ''
            else:
                purchase[new_key] = product_info['product_items'][0][key]

        purchase['total_amount_with_tax'] = product_info['product_items'][0]['amount_with_tax']
        purchase['total_deduction'] = 0.0
        purchase['total_amount'] = product_info['product_items'][0]['amount']
        purchase['discount'] = 0.0
        purchase['deduction'] = 0.0
        purchase['payment_amount'] = product_info['product_items'][0]['amount_with_tax']
        purchase['total_tax_amount'] = product_info['product_items'][0]['tax_amount']


        print purchase
        response = self.user.post_new_purchase(purchase)
        if response['status']['code'] == '200':
            self.purchase = response['purchase']
            self.purchase_id = self.purchase['id']
            print self.purchase_id

    def audit_purchase(self, id=''):
        if len(str(id)) == 0:
            purchase_id = self.purchase_id
        else:
            purchase_id = id
        for i in range(3):
                self.user.audit_purchases(purchase_id)

    def make_new_purchase_order_wl(self, supplier_id='', product_id='', warehouse_id='',):
        self.purchase_order['total_amount'] = self.purchase_order['order_items_attributes[0][amount]']
        self.purchase_order['discount'] = 0.0
        self.purchase_order['deduction'] = 0.0
        self.purchase_order['amount'] = self.purchase_order['order_items_attributes[0][amount_with_tax]']
        self.purchase_order['total_tax_amount'] = self.purchase_order['order_items_attributes[0][tax_amount]']
        self.purchase_order['total_amount_with_tax'] = self.purchase_order['order_items_attributes[0][amount_with_tax]']
        self.purchase_order['total_deduction'] = 0.0

        self.purchase_order['total_quantity'] = 1
        self.purchase_order['note'] = ''
        self.purchase_order['id'] = ''

        for k, v in self.purchase_order.iteritems():
            if v is None:
                self.purchase_order[k] = ''
        print u'purchase.order%s' % self.purchase_order
        purchase_reponse = self.user.post_new_purchase_order(self.purchase_order)
        print purchase_reponse
        if purchase_reponse['status']['code'] == '200':
            self.purchase_order = purchase_reponse['purchase_order']
            print self.purchase_order['id']


if __name__ == '__main__':
    a_purchase = DoForPurchase()
    for i in range(1):
        a_purchase.make_new_purchase_order(supplier_id='5509', product_id='', warehouse_id='3907')
        a_purchase.audit_purchase_order()
        a_purchase.make_new_purchase()
        a_purchase.audit_purchase()
