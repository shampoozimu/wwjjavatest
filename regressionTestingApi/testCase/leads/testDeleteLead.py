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

class DeleteLeads:
    def __init__(self, cookie, csrf):
        self.common = common.Common(cookie, csrf)
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = csrf
        self.cookie = cookie
        self.response = ''
        self.user_id = ''
        self.lead_id =[]
        pass

    #删除单个线索
    def delete_lead(self, lead_id):
        url = self.base_url + 'leads/'+str(lead_id)
        body = {
            '_method':'delete',
            'authenticity_token':self.csrf
        }
        response = self.common.post_response_json(url, body, '删除当前线索')
        return response
    # #批量删除线索
    def delete_leads(self, scope, lead_ids):
        url = self.base_url + 'leads/bulk_delete'
        body = {
            'lead_ids[]': lead_ids[0],
            'lead_ids[]': lead_ids[1],
            'authenticity_token': self.csrf
        }
        response = self.common.delete_response_json(url, body, '批量删除线索')
        if not response:
            return {}

        # 获取当前页的opportunitie id

    def get_lead_ids(self):
        url = self.base_url + 'leads?scope=all_own&section_only=true'
        body = {
            'scope': 'all_own',
            'section_only': 'true'
        }
        response = self.common.get_response_json(url, body, '删除线索时获取所有商机')
        if not response:
            return {}
        self.response = response
        S = self.response.content
        soup = BeautifulSoup(S, 'html.parser')
        contract_id_list = re.findall(r"data-id=\"(.*?)\">", str(soup))
        page = re.findall(r"data-total-pages=\"(.*?)\">", str(soup))
        return page, contract_id_list

        # if not response:
        #     return {}
        # self.response = response
        # S = self.response.content
        # soup = BeautifulSoup(S, 'html.parser')
        # contract_id_list = re.findall(r"data-id=\"(.*?)\">", str(soup))
        # page = re.findall(r"data-total-pages=\"(.*?)\">", str(soup))
        # return page, contract_id_list