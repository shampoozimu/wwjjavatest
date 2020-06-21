# -*- coding: utf-8 -*-
__author__ = 'le Wang'

from commons import common
from commons.const import const
from testCase.basicdata import testGetinfo


class Test_Approved:
    def __init__(self,uid,token):
        self.uid =uid
        self.token =token
        self.common = common.Common(uid,token)
        self.base_url = const.BASE_URL

        pass

    def purchase_verify(self, purchase_order_id=128553, module='purchase_orders'):
        #module=purchase_orders 采购单审批；module=purchases 入库单审批；
        url = self.base_url + 'api/%s/%s.json' % (module,purchase_order_id)
        body = {
            'status': 'approving',
            'approved_level': '1',
            'reason': '审批通过',
            'resume_executing': 'false',
            'allow_negative_inventory': 'false',
            'gt_order_quantity': 'false',
        }
        success = self.common.put_response_json(url, body, 'verify purchase order')
        # print(success.json())
        # return success.json()['purchase_order']['id']
