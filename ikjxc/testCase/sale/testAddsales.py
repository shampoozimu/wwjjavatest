# -*- coding: utf-8 -*-
__author__ = 'le Wang'
from commons import common
from commons.const import const
from testCase.basicdata import testGetinfo


class Sale:
    def __init__(self,uid,token):
        self.uid =uid
        self.common = common.Common(uid,token)
        self.testGetinfo = testGetinfo.Getinfo(uid, token)
        self.base_url = const.BASE_URL

        pass

    #新增销售退货单
    def sale_return_product(self,ProduceId=314,total_quantity=2.00,discount=55,price = 300,warehouse_id =314):
        url = self.base_url + 'api/sales.json'
        product_info = self.testGetinfo.get_product_info(ProduceId)
        print(product_info)
        body = {
            'customer_id': 6799,
            'seller_id': 1000013611,
            'parent_id':'',
            'contact_id': 4166,
            'category': 'in',
            'number': 'auto%s' % self.common.get_random_int(9999),
            'io_at': '2019-03-29',
            'discount': '0.00',
            'deduction': '0.00',
            'amount': price*total_quantity*(100-discount)/100,
            'contact_name': '张海艳',
            'contact_mobile': '13681876857',
            'contact_phone':'',
            'contact_address':'',
            'customer_address': '星创科技广场',
            'total_quantity': total_quantity,
            'total_base_quantity':'',
            'total_deduction': price*total_quantity*discount/100,
            'total_amount': price*total_quantity*(100-discount)/100,
            'total_tax_amount': 0.00,
            'total_amount_with_tax': price*total_quantity*(100-discount)/100,
            'status': 'approving',
            'product_items_attributes[0][product_attr_group_id]': product_info["product"]["product_attr_groups_attributes"][0]['id'],
            'product_items_attributes[0][product_id]': product_info["product"]["id"],
            'product_items_attributes[0][warehouse_id]': warehouse_id,
            'product_items_attributes[0][product_unit_id]': product_info['product']['product_unit_id'],
            'product_items_attributes[0][name]': product_info['product']['name'],
            'product_items_attributes[0][product_number]': product_info['product']['number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]': product_info['product']['spec'],
            'product_items_attributes[0][unit]': product_info['product']['unit'],
            'product_items_attributes[0][quantity]':total_quantity ,
            'product_items_attributes[0][base_unit]':'',
            'product_items_attributes[0][base_quantity]':'',
            'product_items_attributes[0][deputy_unit_quantity]':'',
            'product_items_attributes[0][price]': price,
            'product_items_attributes[0][price_with_tax]': price,
            'product_items_attributes[0][discount]': discount,
            'product_items_attributes[0][deduction]': price*total_quantity*discount/100,
            'product_items_attributes[0][amount]': price*total_quantity*(100-discount)/100,
            'product_items_attributes[0][tax_rate]': 0.00,
            'product_items_attributes[0][tax_amount]': 0.00,
            'product_items_attributes[0][amount_with_tax]': price*total_quantity*(100-discount)/100,
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][note]':product_info['product']['note'],
            'product_items_attributes[0][modified]': 'discount',
            'express_order_attributes[company_name]':'',
            'express_order_attributes[tracking_number]':''
        }
        print(body)
        response = self.common.post_response_json(url, body, 'add sale return product')
        print(response.json())
        return(response.json()['sale']['id'])



