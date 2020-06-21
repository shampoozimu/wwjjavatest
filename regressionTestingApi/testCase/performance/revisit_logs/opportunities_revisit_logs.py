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
from testCase.customers import testUpdateCustomer as UpdateCustomer
from testCase.opportunities import testSettingsOpportunityApproval as ApprovalOppo
from testCase.opportunities import testAddOpportunity as AddOppo
from testCase.opportunities import testDeleteOpportunity as DeleteOppo
from testCase.opportunities import testUpdateOpportunity as UpdateOpportunity

class Opportunities_revisit_logs:
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


    #关闭审批
    def approvaled(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.close_opportunitie_approval()

        list=[]
        for userinfo in self.userinfo_list:
            print (userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie =_login.cookie
            self.csrf = _login.csrf
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # #8个用户新增一条关闭审批的商机
            #添加 用户1商机
            opportunitie_id =_AddOppo.add_opportunities()
            list.append(opportunitie_id)
            print(list)

        a=list

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
               for j in range(6):
                  _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='关闭审批')
            b = b + 1

    # 待审批
    def approvaling(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.open_opportunitie_approval()
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的商机
            ##添加 待审批的商机
            opportunitie_id = _AddOppo.add_opportunities(approve_status='applying', DepartmentId=0)
            list.append(opportunitie_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='待审批')
            b = b + 1

    #审批通过
    def approve_verify(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.open_opportunitie_approval()
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的商机
            ##添加 待审批的商机
            opportunitie_id = _AddOppo.add_opportunities()
            _ApprovalOppo.approve_opportunity(opportunitie_id)
            list.append(opportunitie_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批通过')
            b = b + 1

    #审批驳回
    def deny_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.open_opportunitie_approval()
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的商机
            ##添加 审批通过后驳回
            opportunitie_id = _AddOppo.add_opportunities()
            _ApprovalOppo.approve_opportunity(opportunitie_id)
            _ApprovalOppo.deny_opportunities_approval(opportunitie_id)
            list.append(opportunitie_id)
            # print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批驳回')
            b = b + 1
    # 审批否决
    def deny_approval_opp(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.open_opportunitie_approval()
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的商机
            ##添加 审批通过后否决
            opportunitie_id = _AddOppo.add_opportunities(approve_status='applying', DepartmentId=0)
            _ApprovalOppo.deny_opportunities_approval(opportunitie_id)
            list.append(opportunitie_id)
            # print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批否决')
            b = b + 1
    # 审批撤销
    def cancel_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
            _ApprovalOppo.open_opportunitie_approval()
            
            _AddOppo = AddOppo.AddOpportunities(self.cookie, self.csrf)
            # 8个用户新增一条商机
            opportunitie_id = _AddOppo.add_opportunities(approve_status='applying', DepartmentId=0)
            _ApprovalOppo.cancel_opportunities_approval(opportunitie_id)
            list.append(opportunitie_id)
        print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateOpportunity = UpdateOpportunity.UpdateOpportunities(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateOpportunity.add_opportunities_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批撤销')
            b = b + 1


    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ApprovalOppo = ApprovalOppo.Approvals(self.cookie, self.csrf)
        _ApprovalOppo.close_opportunitie_approval()
        _DeleteOppo = DeleteOppo.DeleteOpportunities(self.cookie, self.csrf)
        b = _DeleteOppo.get_opportunitie_ids()
        print(b)
        page = b[0][0]
        print(page)
        for i in range(int(page)):
            c = _DeleteOppo.get_opportunitie_ids()
            oppo_list = c[1]
            for opportunitie_id in oppo_list:
                _DeleteOppo.delete_opportunitie(opportunitie_id)

    def opportunitie_revisit_logs(self):
        # self.case_2()
        _Opportunities_revisit_logs = Opportunities_revisit_logs()
        # _Opportunities_revisit_logs.approvaled()
        # _Opportunities_revisit_logs.approvaling()
        # # 审批否决
        # _Opportunities_revisit_logs.deny_approval_opp()

        # _Opportunities_revisit_logs.approve_verify()
        # _Opportunities_revisit_logs.deny_approval()
        _Opportunities_revisit_logs.cancel_approval()

if __name__ == '__main__':
    _Opportunities_revisit_logs =Opportunities_revisit_logs()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    # _Opportunities_revisit_logs.case_2()
    _Opportunities_revisit_logs.opportunitie_revisit_logs()











