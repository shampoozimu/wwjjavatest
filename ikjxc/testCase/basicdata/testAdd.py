# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'
from commons import common
from commons.const import const
from testCase.basicdata import testGetinfo


class Basic:
    def __init__(self,uid,token):
        self.uid =uid
        self.common = common.Common(uid,token)
        self.testGetinfo = testGetinfo.Getinfo(uid, token)
        self.base_url = const.BASE_URL

        pass

    #新增产品
    def add_product(self,WarehousesId=314,default_quantity=0,default_cost=3,default_unit_cost =3):
        url = self.base_url + 'api/products.json'
        product_number ='auto%s' % self.common.get_random_int(9999)
        body = {
            'product[org_id]': '5500180',
            'product[number]': product_number,
            'product[name]': 'flowers%s' % self.common.get_random_int(9999),
            'product[product_category_id]': '943',
            'product[spec]': '',
            'product[note]': 'wl-test-auto-%s' % self.common.get_random_int(9999),
            'product[barcode]': self.common.get_random_int(99999999999),
            'product[unit_id]': '2963',
            'product[unit_name]': '瓶',
            'product[standard_price]': '1',
            'product[default_unit_id]': '2963',
            'product[default_in_unit_id]': '2963',
            'product[current_warning_policy]': 'no_warning',
            'product[split_warning_status]': 'split_closed',
            'product[total_warning_status]': 'total_closed',
            'product[attr_warning_status]': 'attr_warning_closed',
            'product[attr_status]': 'attr_closed',
            'product[price_policy_setting]': 'unit_policy',
            'product[unit_setting]': 'single_unit',
            'product[batch_status]': 'batch_closed',
            'product[serial_code_status]': 'serial_closed',
            'product[life_warning_days]':'',
            'product[life_period]':'',
            'product[use_purchase_attribute]': 'false',
            'product[use_sale_attribute]': 'false',
            'product[use_customer_setting]': 'false',
            'product[use_customer_price]': 'false',
            'product[product_units][0][unit_id]': '2963',
            'product[product_units][0][unit_name]': '瓶',
            'product[product_customer_types][0][name]': '一级代理商',
            'product[product_customer_types][0][customer_type_id]': '3430',
            'product[product_customer_types][0][default_percentage]': '100.0',
            'product[product_customer_types][1][name]': '二级代理商',
            'product[product_customer_types][1][customer_type_id]': '3431',
            'product[product_customer_types][1][default_percentage]': '100.0',
            'product[product_customer_types][2][name]': '普通客户',
            'product[product_customer_types][2][customer_type_id]': '3432',
            'product[product_customer_types][2][default_percentage]': '100.0',
            'product[product_customer_types][3][name]': '大客户',
            'product[product_customer_types][3][customer_type_id]': '3433',
            'product[product_customer_types][3][default_percentage]': '100.0',
            'product[product_customer_types][4][name]': '批发客户',
            'product[product_customer_types][4][customer_type_id]': '3434',
            'product[product_customer_types][4][default_percentage]': '100.0',
            'product[product_units_attributes][0][unit_id]': '296',
            'product[product_units_attributes][0][unit_name]': '瓶',
            'product[product_customer_types_attributes][0][name]': '一级代理商',
            'product[product_customer_types_attributes][0][customer_type_id]': '3430',
            'product[product_customer_types_attributes][0][default_percentage]': '100.0',
            'product[product_customer_types_attributes][1][name]': '二级代理商',
            'product[product_customer_types_attributes][1][customer_type_id]': '3431',
            'product[product_customer_types_attributes][1][default_percentage]': 100.0,
            'product[product_customer_types_attributes][2][name]': '普通客户',
            'product[product_customer_types_attributes][2][customer_type_id]': 3432,
            'product[product_customer_types_attributes][2][default_percentage]': 100.0,
            'product[product_customer_types_attributes][3][name]': '大客户',
            'product[product_customer_types_attributes][3][customer_type_id]': 3433,
            'product[product_customer_types_attributes][3][default_percentage]': 100.0,
            'product[product_customer_types_attributes][4][name]': '批发客户',
            'product[product_customer_types_attributes][4][customer_type_id]': 3434,
            'product[product_customer_types_attributes][4][default_percentage]': 100.0,
            'product[product_attr_groups_attributes][0][org_id]': 5500180,
            'product[product_attr_groups_attributes][0][category]':'default_attr',
            'product[product_attr_groups_attributes][0][product_attr_names]':'',
            'product[product_attr_groups_attributes][0][product_attr_ids]':'',
            'product[product_attr_groups_attributes][0][number]':'',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][warehouse_id]': 314,
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][warehouse_name]':warehouses_info["name"] ,
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_id]':'',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_product_attr_ids]':'',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_product_attr_names]':'',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_quantity]': '2',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_cost]': '4.00',
            # 'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_unit_cost]': '2',
        }
        if default_quantity is not 0:
            print (1234)
            warehouses_info = self.testGetinfo.get_warehouses_info(WarehousesId)
            w ={  'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][warehouse_id]': WarehousesId,
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][warehouse_name]':warehouses_info["name"] ,
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_id]':'',
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_product_attr_ids]':'',
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][product_attr_group_product_attr_names]':'',
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_quantity]': default_quantity,
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_cost]': default_cost,
                'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_unit_cost]': default_unit_cost,}
            body =dict( body, **w )
        response = self.common.post_response_json(url, body, 'add product')
        return(response.json()['product']['id'],product_number)



