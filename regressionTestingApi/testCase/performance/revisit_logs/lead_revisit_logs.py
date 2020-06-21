from bs4 import BeautifulSoup
import os
import json
import requests
import random
import datetime
# import MySQLdb
import time
import re
import sys

from decimal import Decimal as D
from commons import common
from commons.const import const
from commons import filters
from testCase.login import testLogin as login
from testCase.leads import testAddLead as AddLead
from testCase.leads import testDeleteLead as DeleteLeads
from testCase.leads import testGetLeads as  GetLeads
from testCase.leads import testUpdateLead as UpdateLeads


class Lead_revisit_logs:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        # self.userinfo_super = {'username': '15639356523', 'password': 'Ab123456','role':'超管'}
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        self.date_list = ['2018-01-10 02:51:58', '2018-03-10 02:51:58', '2018-05-10 02:51:58', '2018-07-10 02:51:58',
                          '2018-09-10 02:51:58 ', '2018-11-10 02:51:58']

        # self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
        #                           [220, 230]]
        self.userinfo_list = const.USER
        self.token = ''

        pass


    #线索跟进次数
    def approvaled(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        list=[]
        for userinfo in self.userinfo_list:
            print (userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie =_login.cookie
            self.csrf = _login.csrf
            _AddLead= AddLead.AddLead(self.cookie, self.csrf)
            #8个用户新增一条关闭审批的客户
            ##添加 用户1客户
            lead_id =_AddLead.add_lead()
            list.append(lead_id)
            print(list)
        a=list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateLead = UpdateLeads.UpdateLeads(self.cookie, self.csrf)
            for i in range(b):
               for j in range(6):
                   print(b)
                   # print(i)
                   print(b - 1 - i)
                   _UpdateLead.add_lead_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='新增线索')
            b = b + 1


   ## 删除
    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _DeleteLeads = DeleteLeads.DeleteLeads(self.cookie, self.csrf)
        b =_DeleteLeads.get_lead_ids()
        page =b[0][0]
        print (page)
        for i in range(int(page)):
             c =_DeleteLeads.get_lead_ids()
             leads_list = c[1]
             for leads in leads_list:
                 _DeleteLeads.delete_lead(leads)

    def lead_revisit_logs(self):
        _lead_revisit_logs = Lead_revisit_logs()
        _lead_revisit_logs.approvaled()

if __name__ == '__main__':
    _lead_revisit_logs =Lead_revisit_logs()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    _lead_revisit_logs.case_2()
    _lead_revisit_logs.approvaled()










