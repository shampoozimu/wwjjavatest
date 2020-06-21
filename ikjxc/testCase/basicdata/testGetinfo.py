# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'
from commons import common
from commons.const import const

class Getinfo:
    def __init__(self, uid, token):
        self.common = common.Common(uid, token)
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.token = token
        self.uid = uid
        pass

    def get_product_info(self, product_id):
        url = self.base_url + 'api/products/%s' % product_id
        print(url)
        body={}
        product_info = self.common.get_response_json(url, body,'get product %s info ' % product_id)

        return product_info

    def get_product_items_for_purchase(self, purchase_order_id):
        url = self.base_url + '/api/purchase_orders/%s.json' % purchase_order_id
        # print(url)
        body ={}
        success = self.common.get_response_json(url, body,'get product items for purhcase order %s' % purchase_order_id)
        # print((success['purchase_order']))
        return(success['purchase_order'])

    def get_warehouses_info(self,WarehousesId):
        url = self.base_url + '/api/warehouses'
        # print(url)
        body = {}
        success = self.common.get_response_json(url, body, 'get WarehousesId info' )
        for warehouses in success['warehouses']:
            if warehouses['id'] == WarehousesId:
                print(warehouses)
        # print((success['purchase_order']))
        return warehouses
