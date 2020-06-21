# -*- coding: utf-8 -*-
import datetime
import os
import codecs
import operator
from commons.const import const
from testCase.login import testLogin as login
from testCase.performance import result
import json
import time
from testCase.roles import testGetRoles

class result_product_amount_quarter:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        # self.dimension1 = 'user'
        # self.dimension2 = 'department'
        # self.Actual_result =""
        ##  用户3
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        ##  用户1
        self.userinfo_ = {'username': '15000249334', 'password': 'Ik123456', 'role': '普通管理员'}

        self.date_list = [['2019-01-01', '2019-03-31'], ['2019-04-01', '2019-06-31'], ['2019-07-01', '2019-09-31'],
                          ['2019-10-01', '2019-12-31'], ['2019-04-01', '2019-08-31'], ['2019-01-01', '2019-12-31']]

        self.month = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [4, 5, 6, 7, 8],
                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

        self.title = [[' 2019一季度'], [' 2019二季度'], [' 2019三季度'], [' 2019四季度'], [' 4~8月金额'], ['1~12月金额']]

        self._month_view = [['2019一季度'], ['2019二季度'], ['2019三季度'], ['2019四季度'],
                            ['2019二季度', '2019三季度'], ['2019一季度', '2019二季度', '2019三季度', '2019四季度']]

        self.user = [['设计部-用户1', '设计部-用户2', '产品部-用户3', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7', '设计部二级部门-用户8'],
                     ['设计部-用户1', '设计部-用户2', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7', '设计部二级部门-用户8'],
                     ['设计部-用户1', '设计部-用户2', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7'],
                     ['设计部-用户1', '销售部-用户5', '同部门下属-用户7']]

        self.field_permission_grant_scope = ['organization_own', 'self_and_subordinate_department_own',
                                             'self_department_own', 'self_own']

        pass


    def check_data_user(self,i =0,_users=['设计部-用户1','销售部-用户5','同部门下属-用户7']):
        current_case = self.title[i]
        time.sleep(2)
        _login = login.Login()
        _login.login(self.userinfo_['username'], self.userinfo_['password'], self.userinfo_['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _result = result.result(self.cookie, self.csrf)
        ##Actual_result输出三个值 图表，中间值，表格
        # 产品销售金额 product_money  产品分类销售额 product_category_money
        Actual_result_all = _result.gole_completion(from_date=self.date_list[i][0], to_date=self.date_list[i][1], type='product_money', dimension='quarter',
                     data='other')
        # # Expected_result输出两个值 中间值，表格
        Expected_result_all =_result.product_amount_get_completion_quarter(_months=self.month[i], _users=_users, _month_view=self._month_view[i])
        # # # 比较图表的统计值是否相同
        Actual_result = Actual_result_all[0]
        # #图表的预期结果和表格的预期结果相同 所以取的是表格预期结果的值
        Expected_result = Expected_result_all[0]
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True:
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case)+'图表的排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case)+'图表的排名' + ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(
                    datetime.datetime.now()))
                f.write(a + '\n')

        ##比较实际中间的统计值和预期中间的统计值是否相同
        Actual_result=Actual_result_all[1]
        Expected_result=Expected_result_all[1]
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True :
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case)+'中间统计排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case)+'中间统计排名' + ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(datetime.datetime.now()))
                f.write(a + '\n')

        #比较表格实际排名和预期排名是否相等
        Actual_result = Actual_result_all[2]
        Expected_result = Expected_result_all[0]
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True:
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case) +'表格排名'+ ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('amount_q.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case) +'表格排名'+ ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(
                    datetime.datetime.now()))
                f.write(a + '\n')

    def payments_amount_baobiao(self):
        _result_count = result_product_amount_quarter()
        for m in range(len(self.field_permission_grant_scope)):
            _login = login.Login()
            _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _Roles = testGetRoles.GetRole(self.cookie, self.csrf)
            _Roles.ding_set_data_authority(self.field_permission_grant_scope[m])
            print(self.field_permission_grant_scope[m])
            for i in range(len(_result_count.date_list)):
                print(self.title[i])
                _result_count.check_data_user(i, _users=self.user[m])



if __name__ == '__main__':
    _result_count =result_product_amount_quarter()
    if os.path.exists('amount_q.txt') ==True:
        os.remove('amount_q.txt')
    #工作台结果对比
    # _result_count.payments_amount_gongzuotai()
    #按季度结果对比
    _result_count.payments_amount_baobiao()
    #测试此方法
    # _result_count.check_data_user()
    #测试此方法
    # _result_count.check_data_first()



