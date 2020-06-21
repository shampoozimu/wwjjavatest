# -*- coding: utf-8 -*-
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
from testCase.contracts import testContract as contracts
from testCase.contracts import testSettingsContractsApproval as ContractsApproval
from testCase.contracts import testAddContract as AddContract
from testCase.contracts import testDeleteContract as DeleteContract
from testCase.performance.result_product_number import result_product_count_number
from testCase.performance.result_product_number import result_product_count_number_departments

from testCase.performance.result_product_number.result_product_number_authority import result_product_number_all_data
from testCase.performance.result_product_number.result_product_number_authority import result_product_number_self_and_subordinate_department_own
from testCase.performance.result_product_number.result_product_number_authority import result_product_number_self_department_own
from testCase.performance.result_product_number.result_product_number_authority import result_product_number_self_own

class products_count:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.common = common.Common(self.cookie,self.csrf)
        # 定义登录用户变量
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456','role':'超管'}
        self.sign_date_list = ['2019-01-31', '2019-03-31', '2019-05-31', '2019-07-31', '2019-09-30', '2019-11-30']
        self.userinfo_list = const.USER
        # 定义合同关联产品的ID、 产品数量、产品标准单价、产品名称
        self.actual_results = ''
        self.expect_results = ''
        global  g1,g2,g3
        #独立版test环境3个产品ID
        # g1 = 11012
        # g2 = 11013
        # g3 = 11048
        #钉钉版#test环境3个产品ID
        g1 = 12579
        g2 = 12580
        g3 = 12581
        # 钉钉版回归环境3个产品ID
        # g1 = 19005
        # g2 = 19007
        # g3 = 19006
        self.q1 = 5
        self.q2 = 10
        self.p1 = 200
        self.p2 = 150
        self.price_list = [15,20]
        self.quantity_list = [5,10]
        self.product_name_list = ['测试产品01','测试产品02']
        self.sleeptime =15

        pass




    def case_1(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _ContractsApproval =ContractsApproval.Approvals(self.cookie,self.csrf)
        _ContractsApproval.close_contract_approval()
        a =0
        for userinfo in self.userinfo_list:
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie =_login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie,self.csrf)
            _ContractsApproval =ContractsApproval.Approvals(self.cookie,self.csrf)
            _DeleteContracts =DeleteContract.DeleteContract(self.cookie,self.csrf)
            # contracts_list =_DeleteContracts.get_contract_ids()
            a = a+1
            for i in range(6):
                q1 = a
                q2 = a
                p1 = 15*(i+1)
                p2 = 10*(i+1)
                if userinfo['username'] == '13799999999' and i >= 3:
                    # 添加合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                            goods_id_list=[g1, g2],quantity_list=[q1,q2], price_list=[p1, p1],approve_status='approved',DepartmentId=1)
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                            goods_id_list=[g3, g2],quantity_list=[q2,q2], price_list=[p2, p2],approve_status='approved',DepartmentId=1)
                    # #添加草稿
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],
                            goods_id_list=[g1, g2],quantity_list=[q1,q2],price_list=[p1, p1],approve_status='draft',DepartmentId=1)
                else:
                    #添加合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                            goods_id_list=[g1, g2],quantity_list=[q1,q2], price_list=[p1, p1],approve_status='approved')
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                            goods_id_list=[g3, g2],quantity_list=[q2,q2], price_list=[p2, p2],approve_status='approved')
                    #添加草稿
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1, g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='draft')


        _login.login(self.userinfo_super['username'], self.userinfo_super['password'],
                        self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        a = 0

        for userinfo in self.userinfo_list:
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            print(userinfo['username'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
            a = a + 1
            for i in range(6):
                q1 = a
                q2 = a
                p1 = 15 *(i+1)
                p2 = 10 *(i+1)
                if userinfo['username'] == '13799999999' and i >= 3:
                    # 待审批的合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1)
                    # 审批通过的合同
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1, g3], quantity_list=[q1, q1],price_list=[p1, p1],approve_status='approved',DepartmentId=1))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g3,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='approved',DepartmentId=1))
                    # # 审批通过后否决
                    contracts_id=_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1)
                    _ContractsApproval.verify_contracts(contracts_id)
                    _ContractsApproval.deny_contracts(contracts_id)
                    # 审批否决的合同
                    _ContractsApproval.deny_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g3],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1))
                    # 合同撤销
                    _ContractsApproval.cancel_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1))

                else:
                    # 待审批的合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying')
                    # 审批通过的合同
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g3],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='approved'))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g3,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='approved'))
                    # 审批通过后否决
                    contracts_id=_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying')
                    _ContractsApproval.verify_contracts(contracts_id)
                    _ContractsApproval.deny_contracts(contracts_id)
                    # 审批否决的合同
                    _ContractsApproval.deny_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g3],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying'))
                    # 合同撤销
                    _ContractsApproval.cancel_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='applying'))



    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _ContractsApproval =ContractsApproval.Approvals(self.cookie,self.csrf)
        _ContractsApproval.close_contract_approval()
        _DeleteContracts = DeleteContract.DeleteContract(self.cookie, self.csrf)
        b =_DeleteContracts.get_contract_ids()
        page =b[0][0]
        print (page)
        for i in range(int(page)):
             c =_DeleteContracts.get_contract_ids()
             contracts_list = c[1]
             for contracts in contracts_list:
                 _DeleteContracts.delete_contract(contracts)






if __name__ == '__main__':
    _products_count =products_count()
    # os.remove('status_code_ok.txt')
    # # # os.remove('status_code.txt')
    _products_count.case_2()
    _products_count.case_1()

    # # 按用户 产品数量 报表
    # _product_count=result_product_count_number.result_product_number_user()
    # # _product_count.product_number_baobiao()
    # # # 按用户 产品数量 工作台
    # _product_count.product_number_gongzuotai()
    # #
    # # # # # 按部门 产品数量 报表
    # _product_count_number_departments=result_product_count_number_departments.result_product_number_departments()
    # _product_count_number_departments.product_number_d_baobiao()

     ##全公司权限
    # print('数据权限是全公司 对比各个时间的产品销量')
    # _all_data=result_product_number_all_data.result_product_number_all_data()
    # _all_data.all_data()
    # ## 所属部门以及子部门
    # print('数据权限是所属部门以及下属 对比各个时间的产品销量')
    # _subordinate_department_own=result_product_number_self_and_subordinate_department_own.result_product_number_self_and_subordinate_department_own()
    # _subordinate_department_own.self_and_subordinate_department_own()
    # ## 所属部门
    # print('数据权限是所属部门 对比各个时间的产品销量')
    # _self_department_own=result_product_number_self_department_own.result_product_number_self_department_own()
    # _self_department_own.self_department_own()
    # ##个人
    # print('数据权限是个人 对比各个时间的产品销量')
    # _self_own=result_product_number_self_own.result_product_number_self_own()
    # _self_own.self_own()





