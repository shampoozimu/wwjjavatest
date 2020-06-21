# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'

from commons import common
from commons.const import const

class Approvals:
    def __init__(self, cookie, csrf):
        self.common = common.Common(cookie, csrf)
        self.base_url = const.BASE_URL
        self.csrf = csrf
        self.cookie = cookie
        pass

    # #开启审批
    # #approve_type 表示审批类型：客户/合同/商机/回款/费用报销（customer_approve/contract_approve/opportunity_approve）
    def open_approval(self,approve_module='customer_approve',approve_parameter='enable_customer_approve'):
        url = self.base_url + 'settings/'+ approve_module +'/update'
        params = {
            str(approve_module):{
                 str(approve_parameter): '1'
            }
        }
        self.common.put_response_json(url, params, '开启审批')
    #
    # # 关闭审批
    def close_approval(self,approve_module='customer_approve',approve_parameter='enable_customer_approve'):
        url = self.base_url + 'settings/'+ approve_module +'/update'
        params = {
            str(approve_module):{
                 str(approve_parameter): '0'
            }
        }
        self.common.put_response_json(url, params, '关闭审批')
    #
    #
    # # 审批客户/商机/合同
    # #date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def approve_verify(self, date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/' + str(date_id) + '/approve'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'key': approve_type,
            str(approve_type): {
                'step': '1',
                'approve_description': '审批通过',
                'notify_user_ids[]': '',
            }
        }
        self.common.post_response_json(url, body, '审批通过')
    #
    #
    # #客户/商机/合同 撤销审批
    # # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def cancel_approval(self,date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/'+ str(date_id) + '/revert?key='+ approve_type
        body = {
            'utf8':'✓',
            'authenticity_token': self.csrf,
            '_method':'put',
            'key':approve_type,
            str(approve_type): {
                'approve_description': '撤销审批',
            }
        }
        self.common.post_response_json(url, body, '撤销审批')
    #
    #
    # #客户/商机/合同 审批否决
    # # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def deny_approval(self,date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/'+ str(date_id) + '/deny'
        body = {
            'utf8':'✓',
            'authenticity_token': self.csrf,
            '_method':'put',
            'key':approve_type,
            str(approve_type):{
                    'step':'1',
                    'approve_description':'审批否决',
                    'notify_user_ids[]':''
            }
        }
        self.common.post_response_json(url, body, '审批否决')
    #
    # # 审批时编辑通知他人
    # # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    # def update_notify_user(self,date_id,approve_type='customer'):
    #     url = self.base_url + 'api/approvals/' + str(date_id) + '/update_notify_users'
    #     body = {
    #         'utf8': '✓',
    #         '_method': 'put',
    #         'authenticity_token': self.csrf,
    #         'key': approve_type,
    #         str(approve_type): {
    #             'notify_user_ids[]': self.user.getUserId(),
    #         }
    #     }
    #     self.common.post_response_json(url, body, '审批通过时通知他人')

