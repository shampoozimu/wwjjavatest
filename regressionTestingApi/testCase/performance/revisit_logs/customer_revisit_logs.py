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
from testCase.customers import testCustomer as Customers
from testCase.approvals import testApprovalSetting as CustomersApproval
from testCase.customers import testAddCustomer as AddCustomer
from testCase.customers import testDeleteCustomer as DeleteCustomer
# from testCase.performance.result_Customers_number import result_Customer_number
# from testCase.performance.result_Customers_number import result_Customer_number_departments
from testCase.customers import testUpdateCustomer as UpdateCustomer


class Customers_revisit_logs:
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
        _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie,self.csrf)
        _CustomersApproval.close_approval()
        dict={}
        list=[]
        for userinfo in self.userinfo_list:
            print (userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie =_login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ## 添加
            customer_id =_AddCustomer.add_customers()
            dict.update({userinfo['username']: customer_id})
            list.append(customer_id)
            print(list)
        a=list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf,self.token)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='关闭审批')

            b = b + 1

    # 待审批
    def approvaling(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.open_approval()
        # a =0
        customer_id = ''
        dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ##添加 待审批的客户
            customer_id = _AddCustomer.add_customers(approve_status='applying', DepartmentId=0)
            dict.update({userinfo['username']: customer_id})
            list.append(customer_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='待审批')
            b = b + 1

    #审批通过
    def approve_verify(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.open_approval()
        # a =0
        customer_id = ''
        dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ##添加
            customer_id = _AddCustomer.add_customers(approve_status='applying', DepartmentId=0)
            _CustomersApproval.approve_verify(customer_id)
            dict.update({userinfo['username']: customer_id})
            list.append(customer_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批通过')
            b = b + 1

    #审批驳回
    def deny_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.open_approval()
        # a =0
        customer_id = ''
        dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ##添加 审批通过后驳回
            customer_id = _AddCustomer.add_customers(approve_status='applying', DepartmentId=0)
            _CustomersApproval.approve_verify(customer_id)
            # 审批被驳回
            _CustomersApproval.deny_approval(customer_id)
            dict.update({userinfo['username']: customer_id})
            list.append(customer_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批驳回')
            b = b + 1
    # 审批否决
    def deny_approval_customer(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.open_approval()
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ##添加 待审批的客户后否决
            customer_id = _AddCustomer.add_customers(approve_status='applying', DepartmentId=0)
            # 审批被否决
            _CustomersApproval.deny_approval(customer_id)
            list.append(customer_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批否决')
            b = b + 1
    # 审批撤销
    def cancel_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # a =0
        customer_id = ''
        dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomer = AddCustomer.AddCustomer(self.cookie, self.csrf)
            _CustomersApproval = CustomersApproval.ApprovalSettings(self.cookie, self.csrf)
            _CustomersApproval.open_approval()
            # 8个用户新增一条关闭审批的客户
            ##添加 审批撤销
            customer_id = _CustomersApproval.cancel_approval(_AddCustomer.add_customers(approve_status='applying'))
            dict.update({userinfo['username']: customer_id})
            list.append(customer_id)
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateCustomer = UpdateCustomer.UpdateCustomer(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateCustomer.add_customer_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批撤销')
            b = b + 1
   ## 删除
    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _CustomersApproval =CustomersApproval.ApprovalSettings(self.cookie,self.csrf)
        _CustomersApproval.close_approval()
        _DeleteCustomers = DeleteCustomer.DeleteCustomer(self.cookie, self.csrf)
        b =_DeleteCustomers.get_customer_ids()
        page =b[0][0]
        print (page)
        for i in range(int(page)):
             c =_DeleteCustomers.get_customer_ids()
             Customers_list = c[1]
             for Customers in Customers_list:
                 _DeleteCustomers.delete_customer(Customers)


    def customer_revisit_logs(self):
        _Customers_revisit_logs = Customers_revisit_logs()
        # 关闭审批
        _Customers_revisit_logs.approvaled()
        # # # 待审批
        # _Customers_revisit_logs.approvaling()
        # # 审批通过
        # _Customers_revisit_logs.approve_verify()
        # # 审批被驳回
        # _Customers_revisit_logs.deny_approval()
        # # 审批否决
        # _Customers_revisit_logs.deny_approval_customer()
        # # 审批被撤销
        # _Customers_revisit_logs.cancel_approval()

if __name__ == '__main__':
    _Customers_revisit_logs =Customers_revisit_logs()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    # _Customers_revisit_logs.case_2()

    # #创建客户数的对象
    # _Customer_number = result_Customer_number.result_Customer_number_user()
    # #按用户 客户数 报表筛选
    # _Customer_number.Customer_number_baobiao()
    # #按用户 客户数 工作台筛选
    # _Customer_number.Customer_number_gongzuotai()
    # # #按部门 客户数 报表筛选
    # _Customer_number_departments=result_Customer_number_departments.result_Customer_number_departments()
    # _Customer_number_departments.Customer_number_d_baobiao()
     # 客户跟进
    _Customers_revisit_logs.customer_revisit_logs()









