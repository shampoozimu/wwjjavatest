# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import requests
import random
import datetime
import re
from decimal import Decimal as D
from commons import common
from commons.const import const
from testCase.users.testGetUser import GetUser
from testCase.opportunities.testAddOpportunity import AddOpportunities
# from testCase.opportunities.testSettingsOpportunityApproval import Approvals


class ApprovalSettings:
    def __init__(self, cookie, csrf):
        self.common = common.Common(cookie, csrf)
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = csrf
        self.cookie = cookie
        self.response = ''
        self.user = GetUser(cookie, csrf)
        self.add = AddOpportunities(cookie, csrf)
        # self.approval = Approvals(cookie, csrf)
        pass

    def testAdd(self):
        opportunity_id = self.add.add_applying_opportunitie()
        self.approve_opportunitie(opportunity_id)
        self.cancel_opportunities_approval(opportunity_id)
        self.deny_opportunities_approval(opportunity_id)

    # 获取随机的审批人列表
    def get_random_user_ids(self):
        user_ids = self.user.getUserId()
        end = self.common.get_random_int(len(user_ids))
        b = []
        for i in range(end):
            start = self.common.get_random_int(end)
            b.append(user_ids[start])
            b = list(set(b))
        return b

    # 获取随机的审批设置
    def get_approval_setting(self):
        approval_role = ['superior', 'specified', 'specified_jointly', 'previous_superior']
        num = self.common.get_random_int(len(approval_role))
        return approval_role[num]

    #开启审批
    #approve_type 表示审批类型：客户/合同/商机/回款/费用报销（customer_approve/contract_approve/opportunity_approve）
    def open_approval(self,approve_module='customer_approve',approve_parameter='enable_customer_approve'):
        url = self.base_url + 'settings/'+ approve_module +'/update'
        params = {
            # str(approve_module):{
            #      str(approve_parameter): '1'
            'customer_approve[enable_customer_approve]': '1'
            }

        self.common.put_response_json(url, params, '开启审批')


    # 关闭审批
    def close_approval(self,approve_module='customer_approve',approve_parameter='enable_customer_approve'):
        url = self.base_url + 'settings/'+ approve_module +'/update'
        params = {
                     'customer_approve[enable_customer_approve]': '0'

            }
        # 'customer_approve[enable_customer_approve]': '0',
        self.common.put_response_json(url, params, '关闭审批')


    # 审批客户/商机/合同
    #date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def approve_verify(self, date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/' + str(date_id) + '/approve'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'key': approve_type,
            'customer[step]': '1',
            'customer[approve_description]':'审批通过',
            'customer[notify_user_ids][]':''
        # '%s'+approve_type+'%s': '' %(approve_type,),
            # str(approve_type): {
            #     'step': '1',
            #     'approve_description': '审批通过',
            #     'notify_user_ids[]': '',
        }
        self.common.post_response_json(url, body, '审批通过')
        return date_id


    #客户/商机/合同 撤销审批
    # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def cancel_approval(self,date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/'+ str(date_id) + '/revert?key='+ approve_type
        # print (url)
        body = {
            'utf8':'✓',
            'authenticity_token': self.csrf,
            '_method':'put',
            'key':approve_type,
            
            # 'customer[approve_description]': '撤销审批',
            '%s[approve_description]'% approve_type: '撤销审批'
            # str(approve_type): {
            #     'approve_description': '撤销审批',
        }
        # print (body)
        self.common.post_response_json(url, body, '撤销审批')
        return date_id


    #客户/商机/合同 审批驳回
    # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def deny_approval(self,date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/'+ str(date_id) + '/deny'
        body = {
            'utf8':'✓',
            'authenticity_token': self.csrf,
            '_method':'put',
            'key':approve_type,
            'customer[approve_description]': '驳回',
            'customer[step]': '1'
            # str(approve_type):{
            #         'step':'1',
            #         'approve_description':'审批否决',
            #         'notify_user_ids[]':''

        }
        self.common.post_response_json(url, body, '审批驳回')
        return date_id

    # 审批时编辑通知他人
    # date_id 表示客户id/ 商机id/合同id/费用报销id：customer_id/opportunity_id/contract_id
    def update_notify_user(self,date_id,approve_type='customer'):
        url = self.base_url + 'api/approvals/' + str(date_id) + '/update_notify_users'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'key': approve_type,
            str(approve_type): {
                'notify_user_ids[]': self.user.getUserId(),
            }
        }
        self.common.post_response_json(url, body, '审批通过时通知他人')

    # 获取审批状态
    def opportunities_info(self, opportunities_id):
        url = self.base_url + 'opportunities?scope=all_own&per_page=10&type=advance&section_only=true'
        body = {}
        success = self.get_response_json(url, body, 'opportunities_info')
        if not success:
            return {}
        html_str = self.response.content
        soup = BeautifulSoup(html_str, "html.parser")
        a = soup.find(attrs={'data-id': opportunities_id})
        b = a.find(attrs={'data-column': 'approve_status_i18n'})
        c = b.find('div').text
        c = c.strip()
        print(c)
        if c == "已通过":
            print("ok")
        else:
            print("ng")

    # 开启1级商机审批
    def open_first_approval(self,approval_role,editable,user_id):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
        'utf8':'✓',
        '_method':'put',
        'authenticity_token': self.csrf,
        'opportunity_approve[multistep][1][step]': '1',
        'opportunity_approve[multistep][1][enable]': '1',
        'opportunity_approve[multistep][1][type]': approval_role,
        'opportunity_approve[editable][enable]': '1',
        'opportunity_approve[editable][policy]': editable,
        # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
        'opportunity_approve[editable][fields][]': 'customer',
        'opportunity_approve[editable][fields][]': 'total_amount',
        'opportunity_approve[multistep][1][user_ids][]':user_id
        }
        respone = self.common.put_response_json(url, body, '开启1级商机审批')
        print(approval_role)
        # print (respone.status_code)
        print (approval_role,editable,user_id)

    # 开启2级商机审批
    def open_second_approval(self,approval_role_first,approval_role_second,editable,user_id_first,user_id_second):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
            'utf8':'✓',
            '_method':'put',
            'authenticity_token': self.csrf,
            'opportunity_approve[multistep][1][step]': '1',
            'opportunity_approve[multistep][1][enable]': '1',
            'opportunity_approve[multistep][1][type]': approval_role_first,
            'opportunity_approve[multistep][2][step]': '2',
            'opportunity_approve[multistep][2][enable]': '1',
            'opportunity_approve[multistep][2][type]': approval_role_second,
            'opportunity_approve[editable][enable]': '1',
            'opportunity_approve[editable][policy]': editable,
            # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
            'opportunity_approve[editable][fields][]': 'customer',
            'opportunity_approve[editable][fields][]': 'total_amount',
            'opportunity_approve[multistep][1][user_ids][]':user_id_first,
            'opportunity_approve[multistep][2][user_ids][]':user_id_second
            }
        respone = self.common.put_response_json(url, body, '开启2级商机审批')
        print(approval_role_first,user_id_first)
        print('++++++++++')
        print(approval_role_second,user_id_second)
        return approval_role_first,approval_role_second,editable,user_id_first,user_id_second

    # 开启3级商机审批
    def open_third_approval(self, approval_role_first, approval_role_second, approval_role_third, editable,user_id_first, user_id_second,user_id_third):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'opportunity_approve[multistep][1][step]': '1',
            'opportunity_approve[multistep][1][enable]': '1',
            'opportunity_approve[multistep][1][type]': approval_role_first,
            'opportunity_approve[multistep][2][step]': '2',
            'opportunity_approve[multistep][2][enable]': '1',
            'opportunity_approve[multistep][2][type]': approval_role_second,
            'opportunity_approve[editable][enable]': '1',
            'opportunity_approve[editable][policy]': editable,
            'opportunity_approve[multistep][3][step]': '3',
            'opportunity_approve[multistep][3][enable]':'1' ,
            'opportunity_approve[multistep][3][type]': approval_role_third,
            # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
            'opportunity_approve[editable][fields][]': 'customer',
            'opportunity_approve[editable][fields][]': 'total_amount',
            'opportunity_approve[multistep][1][user_ids][]': user_id_first,
            'opportunity_approve[multistep][2][user_ids][]': user_id_second,
            'opportunity_approve[multistep][3][user_ids][]': user_id_third
        }
        respone = self.common.put_response_json(url, body, '开启3级商机审批')
        return approval_role_first, approval_role_second, approval_role_third,editable, user_id_first, user_id_second,user_id_third


    # 开启4级商机审批
    def open_fourth_approval(self, approval_role_first, approval_role_second, approval_role_third,approval_role_fourth,
                            editable,user_id_first, user_id_second,user_id_third,user_id_fourth):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'opportunity_approve[multistep][1][step]': '1',
            'opportunity_approve[multistep][1][enable]': '1',
            'opportunity_approve[multistep][1][type]': approval_role_first,
            'opportunity_approve[multistep][2][step]': '2',
            'opportunity_approve[multistep][2][enable]': '1',
            'opportunity_approve[multistep][2][type]': approval_role_second,
            'opportunity_approve[editable][enable]': '1',
            'opportunity_approve[editable][policy]': editable,
            'opportunity_approve[multistep][3][step]': '3',
            'opportunity_approve[multistep][3][enable]':'1' ,
            'opportunity_approve[multistep][3][type]': approval_role_third,
            'opportunity_approve[multistep][4][step]': '4',
            'opportunity_approve[multistep][4][enable]': '1',
            'opportunity_approve[multistep][4][type]': approval_role_fourth,
            # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
            'opportunity_approve[editable][fields][]': 'customer',
            'opportunity_approve[editable][fields][]': 'total_amount',
            'opportunity_approve[multistep][1][user_ids][]': user_id_first,
            'opportunity_approve[multistep][2][user_ids][]': user_id_second,
            'opportunity_approve[multistep][3][user_ids][]': user_id_third,
            'opportunity_approve[multistep][4][user_ids][]': user_id_fourth
        }
        respone = self.common.put_response_json(url, body, '开启4级商机审批')
        return approval_role_first, approval_role_second, approval_role_third,approval_role_fourth, \
               editable, user_id_first, user_id_second,user_id_third,user_id_fourth

    # 开启5级商机审批
    def open_fifth_approval(self, approval_role_first, approval_role_second, approval_role_third,approval_role_fourth,
                            approval_role_fifth, editable,user_id_first, user_id_second,
                            user_id_third,user_id_fourth,user_id_fifth):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'opportunity_approve[multistep][1][step]': '1',
            'opportunity_approve[multistep][1][enable]': '1',
            'opportunity_approve[multistep][1][type]': approval_role_first,
            'opportunity_approve[multistep][2][step]': '2',
            'opportunity_approve[multistep][2][enable]': '1',
            'opportunity_approve[multistep][2][type]': approval_role_second,
            'opportunity_approve[editable][enable]': '1',
            'opportunity_approve[editable][policy]': editable,
            'opportunity_approve[multistep][3][step]': '3',
            'opportunity_approve[multistep][3][enable]':'1' ,
            'opportunity_approve[multistep][3][type]': approval_role_third,
            'opportunity_approve[multistep][4][step]': '4',
            'opportunity_approve[multistep][4][enable]': '1',
            'opportunity_approve[multistep][4][type]': approval_role_fourth,
            'opportunity_approve[multistep][5][step]':'5',
            'opportunity_approve[multistep][5][enable]': '1',
            'opportunity_approve[multistep][5][type]': approval_role_fifth,
            # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
            'opportunity_approve[editable][fields][]': 'customer',
            'opportunity_approve[editable][fields][]': 'total_amount',
            'opportunity_approve[multistep][1][user_ids][]': user_id_first,
            'opportunity_approve[multistep][2][user_ids][]': user_id_second,
            'opportunity_approve[multistep][3][user_ids][]': user_id_third,
            'opportunity_approve[multistep][4][user_ids][]': user_id_fourth,
            'opportunity_approve[multistep][5][user_ids][]': user_id_fifth
        }
        respone = self.common.put_response_json(url, body, '开启5级商机审批')
        return approval_role_first, approval_role_second, approval_role_third,approval_role_fourth,\
               approval_role_fifth, editable, user_id_first, user_id_second,user_id_third,user_id_fifth,

    # 开启6级商机审批
    def open_sixth_approval(self, approval_role_first, approval_role_second, approval_role_third,approval_role_fourth,
                            approval_role_fifth,approval_role_sixth,editable,user_id_first, user_id_second,
                            user_id_third,user_id_fourth,user_id_fifth,user_id_sixth):
        url = self.base_url + '/settings/opportunity_approve/update'
        body = {
            'utf8': '✓',
            '_method': 'put',
            'authenticity_token': self.csrf,
            'opportunity_approve[multistep][1][step]': '1',
            'opportunity_approve[multistep][1][enable]': '1',
            'opportunity_approve[multistep][1][type]': approval_role_first,
            'opportunity_approve[multistep][2][step]': '2',
            'opportunity_approve[multistep][2][enable]': '1',
            'opportunity_approve[multistep][2][type]': approval_role_second,
            'opportunity_approve[editable][enable]': '1',
            'opportunity_approve[editable][policy]': editable,
            'opportunity_approve[multistep][3][step]': '3',
            'opportunity_approve[multistep][3][enable]':'1' ,
            'opportunity_approve[multistep][3][type]': approval_role_third,
            'opportunity_approve[multistep][4][step]': '4',
            'opportunity_approve[multistep][4][enable]': '1',
            'opportunity_approve[multistep][4][type]': approval_role_fourth,
            'opportunity_approve[multistep][5][step]':'5',
            'opportunity_approve[multistep][5][enable]': '1',
            'opportunity_approve[multistep][5][type]': approval_role_fifth,
            'opportunity_approve[multistep][6][step]': '6',
            'opportunity_approve[multistep][6][enable]': '1',
            'opportunity_approve[multistep][6][type]': approval_role_sixth,
            # 这里应该是获取到商机模块启用的字段，需要前台页面返回的列表，批量编辑或者在详情页面编辑都可以获取得到
            'opportunity_approve[editable][fields][]': 'customer',
            'opportunity_approve[editable][fields][]': 'total_amount',
            'opportunity_approve[multistep][1][user_ids][]': user_id_first,
            'opportunity_approve[multistep][2][user_ids][]': user_id_second,
            'opportunity_approve[multistep][3][user_ids][]': user_id_third,
            'opportunity_approve[multistep][4][user_ids][]': user_id_fourth,
            'opportunity_approve[multistep][5][user_ids][]': user_id_fifth,
            'opportunity_approve[multistep][6][user_ids][]': user_id_sixth
        }
        respone = self.common.put_response_json(url, body, '开启6级商机审批')
        return approval_role_first, approval_role_second, approval_role_third,approval_role_fourth,\
               approval_role_fifth,approval_role_sixth, editable, user_id_first, user_id_second,\
               user_id_third,user_id_fifth,user_id_sixth

    # 将1-6级审批的执行放在该方法里面调用
    def opportunity_approval_setting(self):
        self.open_customer_approval()
        # self.close_customer_approval()
        editable = ['can','cannot']
        k = self.common.get_random_int(len(editable))
        approval_role_first = self.get_approval_setting()
        approval_role_second = self.get_approval_setting()
        # if approval_role_first == 'previous_superior':
        #     # 但是怎么让这个语句直接break掉呢？
        #     print('第一层级的审批设置不可以是:上一级审批人主管')
        # else:
            # self.open_fist_approval(approval_role_first,editable[k],self.get_random_user_ids())
        if approval_role_first == 'previous_superior'or (approval_role_first == 'specified_jointly'and approval_role_second=='previous_superior'):
            print('第一层级的审批设置不可以是上一级审批人主管;或者多人会签的下一层级审批人不可以是上一级审批人主管')
        else:
            self.open_second_approval(approval_role_first, approval_role_second,
                                  editable[k],self.get_random_user_ids(), self.get_random_user_ids())
        # self.open_third_approval(approval_role_first, approval_role_second,
        #                          self.get_approval_setting()editable[k], self.get_random_user_ids(),
        #                          self.get_random_user_ids(),self.get_random_user_ids())
        # self.open_fourth_approval(self.get_approval_setting(), self.get_approval_setting(),
        #                          self.get_approval_setting(),self.get_approval_setting(),
        #                          editable[k], self.get_random_user_ids(), self.get_random_user_ids(),
        #                         self.get_random_user_ids(),self.get_random_user_ids())
        # self.open_fifth_approval(self.get_approval_setting(), self.get_approval_setting(),
        #                          self.get_approval_setting(), self.get_approval_setting(),
        #                          self.get_approval_setting(),editable[k], self.get_random_user_ids(),
        #                          self.get_random_user_ids(),self.get_random_user_ids(),
        #                          self.get_random_user_ids(),self.get_random_user_ids())
        # self.open_sixth_approval(self.get_approval_setting(), self.get_approval_setting(),
        #                          self.get_approval_setting(), self.get_approval_setting(),
        #                           self.get_approval_setting(), self.get_approval_setting(),
        #                           editable[k], self.get_random_user_ids(), self.get_random_user_ids(),
        #                          self.get_random_user_ids(),self.get_random_user_ids(),
        #                          self.get_random_user_ids(),self.get_random_user_ids())







