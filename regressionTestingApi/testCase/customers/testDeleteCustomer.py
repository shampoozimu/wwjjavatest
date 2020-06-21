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

class DeleteCustomer:
    def __init__(self, cookie, csrf,token=123456):
        self.common = common.Common(cookie,csrf,token)
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = csrf
        self.token =token
        self.cookie = cookie
        self.response = ''
        self.user_id = ''
        self.customers_id =[]
        pass

    #删除单个客户
    def delete_customer(self, customer_id):
        url = self.base_url + '/customers/bulk_delete'
        body = {
            'del_associated':'true',
            'authenticity_token':self.csrf,
            'customer_ids[]': customer_id
        }
        response = self.common.delete_response_json(url, body, '删除当前客户')
        return response
    #批量删除客户
    def delete_customers(self, customer_ids):
        url = self.base_url + 'customers/bulk_delete'
        body = [("utf8", "✓"), ("authenticity_token", self.csrf,), ("customer_ids[]", customer_ids[0]), ("customer_ids[]", customer_ids[1])]
        response = self.common.delete_response_json(url, body, '批量删除客户')
        if not response:
            return {}
        # self.response = response
        # return self.response.json()
    #获取当前页的Customer id
    def get_customer_ids(self):
        # url = self.base_url + 'customers'
        url = self.base_url + 'api/pc/customers?scope=all_own&type=advance&section_only=true&order=desc&sort=customers.updated_at&page=1&per_page=100'
        body = {
        }
        response = self.common.get_json_response_json(url, body, '删除客户时获取所有客户')
        if not response:
            return {}
        self.response = response
        print(self.response.json())
        a =self.response.json()['data']['list']
        page =self.response.json()['data']['total_pages']
        id_list =[]
        for id in a:
            id_list.append(id["id"])
        return(page,id_list)
