# -*- coding: utf-8 -*-
import datetime
import os
import codecs
import operator
from commons.const import const
from testCase.login import testLogin as login
from testCase.performance import result
import time
from testCase.roles import testGetRoles


class result_contract_amount_month:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.dimension1 = 'user'
        self.dimension2 = 'department'
        self.Actual_result =""
        ##  用户3
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456','role':'超管'}
        ##  用户1
        self.userinfo_ = {'username': '15000249334', 'password': 'Ik123456', 'role': '普通管理员'}

        self.date_list = [['2019-01-01', '2019-01-31'], ['2019-03-01', '2019-03-31'], ['2019-05-01', '2019-05-31'],
                          ['2019-07-01', '2019-07-31'], ['2019-09-01', '2019-09-30'], ['2019-11-01', '2019-11-30'],
                          ['2019-01-01', '2019-03-31'], ['2019-04-01', '2019-06-30'], ['2019-07-1', '2019-09-30'],
                          ['2019-10-01', '2019-12-31'], ['2019-01-01', '2019-12-31'], ['2019-01-01', '2019-06-30'],
                          ['2019-07-01', '2019-12-31'], ['2019-04-01', '2019-08-31']]


        self.month = [[1], [3], [5], [7], [9], [11], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                      [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8]]

        self.title = [['1月合同金额'],
                      ['3月合同金额'],
                      ['5月合同金额'],
                      ['7月合同金额'],
                      ['9月合同金额'],
                      ['11月合同金额'],
                      ['第一季度合同金额'],
                      ['第二季度合同金额'],
                      ['第三季度合同金额'],
                      ['第四季度合同金额'],
                      ['本年合同金额'],
                      ['上半年合同金额'],
                      ['下半年合同金额'],
                      ['4~8月合同金额']
                      ]

        self.date = [['other'],
             ['current_month'],
             ['other'],
             ['other'],
             ['other'],
             ['other'],
             ['current_quarter'],
             ['next_quarter'],
             ['other'],
             ['other'],
             ['current_year'],
             ['last_half_year'],
             ['next_half_year'],
             ['other']
             ]

        self._month_view = [['2019一月'], ['2019三月'], ['2019五月'], ['2019七月'], ['2019九月'], ['2019十一月'],
                            ['2019一月', '2019二月', '2019三月'],
                            ['2019四月', '2019五月', '2019六月'], ['2019七月', '2019八月', '2019九月'],
                            ['2019十月', '2019十一月', '2019十二月'],
                            ['2019一月', '2019二月', '2019三月', '2019四月', '2019五月', '2019六月', '2019七月', '2019八月',
                             '2019九月', '2019十月', '2019十一月', '2019十二月'],
                            ['2019一月', '2019二月', '2019三月', '2019四月', '2019五月', '2019六月'],
                            ['2019七月', '2019八月', '2019九月', '2019十月', '2019十一月', '2019十二月'],
                            ['2019四月', '2019五月', '2019六月', '2019七月', '2019八月']]

        self.user = [['设计部-用户1', '设计部-用户2', '产品部-用户3', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7', '设计部二级部门-用户8'],
            ['设计部-用户1', '设计部-用户2', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7','设计部二级部门-用户8'],
                   ['设计部-用户1', '设计部-用户2', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7'] ,
                   ['设计部-用户1', '销售部-用户5', '同部门下属-用户7']]

        self.field_permission_grant_scope = ['organization_own','self_and_subordinate_department_own','self_department_own','self_own']
        ## 工作台的参数
        self.date_list_first = [
            ['current_month'],
            ['current_quarter'],
            ['last_half_year'],
            ['next_half_year'],
            ['current_year']
        ]

        self.month_list_first = [
            [3],
            [1, 2, 3],
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ]
        self.title_list_first = [['2019三月'],
                                 ['2019本季度'],
                                 ['2019上半年'],
                                 ['2019下半年'],
                                 ['2019年']
                                 ]
        self._month_view_first = [
            ['2019三月'],
            ['2019本季度'],
            ['2019上半年'],
            ['2019下半年'],
            ['2019年']
        ]

        pass

    def check_data_user(self, i=0, _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7']):
        current_case = self.title[i]
        time.sleep(1)
        _login = login.Login()
        _login.login(self.userinfo_['username'], self.userinfo_['password'], self.userinfo_['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _result = result.result(self.cookie, self.csrf)
        # Actual_result输出三个值 图表，中间值，表格
        #合同金额contract_money  商机金额win_money
        Actual_result_all = _result.gole_completion(from_date=self.date_list[i][0], to_date=self.date_list[i][1], type='win_money', dimension='month',
                     data=self.date[i][0])
        # Expected_result输出两个值 中间值，表格
        Expected_result_all =_result.contract_amount_get_completion(_months=self.month[i], _users=_users, _month_view=self._month_view[i])
        # # 比较图表的统计值是否相同
        Actual_result = Actual_result_all[0]
        # #图表的预期结果和表格的预期结果相同 所以取的是表格预期结果的值
        Expected_result = Expected_result_all[0]
        s = len(Actual_result)
        for i in range(s):
            test_result = operator.eq(Expected_result[i], Actual_result[i])
            if test_result == True:
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case)+'图表的排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+str(str(current_case)+'图表的排名' + ': '  "is wrong, expected_result:" + str(
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
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
                a = str(_users)+'\n'+str(str(current_case)+'中间统计排名' + ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
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
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case) +'表格排名'+ ': '  "is right " + str(datetime.datetime.now()))
                f.write(a + '\n')
            else:
                f = codecs.open('contract_amount.txt', 'a', 'utf-8')
                a =str(_users)+'\n'+ str(str(current_case) +'表格排名'+ ': '  "is wrong, expected_result:'\n'" + str(
                    Expected_result[i]) + "Actual_result:'\n'" + str(Actual_result[i]) + ',' + str(
                    datetime.datetime.now()))
                f.write(a + '\n')

#工作台的对比
    def check_data_first(self,i=0,_users=['设计部-用户1', '销售部-用户5',  '同部门下属-用户7']):
        current_case = self.title_list_first[i]
        time.sleep(1)
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _Roles = testGetRoles.GetRole(self.cookie, self.csrf)
        for m in range(len(self.field_permission_grant_scope)):
            ### 设置用户的角色必须是普通管理员的角色
            _Roles.ding_set_data_authority(self.field_permission_grant_scope[m])
            print(self.field_permission_grant_scope[m])

            _login = login.Login()
            _login.login(self.userinfo_['username'], self.userinfo_['password'], self.userinfo_['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf

            _result = result.result(self.cookie, self.csrf)
            Actual_result = _result.sales_rank_completion(type="contract_money", scope_unit=self.date_list_first[i][0])
            Actual_result[0]['month']=self.title_list_first[i][0]
            Actual_result_list=[]
            Actual_result_month=[]
            Actual_result_month.append(Actual_result[0]['month'])
            Actual_result_new={
                'month': Actual_result_month,
                'amount':Actual_result[0]['count'],
                'goal_data':Actual_result[0]['goal_data'],
                'percentage_data':Actual_result[0]['percentage_data']
            }
            Actual_result_list.append(Actual_result_new)
            print(Actual_result_list)

            Expected_result_all = _result.gongzuotai_contract_amount_get_completion(_months=self.month_list_first[i], _users=_users, _month_view = self._month_view_first[i])
            print(Expected_result_all)

            s = len(Expected_result_all)
            for i in range(s):
                test_result = operator.eq(Actual_result_list[i], Expected_result_all[i])
                print(test_result)
                if test_result == True:
                    f = codecs.open('contract_number.txt', 'a', 'utf-8')
                    a = str(str(current_case)+'工作台对比' + ': '  "is right " + str(datetime.datetime.now()))
                    f.write(a + '\n')
                else:
                    f = codecs.open('contract_number.txt', 'a', 'utf-8')
                    a = str(str(current_case)+'工作台对比' + ': '  "is wrong, expected_result:'\n'" + str(
                        Expected_result_all[i]) + "Actual_result:'\n'" + str(Actual_result_list[i]) + ',' + str(
                        datetime.datetime.now()))
                    f.write(a + '\n')


    def payments_amount_baobiao(self):
        _result_count = result_contract_amount_month()
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

    # 工作台结果对比
    def payments_amount_gongzuotai(self):
        _result_count = result_contract_amount_month()
        for i in range(len(self.month_list_first)):
            for j in range(len(self.user)):
                # print(self.user[j])
               _result_count.check_data_first(i,_users=self.user[j])


if __name__ == '__main__':
    _result_count =result_contract_amount_month()
    if os.path.exists('contract_amount.txt') ==True:
        os.remove('contract_amount.txt')
    #工作台结果对比
    # _result_count.payments_amount_gongzuotai()
    # 按部门结果对比
    _result_count.payments_amount_baobiao()
    #测试此方法
    # _result_count.check_data_user()
    #测试此方法
    # _result_count.check_data_first()



