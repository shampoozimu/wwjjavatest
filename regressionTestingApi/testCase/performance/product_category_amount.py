# -*- coding: utf-8 -*-
# import MySQLdb
from commons import common
from commons.const import const
from testCase.login import testLogin as login
from testCase.contracts import testSettingsContractsApproval as ContractsApproval
from testCase.contracts import testAddContract as AddContract
from testCase.contracts import testDeleteContract as DeleteContract
from testCase.performance.result_product_catagory_amount.product_category_amount_authority import result_product_category_amount_all_data
from  testCase.performance.result_product_catagory_amount.product_category_amount_authority import result_product_category_amount_self_and_subordinate_department_own
from testCase.performance.result_product_catagory_amount.product_category_amount_authority import result_product_category_amount_self_department_own
from testCase.performance.result_product_catagory_amount.product_category_amount_authority import result_product_category_amount_self_own

class products_category_amount:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.common = common.Common(self.cookie,self.csrf)
        # 定义登录用户变量
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        # 定义12个月日期 创建12个月的合同
        self.sign_date_list = ['2019-01-31', '2019-03-31', '2019-05-31', '2019-07-31', '2019-09-30', '2019-11-30']
        # 定义每个月创建合同的合同金额
        self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
                                  [220, 230]]
        self.userinfo_list = const.USER
        # 定义合同关联产品的ID、 产品数量、产品标准单价、产品名称
        self.actual_results = ''
        self.expect_results = ''
        global  g1,g2,g3
        #独立版test环境3个产品ID
        # g1 = 11012
        # g2 = 11013
        # g3 = 11048
        #钉钉版test环境3个产品ID
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

        self.goods_id_list = [12579, 12580]
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
            print(userinfo['username'])
            _AddContract = AddContract.AddContract(self.cookie,self.csrf)
            _ContractsApproval =ContractsApproval.Approvals(self.cookie,self.csrf)
            _DeleteContracts =DeleteContract.DeleteContract(self.cookie,self.csrf)
            # contracts_list =_DeleteContracts.get_contract_ids()
            a = a+1
            # 独立版test环境3个产品ID
            # g1 = 11012
            # g2 = 11013
            # g3 = 11048
            #钉钉test企业产品
            g1 = 12579
            g2 = 12580
            g3 = 12581
            # # 钉钉版回归环境3个产品ID
            # g1 = 19005
            # g2 = 19007
            # g3 = 19006
            for i in range(6):
                q1 = a *(i+1)
                q2 = a *(i+1)
                p1 = 15
                p2 = 10
                if userinfo['username'] == '13799999999' and i>=3 :
                    # 添加合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                                            goods_id_list=[g1, g1],quantity_list=[q1,q1], price_list=[p1, p1],DepartmentId=1)

                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],
                                            goods_id_list=[g2, g2],quantity_list=[q2,q2], price_list=[p2, p2],DepartmentId=1)
                    # 添加草稿
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],
                                            goods_id_list=[g1, g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='draft')
                else:
                    # 添加合同
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],
                                            goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1,p1])
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],
                                            goods_id_list=[g2,g2],quantity_list=[q1,q2],price_list=[p1,p1])
                    # 添加草稿
                    _AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],
                                            goods_id_list=[g1, g2],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='draft')

        _login.login(self.userinfo_super['username'], self.userinfo_super['password'],self.userinfo_super['role'])
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
                q1 = a *(i+1)
                q2 = a *(i+1)
                p1 = 15
                p2 = 10
                if userinfo['username'] == '13799999999' and i>=3:
                    # 待审批的合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1)
                    # 审批通过的合同
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1, g2],
                                                                        quantity_list=[q1, q2],price_list=[p1, p1],approve_status='applying',DepartmentId=1))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g3,g2],
                                                                        quantity_list=[q1,q2],price_list=[p1, p2],approve_status='applying',DepartmentId=1))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g2,g2],
                                                                        quantity_list=[q2,q2],price_list=[p2, p2],approve_status='applying',DepartmentId=1))
                    # 审批通过后否决
                    contracts_id=_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],
                                                                         quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1)
                    _ContractsApproval.verify_contracts(contracts_id)
                    _ContractsApproval.deny_contracts(contracts_id)
                    # 审批否决的合同
                    _ContractsApproval.deny_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],
                                                                        quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1))
                    # 合同撤销
                    _ContractsApproval.cancel_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],
                                                                        quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying',DepartmentId=1))

                else:
                    # 待审批的合同
                    _AddContract.add_contracts_products_add(sign_date =self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying')
                    # 审批通过的合同
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='applying'))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g3,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='applying'))
                    _ContractsApproval.verify_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g2,g2],quantity_list=[q2,q2],price_list=[p2, p2],approve_status='applying'))
                    # 审批通过后否决
                    contracts_id=_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying')
                    _ContractsApproval.verify_contracts(contracts_id)
                    _ContractsApproval.deny_contracts(contracts_id)
                    # 审批否决的合同
                    _ContractsApproval.deny_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g1],quantity_list=[q1,q1],price_list=[p1, p1],approve_status='applying'))
                    # 合同撤销
                    _ContractsApproval.cancel_contracts(_AddContract.add_contracts_products_add(sign_date=self.sign_date_list[i],goods_id_list=[g1,g2],quantity_list=[q1,q2],price_list=[p1, p2],approve_status='applying'))



    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        print(self.userinfo_super['username'])
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
    _products_category_amount =products_category_amount()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    _products_category_amount.case_2()
    _products_category_amount.case_1()

    # _product_category_money = result_product_category_money_amount.result_product_category_amount_user()
    # # 按用户 产品分类销售额 报表
    # _product_category_money.product_category_amount_baobiao()
    # # # 按用户 产品分类销售额 工作台
    # _product_category_money.product_category_amount_gongzuotai()
    # # # 按部门  产品分类销售额 报表
    # _product_category_money_amount_department=result_product_category_money_amount_departments.result_product_category_amount_departments()
    # # _product_category_money_amount_department.product_category_amount_d_baobiao()
    # print('数据权限是全公司 对比各个时间的产品分类销售金额')
    # _all_data=result_product_category_amount_all_data.result_product_category_amount_all_data()
    # _all_data.all_data()
    # print('数据权限是所属部门以及下属 对比各个时间的产品分类销售金额')
    # _self_and_subordinate_department_own=result_product_category_amount_self_and_subordinate_department_own.result_product_category_amount_self_and_subordinate_department_own()
    # _self_and_subordinate_department_own.self_and_subordinate_department_own()
    # print('数据权限是所属部门 对比各个时间的产品分类销售金额')
    # _self_department_own=result_product_category_amount_self_department_own.result_product_category_amount_self_department_own()
    # _self_department_own.self_department_own()
    # print('数据权限是个人 对比各个时间的产品分类销售金额')
    # _self_own=result_product_category_amount_self_own.result_product_category_amount_self_own()
    # _self_own.self_own()
    #
    #
    #






