# -*- coding: utf-8 -*-
import datetime
import os
import codecs
import operator
from commons.const import const
from testCase.login import testLogin as login
from testCase.performance import result
import json
from testCase.roles import testGetRoles
import time


class result_contract_number_year:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        ##  用户3
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        ##  用户1
        self.userinfo_ = {'username': '15000249334', 'password': 'Ik123456', 'role': '普通管理员'}

        self.date_list = [['2019-01-01', '2019-12-31']]

        self.title_list_first = [
                      ['按年查看本年合同数']
                      ]
        self.month = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

        self.title = [['按年查看2019年合同数'] ]

        self.date = [['other']
             ]
        self._month_view = [['2019']]

        self.user = [
            ['设计部-用户1', '设计部-用户2', '产品部-用户3', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7', '设计部二级部门-用户8'],
            ['设计部-用户1', '设计部-用户2', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7','设计部二级部门-用户8'],
            ['设计部-用户1', '设计部-用户2', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7'] ,
            ['设计部-用户1', '销售部-用户5', '同部门下属-用户7']]

        self.field_permission_grant_scope = ['organization_own', 'self_and_subordinate_department_own',
                                             'self_department_own', 'self_own']

        pass


    def check_data_user(self,s1,type1,i =0,_users= ['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],k=0):
        current_case = self.title[i]
        time.sleep(2)
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _Roles = testGetRoles.GetRole(self.cookie, self.csrf)
        ### 设置用户的角色必须是普通管理员的角色
        _Roles.ding_set_data_authority(self.field_permission_grant_scope[k])
        print(self.field_permission_grant_scope[k])
        _login = login.Login()
        _login.login(self.userinfo_['username'], self.userinfo_['password'], self.userinfo_['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _result = result.result(self.cookie, self.csrf)
        ##Actual_result输出三个值 图表，中间值，表格
        ## 业绩类型切换 合同数：contract_count 商机数：win_count 产品销量：product_count 产品分类销量：product_category_count s= 4
        Actual_result_all = _result.gole_completion(from_date=self.date_list[i][0], to_date=self.date_list[i][1], type=type1, dimension='year',
                     data=self.date[i][0])

        # print(Actual_result_all[0])
        # # # Expected_result输出两个值 中间值，表格
        Expected_result_all =_result.count_get_completion_year(_months=self.month[i], _users= _users,_month_view=self._month_view[i],s=s1)
        # # # # 比较图表的统计值是否相同
        Actual_result = Actual_result_all[0]
        # #图表的预期结果和表格的预期结果相同 所以取的是表格预期结果的值
        Expected_result = Expected_result_all
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True:
                f = codecs.open('contract_number.txt', 'a', 'utf-8')
                a = str(_users)+str(str(current_case)+'图表的排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_number.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case)+'图表的排名' + ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(
                    datetime.datetime.now()))
                f.write(a + '\n')
        # ##比较实际中间的统计值和预期中间的统计值是否相同
        Actual_result=Actual_result_all[1]
        Expected_result=Expected_result_all
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True :
                f = codecs.open('contract_number_y.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case)+'中间统计排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_number_y.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case)+'中间统计排名' + ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(datetime.datetime.now()))
                f.write(a + '\n')
            #
        #比较表格实际排名和预期排名是否相等
        Actual_result = Actual_result_all[2]
        Expected_result = Expected_result_all
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True:
                f = codecs.open('contract_number_y.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case) +'表格排名'+ ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_number_y.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case) +'表格排名'+ ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(
                    datetime.datetime.now()))
                f.write(a + '\n')
            #

    def payments_amount_baobiao(self,s1,type1):
        _result_count = result_contract_number_year()
        for j in range(len(self.user)):
            print(self.user[j])
            _result_count.check_data_user(s1,type1,i=0, _users=self.user[j],k=j)


if __name__ == '__main__':
    _result_count =result_contract_number_year()
    if os.path.exists('contract_number_y.txt') == True:
        os.remove('contract_number_y.txt')
    #工作台结果对比
    # _result_count.payments_amount_gongzuotai()
    #按年结果对比
    _result_count.payments_amount_baobiao(4, 'product_category_count')




