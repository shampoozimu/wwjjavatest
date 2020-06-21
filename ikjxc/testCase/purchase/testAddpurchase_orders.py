# -*- coding: utf-8 -*-
__author__ = 'le Wang'

from commons import common
from commons.const import const
from testCase.basicdata import testGetinfo


class Testadd_purchase:
    def __init__(self,uid,token):
        self.uid =uid
        self.common = common.Common(uid,token)
        self.base_url = const.BASE_URL
        self.testGetinfo = testGetinfo.Getinfo(uid, token)
        pass

    def post_new_purchase_order_new_produce(self, product_id=128553, warehouse_id=4024, total_quantity=3.00, price=10.0000):
        product_info = self.testGetinfo.get_product_info(product_id)
        print(product_info)
        print(product_info['product']['product_attrables_attributes'])
        url = self.base_url + 'api/purchase_orders.json'
        body = {
            'purchaser_id': '13356',
            'supplier_id': '54',
            'parent_id':'',
            'contact_id': '25442',
            # 'warehouse_id': warehouse_id,
            'number': 'test-%s' % self.common.get_random_int(9999),
            'documented_at': self.common.get_today_str(),
            'delivered_at': self.common.get_today_str(),
            'discount': '0.00',
            'deduction': '0.0000',
            'contact_name': '小张三',
            'amount': price * total_quantity * 1.16,
            'contact_mobile': '18516548889',
            'contact_phone': '',
            'supplier_address': 'sadadadasd',
            'total_quantity': total_quantity,
            'total_base_quantity': '',
            'total_deduction': '0.0000',
            'total_amount': price * total_quantity,
            'total_tax_amount': price * 0.16 * total_quantity,
            'total_amount_with_tax': price * total_quantity * 1.16,
            'select_field_852becb357':'1325',
             'status': 'approving',
             'document_approvers_params[0][level]': '1',
            'document_approvers_params[0][member_ids][]': '204757',
            'order_items_attributes[0][warehouse_id]': warehouse_id,
            'order_items_attributes[0][product_attr_group_id]':
                product_info['product']['product_attrables_attributes'][0]['id'],
            'order_items_attributes[0][product_number]': product_info['product']['number'],
            'order_items_attributes[0][product_unit_id]': product_info['product']['product_unit_id'],
            'order_items_attributes[0][attr_names]': '',
            'order_items_attributes[0][product_id]': product_id,
            'order_items_attributes[0][modified]': 'price',
            'order_items_attributes[0][name]': product_info['product']['name'],
            'order_items_attributes[0][spec]': '',  # product_info['product']['name'],
            'order_items_attributes[0][unit]': product_info['product']['unit_name'],
            'order_items_attributes[0][quantity]': total_quantity,
            'order_items_attributes[0][price]': price,
            'order_items_attributes[0][price_with_tax]': price * 1.16,
            'order_items_attributes[0][discount]': '0.00',
            'order_items_attributes[0][batch_number]': '',
            'order_items_attributes[0][produced_at]': '',
            'order_items_attributes[0][expired_at]': '',
            'order_items_attributes[0][deduction]': '0.0000',
            'order_items_attributes[0][amount]': price * total_quantity,
            'order_items_attributes[0][tax_rate]': '16.00',
            'order_items_attributes[0][tax_amount]': price * total_quantity * 0.16,
            'order_items_attributes[0][amount_with_tax]': price * total_quantity * 1.16,
            'order_items_attributes[0][note]': ''
        }
        success = self.common.post_response_json(url, body, 'post new purchase order')
        print(success.json())
        return success.json()['purchase_order']['id']

    def make_new_purchase(self, purchase_order_id, total_quantity, price):
        url = self.base_url + 'api/purchases.json'
        product_info = self.testGetinfo.get_product_items_for_purchase(purchase_order_id)
        body = {
            'supplier_id': product_info['supplier_id'],
            'purchaser_id': product_info['purchaser_id'],
            'purchase_order_id': purchase_order_id,
            'parent_id': '',
            'contact_id': product_info['contact_id'],
            'status': 'approving',
            'category': 'in',
            'number': product_info['number'],
            'io_at': self.common.get_today_str(),
            'discount': '0.00',
            'deduction': '0.0000',
            'amount':total_quantity * price*1.16,
            'note': '',
            'contact_name':  product_info['contact_name'],
            'contact_mobile':  product_info['contact_mobile'],
            'contact_phone': product_info['contact_phone'],
            'contact_address': product_info['contact_address'],
            'supplier_address': product_info['supplier_address'],
            'total_quantity': total_quantity,
            'total_base_quantity': '',
            'total_deduction': '0.0000',
            'total_amount': total_quantity * price,
            'total_tax_amount': round(total_quantity * price * 0.16, 6),
            'total_amount_with_tax': total_quantity * price * 1.16,
            'total_fee_amount': '0.0',
            'text_field_1dfb5df7b9':'',
            'select_field_24af1d35cc': '',
            'product_items_attributes[0][warehouse_id]': product_info['order_items'][0]['warehouse_id'],
            'product_items_attributes[0][id]': '',
            'product_items_attributes[0][product_attr_group_id]': product_info['order_items'][0]['product_attr_group_id'],
            'product_items_attributes[0][order_item_id]': product_info['order_items'][0]['id'],
            'product_items_attributes[0][product_id]': product_info['order_items'][0]['product_id'],
            'product_items_attributes[0][name]': product_info['order_items'][0]['name'],
            'product_items_attributes[0][product_number]': product_info['order_items'][0]['product_number'],
            'product_items_attributes[0][attr_names]': '',
            'product_items_attributes[0][spec]': '',
            'product_items_attributes[0][unit]': product_info['order_items'][0]['unit'],
            'product_items_attributes[0][quantity]': total_quantity,
            'product_items_attributes[0][price]': price,
            'product_items_attributes[0][discount]': '0.00',
            'product_items_attributes[0][deduction]': '0.0000',
            'product_items_attributes[0][amount]': price * total_quantity,
            'product_items_attributes[0][price_with_tax]': round(price * 1.16, 6),
            'product_items_attributes[0][tax_rate]': '16.00',
            'product_items_attributes[0][tax_amount]': round(price * total_quantity * 0.16, 6),
            'product_items_attributes[0][amount_with_tax]': price * total_quantity * 1.16,
            'product_items_attributes[0][note]': '',
            'product_items_attributes[0][batch_number]': '',
            'product_items_attributes[0][product_unit_id]': product_info['order_items'][0]['product_unit_id'],
            'product_items_attributes[0][produced_at]': '',
            'product_items_attributes[0][expired_at]': '',
            'product_items_attributes[0][modified]': product_info['order_items'][0]['modified']
        }
        success = self.common.post_response_json(url, body, 'post new purchase order')
        return(success.json()['purchase']['id'])
