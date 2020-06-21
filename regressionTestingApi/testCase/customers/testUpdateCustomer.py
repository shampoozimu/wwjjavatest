# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'

from bs4 import BeautifulSoup
import json
import requests
import random
import datetime
import re
from decimal import Decimal as D
from commons import common
from commons.const import const
import re
import random
import string
from testCase.leads.testGetLeads import GetLeads
class UpdateCustomer:
    def __init__(self, cookie, csrf,token=123456):
        self.common = common.Common(cookie, csrf,token)
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = csrf
        self.cookie = cookie
        self.cookie = token
        self.response = ''
        self.users_id = []
        self.customers_id = []
        self.get_lead_ids = GetLeads(cookie, csrf)


    def update_customers_by_scope(self, scope, customers_id):
        self.quick_edit_customers(scope, customers_id)
        self.customers_field_update(scope, customers_id)
        # 批量转移客户
        self.customers_mass_transfer(scope, customers_id)
        # 批量添加协作人
        self.customers_add_assist_user(scope, customers_id)

        for customer_id in customers_id:
            self.add_assist_user_for_customer(customer_id)
            self.upload_attachment_for_current_customer(customer_id)
            event_id = self.create_event_for_customer(customer_id)
            self.update_event_complete(event_id)
            self.update_event_todo(event_id)
            self.get_event_todo(customer_id)
        # 批量客户转移到公海
        self.customers_to_common_pool(customers_id)
    # 批量编辑
    def customers_field_update(self, scope, customer_ids):
        url = self.base_url + 'batch_edit/field_form'
        params = {
            'model': 'Customer'
        }
        response = self.common.get_response_json(url, params, '打开编辑客户的窗扣')
        if response != False:
            S = response.content
            soup = BeautifulSoup(S, 'html.parser')
            optional_field = soup.find(attrs={'id': 'field_choice'})
            fields = re.findall(r"value=\"(.*?)\">", str(optional_field))

            selected_fields = soup.findAll(attrs={'class': 'batch-edit-custom-field hidden'})
            selected_field_list = []
            for i in selected_fields:
                selected_field = re.findall(r"value=\"(.*?)\">", str(i))
                selected_field_list.append(selected_field)

            url = self.base_url + 'api/customers/batch_update'
            body = {
                'utf8': '✓',
                'authenticity_token': self.csrf,
                'field_choice': fields[1],
                'customer[' + fields[1] + ']': selected_field_list[0][3],
                'ids[]': customer_ids[0],
                'ids[]': customer_ids[1]
            }
            response = self.common.put_response_json(url, body, '批量编辑客户')
            return response
    # 快捷编辑客户
    def quick_edit_customers(self, scope, customer_ids):
        for customer_id in customer_ids:
            self.quick_edit_customer('111111111', customer_id)
    # 快捷编辑单个客户
    def quick_edit_customer(self, new_value, customer_id):
        url = self.base_url + 'quick_edit/field_form'
        params = {
            'model': 'Customer',
            'id': customer_id,
            'field_name': 'name',
            'page_type': 'index'
        }
        self.common.get_response_json(url, params, '获取客户详情***************')

        url = self.base_url + 'api/customers/' + str(customer_id)
        body = {
            'utf8': '✓',
            '_method': 'patch',
            'authenticity_token': self.csrf,
            'customer[id]': customer_id,
            'common_id': '',
            'customer[name]': new_value
        }
        response = self.common.put_response_json(url, body, '快捷编辑客户，编辑的字段是：')
    # 查重字段
    def check_duplicate_field(self, field, new_value, customer_id):
        url = self.base_url + 'api/customers/check_duplicate_field.json'
        body = {
            'field': field,
            'field_value': new_value,
            'customer_id': customer_id
        }
        response = self.common.post_response_json(url, body, '查重字段: ')
        return response
    # 批量转移客户
    def customers_mass_transfer(self, scope, customers_id):
        url = self.base_url + 'api/customers/mass_transfer'
        self.users_id = self.users_get_all()
        body = {
            'authenticity_token': self.csrf,
            'user_id': self.users_id[0],
            'transfer_contracts': 'false',
            'transfer_opportunities': 'false',
            'nowin_opportunities': 'false',
            'customer_ids[]': customers_id[0],
            'customer_ids[]': customers_id[1],
            'customer_ids[]': customers_id[2]
        }
        response = self.common.put_response_json(url, body, '批量转移客户')
        if not response:
            return {}
    # 获取所有的用户id
    def users_get_all(self):
        url = self.base_url + 'api/users'
        params = {
            'username': '',
            'page': 1,
            'perPage': 15
        }
        response = self.common.get_response_json(url, params, '获取用户************')
        if not response:
            return {}
        user_models = response.json()['models']
        user_ids = []
        for user in user_models:
            user_ids.append(user['id'])
        return user_ids
    # 获取客户的id list  需要用新的
    def get_customer_ids(self, scope):
        url = self.base_url + 'customers'
        params = {
            'order': 'asc',
            'scope': scope,
            'sort': 'customers.updated_at desc',
            'per_page': '10',
            'type': 'advance',
            'section_only': 'true'
        }
        response = self.common.get_response_json(url, params, '获取所有的客户************')
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        checked_customer = soup.find(attrs={'data-entity-table-name': 'Customer'})
        if checked_customer:
            a = str(checked_customer)
            customer_ids = re.findall(r"data-id=\"(.*?)\">", a)
            return customer_ids

    # 批量添加协作人
    def customers_add_assist_user(self, scope, customer_ids):
        url = self.base_url + 'batch_edit_assist_user/field_form'
        params = {
            'model': 'Customer'
        }
        response = self.common.get_response_json(url, params, '打开添加协作人的窗口************')
        if not response:
            return {}
        self.response = response
        S = self.response.content
        soup = BeautifulSoup(S, 'html.parser')
        assit_user_content = soup.find(attrs={'id': 'customer_assist_user_ids'})
        # 获取所有下拉框中的用户对应的id
        assit_users = re.findall(r"value=(.*?)>", str(assit_user_content))
        url = self.base_url + 'api/customers/batch_update_assist_user'
        for operation_selection in const.CUSTOMER_ADD_ASSIST_USER_OPERATION_SELECTION:
            body = {
                'utf8': '✓',
                'authenticity_token': self.csrf,
                'operation_selection': operation_selection,
                'customer[assist_user_ids][]': '',
                'customer[assist_user_ids][]': assit_users[0],
                'customer[assist_user_ids][]': assit_users[1],
                'ids[]': customer_ids[0],
                'ids[]': customer_ids[1]
            }
            response = self.common.put_response_json(url, body, '给所选的客户添加协作人:' + '添加的操作是 is:' + operation_selection)
            if not response:
                return {}

    # 批量客户转移到公海
    def customers_to_common_pool(self, customers_id):
        url = self.base_url + 'api/customers/mass_transfer_to_common_pool'
        body = {
            'common_id': 815,
            'authenticity_token': self.csrf,
            'customer_ids[]': customers_id[0],
            'customer_ids[]': customers_id[1],
            'customer_ids[]': customers_id[2]
        }
        response = self.common.put_response_json(url, body, '批量转移客户到公海************')
        if not response:
            return {}
        self.response = response
        return self.response.json()

    # 给客户添加协作人
    def add_assist_user_for_customer(self, customer_id):
        url = self.base_url + 'customers/' + str(customer_id) + '/edit_assist_user'
        params = {}
        response = self.common.get_response_json(url, params, '客户详情页打开添加协作人的窗口')

        url = self.base_url + 'api/customers/' + str(customer_id) + '/update_assist_user'
        self.users_id = self.users_get_all()
        body = {
            'utf8': '✓',
            '_method': 'patch',
            'customer[id]': customer_id,
            'customer[assist_user_ids][]': '',
            'customer[assist_user_ids][]': self.users_id[0],
            'customer[assist_user_ids][]': self.users_id[1]
        }
        self.common.post_response_json(url, body, '客户详情页给该客户添加协作人')

    # 给当前客户添加附件
    def upload_attachment_for_current_customer(self, customer_id):
        url = self.base_url + 'attachments/' + str(customer_id) + '/add_attachment'
        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'klass': 'Customer',
            'attachment_ids[]': 123456,
            'note': ''
        }
        self.common.post_response_json(url, body, '客户详情页添加附件')

    # 新建任务
    def create_event_for_customer(self, customer_id):
        url = self.base_url + 'events/new'
        params = {
            'ajax_back_to': '/events?entity_id=' + str(customer_id) + '&entity_klass=Customer',
            'entity_id': customer_id,
            'entity_klass': 'Customer'
        }
        response = self.common.get_response_json(url, params, '打开新建任务窗口')
        url = self.base_url + 'api/events'
        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'event[note]': '给客户打电话',
            'event[remind_at]': '2018-03-02 17:19',
            'event[remind_type]': 'punctual',
            'event[related_item_id]': customer_id,
            'event[related_item_type]': 'Customer',
            'event[user_ids]': self.users_get_all()[0]
        }
        response = self.common.post_response_json(url, body, '客户详情页创建任务')
        if not response:
            return {}
        self.response = response
        event_id = response.json()['data']['id']
        return event_id

    # 将任务设为已完成
    def update_event_complete(self, event_id):
        url = self.base_url + 'api/reminders/' + str(event_id) + '/update_status'
        params = {
            'remind_status': 'complete'
        }
        self.common.get_response_json(url, params, '把任务设置成已完成')

    # 将任务设为未完成
    def update_event_todo(self, event_id):
        url = self.base_url + 'api/reminders/' + str(event_id) + '/update_status'
        params = {
            'remind_status': 'todo'
        }
        self.common.get_response_json(url, params, '设置任务为未完成')

    # 获取当前用户为完成的任务
    def get_event_todo(self, customer_id):
        url = self.base_url + 'api/events/count_by_status'
        params = {
            'entity_id': customer_id,
            'entity_klass': 'Customer',
            'status': 'expired_and_todo'
        }
        self.common.get_response_json(url, params, '获取所有已完成的任务')

    # 审批客户
    def approve_customer(self, customer_id):
        url = self.base_url + 'api/approvals/' + str(customer_id) + '/approve'
        body = {
            '_method': 'put',
            'authenticity_token': self.csrf,
            'customer[approve_description]': '',
            'customer[notify_user_ids][]': '',
            'customer[step]': '1',
            'key': 'customer',
            'utf8': '✓'
        }
        self.common.post_response_json(url, body, '审批客户通过')

    # 审批否决客户
    def deny_customer(self, customer_id):
        url = self.base_url + 'api/approvals/' + str(customer_id) + '/deny'
        body = {
            '_method': 'put',
            'authenticity_token': self.csrf,
            'customer[approve_description]': '不于通过',
            'customer[step]': '1',
            'key': 'customer',
            'utf8': '✓'
        }
        self.common.post_response_json(url, body, '审批否决客户')

    # 审批时编辑通知他人
    def update_notify_user(self, customer_id, user_id):
        url = self.base_url + 'api/approvals/' + str(customer_id) + '/update_notify_users'
        body = {
            '_method': 'put',
            'authenticity_token': self.csrf,
            'customer[notify_user_ids][]': user_id,
            'key': 'customer',
            'utf8': '✓'
        }
        self.common.post_response_json(url, body, '审批通过时通知他人')
    # 客户拜访签到
    def checkins(self,checkable_id):
        # token = '7932e13e8a3cea4e8a4e551f41356d29'
        url = self.base_url + 'api/v2/checkins'
        body = {
                "checkin": {
                    "message": "签到",
                    "checkable_type": "Customer",
                    "checkable_id": checkable_id,
                    "checkin_name": "22",
                    "address_attributes": {
                        "off_distance": 43,
                        "detail_address": "上海市浦东新区张江高科技园区我查查信息技术(上海)有限公司星创科技广场",
                        "lng": 121.6266115993924,
                        "lat": 31.20879231770833
                    },
                    "device_info": "iPhone 6s Plus"
                },
                "attachment_ids": [],
                "update_entity_address": 'false'
        }
        response = self.common.post_json_response_json(url, body, "add_lead_revisit_log")
        print(response.status_code)
        return (response.json()['data']['id'])

    # 获取各模块跟进状态和跟进类型
    def get_visit_way_list(self):
        url = self.base_url + 'field_maps'
        body = {}
        response = self.common.get_response_json(url, body, 'get_page')
        soup = BeautifulSoup(response.content, 'html.parser')
        lead_way = str(str(soup).split('跟进状态')[1]).split('渠道')[0]
        lead_status = re.findall(r' data-fieldvalue-id=\"(\d+)\"', str(lead_way))
        customer_way = str(str(soup).split('跟进状态')[2]).split('客户类型')[0]
        customer_status = re.findall(r' data-fieldvalue-id=\"(\d+)\"', str(customer_way))
        opportunity_way = str(str(soup).split('销售阶段')[1]).split('商机类型')[0]
        opportunity_status = re.findall(r' data-fieldvalue-id=\"(\d+)\"', str(opportunity_way))
        contract_way = str(str(soup).split('合同状态')[1]).split('回款类型')[0]
        contract_status = re.findall(r' data-fieldvalue-id=\"(\d+)\"', str(contract_way))
        visit_way = str(str(soup).split('跟进类型')[1]).split('费用类型')[0]
        visit_way_list = re.findall(r' data-fieldvalue-id=\"(\d+)\"', str(visit_way))
        return lead_status, customer_status, opportunity_status, contract_status, visit_way_list
    # 写跟进
    def add_customer_revisit_log(self,id,date_list='2019-03-01 16:18',data=''):
        url = self.base_url + 'api/customers/' + str(id) + '/revisit_logs?customer_id=' + str(id)
        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'request_ticket': ''.join(random.sample(string.ascii_letters + string.digits, 12)),
            'revisit_log[category]': self.get_visit_way_list()[4][0],
            'revisit_log[real_revisit_at]': date_list,
            'revisit_log[content]': data+'关闭审批'.join(random.sample(string.ascii_letters + string.digits, 10)),
            'revisit_log[loggable_attributes][status]': self.get_visit_way_list()[1][0],
            'revisit_log[loggable_attributes][id]': id,
            'revisit_log[remind_at]': ''
        }
        response = self.common.post_response_json(url, body, "add_customer_revisit_log")

