# -*- coding: utf-8 -*-
__author__ = 'le Wang'

from commons import common
from commons.const import const
from testCase.basicdata import testGetinfo


class Repoer_get_info:
    def __init__(self,uid,token):
        self.uid =uid
        self.token =token
        self.common = common.Common(uid,token)
        self.base_url = const.BASE_URL
        pass

    def Product_invernory_flow(self,product_number ):
        print(product_number)
        url="https://dingtalkjxc-test.ikcrm.com/api/reports/query_inventories.json?page=1&per=15&warehouse_id%5B%5D=all&product_category_id=all&product_id=all&inventory_quantity=all&disabled_product=hide&keyword=%s&keyword_type=products.number" % product_number
        # url="https://dingtalkjxc-test.ikcrm.com/api/reports/query_summaries.json?page=1&per=15&date=&warehouse_id=all&product_category_id=&product_id=128696&settlements=-1"
        print(url)
        body ={
        }
        response=self.common.get_response_json(url,body,"get product inventory flow")
        print(response)
