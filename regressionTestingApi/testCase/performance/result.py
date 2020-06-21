# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
from commons import common
import math
import datetime
import os
import codecs
import operator
from commons.const import const
from testCase.login import testLogin as login
# from testCase.performance import result
import random
import string


class result:
    def __init__(self,cookie,csrf):
        self.csrf = csrf
        self.cookie = cookie
#
    # def __init__(self):
    #     self.csrf = ''
    #     self.cookie = ''
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL

        self.response =''
        self.common = common.Common(self.cookie, self.csrf)
        self.userinfo_super = {'username': '15000249334', 'password': 'Ik123456','role':'超管'}
        self.userinfo_user1 = {'username': '15000249334', 'password': 'Ik123456', 'role': '超管'}
        self._username = []
        self._user_department = []
        self.userlist = const.USER
        self.sign_date_list = ['2019-01-31', '2019-03-31', '2019-05-31', '2019-07-31', '2019-09-30', '2019-11-30']
        # 合同关联产品的总金额
        self.add_product_amount_list = [[15, 15], [30, 30], [45, 45], [60, 60], [75, 75], [90, 90],
                                        [105, 105],[120, 120]]

        self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
                                  [220, 230]]
        pass

    def case_1(self):
        self.current_case = 'case 1'
        _login = login.Login()
        print (self.userinfo_super['username'])
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # self.amount_get()
        # self.count_get()
        # self.payments_amount_get(s=8)
        # self.payments_count_get()
        # self.gole(dimension ='department')
        # self.gole_departments()
        # self.sales_goal()
        # self.h5_gole()
        # self.count_get_completion()
        # self.sales_rank()
        # self.gole_department()
        # self.count_get_department()
        # self.count_get_user()
        # self.product_amount_get_user()
        # self.amount_get_department()
        # self.amount_get_user()

    def get_rank_by_dep(self,rank_type,date_type):
        url = self.base_url + 'api/dashboard/department_rank?rank_type=' + rank_type + '&date_type=' + date_type
        body = {}
        response = self.common.get_response_json(url , body ,'get_page')
        print(response)
        rank = []
        department = []
        count_or_amount = []
        for i in range(len(response.json()['rank'])):
            rank.append(response.json()['rank'][i]['ranking'])
            department.append(response.json()['rank'][i]['department_name'])
            count_or_amount.append(response.json()['rank'][i]['count_or_amount'])
        actual_dep_rank = []
        for i in range(len(rank)):
            dep_rank = {
                'date_type': date_type,
                'rank_type' : rank_type,
                'dep':department[i],
                ' rank': rank[i],
                'count_or_amount': count_or_amount[i]
            }
            actual_dep_rank.append(dep_rank)
        print(actual_dep_rank)

    def get_rank_by_user(self,rank_type,date_type):
        url = self.base_url + 'api/dashboard/user_rank?rank_type=' + rank_type + '&date_type=' + date_type
        body = {}
        response  =  self.common.get_response_json(url , body ,'get_page')
        rank = []
        user = []
        count_or_amount = []
        for i in range(len(response.json()['rank'])):
            rank.append(response.json()['rank'][i]['ranking'])
            user.append(response.json()['rank'][i]['user_name'])
            count_or_amount.append(response.json()['rank'][i]['count_or_amount'])
        actual_user_rank = []
        for i in range(len(rank)):
            user_rank = {
                'date_type': date_type,
                'rank_type' : rank_type,
                'dep':user[i],
                ' rank': rank[i],
                'count_or_amount': count_or_amount[i]
            }
            actual_user_rank.append(user_rank)
        print(actual_user_rank)

    def change_to_html(self,a_str):
        html_str = str(a_str)
        html_str = html_str.replace('<\\', '<')
        html_str = html_str[8: -3]
        return html_str
    # 取图表值，中间的统计，表格的排名，如果参数是按照部门则是按部门的值
    # 回款的case1 case2   按用户筛选   取实际结果调用的此方法
    # 按用户 商机数 报表
    # 按部门 商机数 报表
    # 按用户 商机金额 报表的筛选
    # 按部门 商机金额 报表的筛选
    # 按用户 合同数 报表筛选
    # 按部门 合同数 报表筛选
    # 按用户 商机金额 报表的筛选
    # 按部门 合同金额 报表的筛选
    def gole(self, from_date='2019-07-01', to_date='2019-09-30', type='win_count', dimension='user'):
        _common = common.Common(self.cookie, self.csrf)
        # url = self.base_url+'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension='+str(dimension)+'&from_y_m=&to_y_m=&date=current_month&product_id=12579&product_category_id=16828&goal_type='+str(type)+'&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_rank&from_date=' + str(from_date) +'&to_date=' + str(to_date) +'&goal_types%5B0%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D='+str(type)+'&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B3%5D%5B%5D=product_count%23product_id%2311012&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%96%B0%E5%A2%9E%E5%88%86%E7%B1%BB01)&goal_types%5B4%5D%5B%5D=product_category_count%23product_category_id%2318498&goal_types%5B5%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B5%5D%5B%5D=product_money%23product_id%2311012&_=1547546205858'
        url = self.base_url + 'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&from_y_m=&to_y_m=&date=last_month&product_id=12579&product_category_id=16288&goal_type=' + str(
            type) + '&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_rank&from_date=' + str(
            from_date) + '&to_date=' + str(
            to_date) + '&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=result_contract_rank&goal_types%5B1%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=win_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B2%5D%5B%5D=contract_money&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B3%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B4%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B4%5D%5B%5D=contract_count&goal_types%5B5%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B5%5D%5B%5D=product_category_count%23product_category_id%2316288&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B6%5D%5B%5D=product_count%23product_id%238823&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B7%5D%5B%5D=product_money%23product_id%238823&goal_types%5B8%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B8%5D%5B%5D=win_count&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B9%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B10%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B10%5D%5B%5D=product_money%23product_id%2312579&_=1550226613316'

        response = _common.get_response_json(url, '', '')
        print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取图表数值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        print(percentage_data)
        Actual_result = []
        for i in range(len(categories)):
            # 排除等于null的情况
            if percentage_data[i] == 'null':
                percentage_data[i] = 0
            if percentage_data[i] == '':
                percentage_data[i] = 0
            Actual_body = {
                'count': stats_data[i].replace('¥ ', "").replace(',', ""),
                ' user_name': categories[i],
                # 'goal_data': goal_data[i].replace('¥ ', "").replace(',', ""),
                # 'percentage_data': str(round(float(percentage_data[i]), 1))
            }
            # 应该是没有跑数据  会报ValueError: could not convert string to float:
            Actual_result.append(Actual_body)
        print(u'图表的值')
        print(Actual_result)
        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            # print (span)
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                test.append(t[1])
            # print(test)

        totle_gole = [{
            'count': str(test[0]).replace('¥ ', "").replace(',', ""),
            # 'goal_data': str(test[1]).replace('¥ ', "").replace(',', ""),
            # 'percentage_data': str(test[2].split("%")[0])
        }]
        # print (totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)

            test.append(text_list)
        _result_table = []
        for i in range(len(test)):
            count_info = {
                'count': str(test[i][3]).replace('¥ ', "").replace(',', "") + ".0",
                ' user_name': test[i][1],
                # 'goal_data': str(test[i][4]).replace('¥ ', "").replace(',', "") + ".0",
                # 'percentage_data': str(test[i][5].split("%")[0])
            }
            _result_table.append(count_info)
        # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table

    # # # 按部门 产品分类销量 报表
    def gole_d(self, from_date='2019-07-01', to_date='2019-09-30', type='win_count', dimension='user'):
        _common = common.Common(self.cookie, self.csrf)
        url = self.base_url + 'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&from_y_m=&to_y_m=&date=last_month&product_id=&product_category_id=16288&goal_type=' + str(
            type) + '&department_ids=6183%2C6186%2C6187%2C6184%2C6185&user_ids=&include_children_dep=0&controller=' \
                    'statistic_center%2Fsales_goal&action=goal_rank&per_page=20&from_date=' + str(
            from_date) + '&to_date=' + str(
            to_date) + '&_=1550753693872'
        response = _common.get_response_json(url, '', '')
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取图表数值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        print(percentage_data)
        Actual_result = []
        for i in range(len(categories)):
            # 排除等于null的情况
            if percentage_data[i] == 'null':
                percentage_data[i] = 0
            if percentage_data[i] == '':
                percentage_data[i] = 0
            Actual_body = {
                'count': stats_data[i].replace('¥ ', "").replace(',', ""),
                ' user_name': categories[i],
                # 'goal_data': goal_data[i].replace('¥ ', "").replace(',', ""),
                # 'percentage_data': str(round(float(percentage_data[i]), 1))
            }
            # 应该是没有跑数据  会报ValueError: could not convert string to float:
            Actual_result.append(Actual_body)
        print(u'图表的值')
        print(Actual_result)
        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            # print (span)
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                test.append(t[1])
            # print(test)

        totle_gole = [{
            'count': str(test[0]).replace('¥ ', "").replace(',', ""),
            # 'goal_data': str(test[1]).replace('¥ ', "").replace(',', ""),
            # 'percentage_data': str(test[2].split("%")[0])
        }]
        # print (totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)

            test.append(text_list)
        _result_table = []
        for i in range(len(test)):
            count_info = {
                'count': str(test[i][2]).replace('¥ ', "").replace(',', "") + ".0",
                ' user_name': test[i][1],
                # 'goal_data': str(test[i][3]).replace('¥ ', "").replace(',', "") + ".0",
                # 'percentage_data': str(test[i][4].split("%")[0])
            }
            _result_table.append(count_info)
        # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table
    #按用户 产品销量的实际结果调用此方法
    #按用户 产品金额的实际结果调用此方法
    #按部门 产品销量的实际结果调用此方法
    #按用户 产品分类销量  报表
    #按用户 产品分类销售额 报表
    def gole_product(self, from_date='2019-07-01', to_date='2019-09-30', type='win_count', dimension='user'):
        _common = common.Common(self.cookie, self.csrf)
        url =  self.base_url + 'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&from_y_m=&to_y_m=&date=last_month&product_id=12579&product_category_id=16288&goal_type=' + str(
            type) + '' \
                         '&department_ids=6183%2C6186%2C6187%2C6184%2C6185&user_ids=&controller=statistic_center%2Fsales_goal&action=' \
                         'goal_rank&per_page=20&from_date=' + str(
            from_date) + '&to_date=' + str(
            to_date) + '&_=1550740219912'

        response = _common.get_response_json(url, '', '')
        print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取图表数值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        print(percentage_data)
        Actual_result = []
        for i in range(len(categories)):
            # 排除等于null的情况
            if percentage_data[i] == 'null':
                percentage_data[i] = 0
            if percentage_data[i] == '':
                percentage_data[i] = 0
            Actual_body = {
                'count': stats_data[i].replace('¥ ', "").replace(',', ""),
                ' user_name': categories[i],
                # 'goal_data': goal_data[i].replace('¥ ', "").replace(',', ""),
                # 'percentage_data': str(round(float(percentage_data[i]), 1))
            }
            # 应该是没有跑数据  会报ValueError: could not convert string to float:
            Actual_result.append(Actual_body)
        print(u'图表的值')
        print(Actual_result)
        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            # print (span)
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                test.append(t[1])
            # print(test)

        totle_gole = [{
            'count': str(test[0]).replace('¥ ', "").replace(',', ""),
            # 'goal_data': str(test[1]).replace('¥ ', "").replace(',', ""),
            # 'percentage_data': str(test[2].split("%")[0])
        }]
        # print (totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)

            test.append(text_list)
        _result_table = []
        for i in range(len(test)):
            count_info = {
                'count': str(test[i][2]).replace('¥ ', "").replace(',', "") + ".0",
                ' user_name': test[i][1],
                # 'goal_data': str(test[i][3]).replace('¥ ', "").replace(',', "") + ".0",
                # 'percentage_data': str(test[i][4].split("%")[0])
            }
            _result_table.append(count_info)
        # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table

    # 部门 不包含在部门 勾选5个部门的获取实际结果的值
    # 按部门查询   回款的case2  获取报表的实际结果
    # 按部门 产品金额 报表 实际结果
    # 按部门  产品分类销售额 报表
    def gole_department(self, from_date='2019-07-01', to_date='2019-09-30', type='win_count', dimension='user'):
        _common = common.Common(self.cookie, self.csrf)

        url=self.base_url+'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&from_y_m=&to_y_m=&date=last_month&product_id=&product_category_id=&goal_type=' + str(
            type) + '&department_ids=6183%2C6184%2C6185%2C6186%2C6187&' \
                    'user_ids=&include_children_dep=0&controller=statistic_center%2Fsales_goal&action=goal_rank&per_page=20' \
                    '&from_date=' + str(
            from_date) + '&to_date=' + str(
            to_date) + '&_=1550669464523'

        response = _common.get_response_json(url, '', '')
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取图表数值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        print(percentage_data)
        Actual_result = []
        for i in range(len(categories)):
            # 排除等于null的情况
            if percentage_data[i] == 'null':
                percentage_data[i] = 0
            if percentage_data[i] == '':
                percentage_data[i] = 0
            Actual_body = {
                'count': stats_data[i].replace('¥ ', "").replace(',', ""),
                ' user_name': categories[i],
                # 'goal_data': goal_data[i].replace('¥ ', "").replace(',', ""),
                # 'percentage_data': str(round(float(percentage_data[i]), 1))
            }
            # 应该是没有跑数据  会报ValueError: could not convert string to float:
            Actual_result.append(Actual_body)
        # print(u'图表的值')
        # print(Actual_result)
        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            # print (span)
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                test.append(t[1])
            # print(test)

        totle_gole = [{
            'count': str(test[0]).replace('¥ ', "").replace(',', ""),
            # 'goal_data': str(test[1]).replace('¥ ', "").replace(',', ""),
            # 'percentage_data': str(test[2].split("%")[0])
        }]
        # print (totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)

            test.append(text_list)
        _result_table = []
        for i in range(len(test)):
            count_info = {
                'count': str(test[i][2]).replace('¥ ', "").replace(',', "") + ".0",
                ' user_name': test[i][1],
                # 'goal_data': str(test[i][3]).replace('¥ ', "").replace(',', "") + ".0",
                # 'percentage_data': str(test[i][4].split("%")[0])
            }
            _result_table.append(count_info)
        # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table
    # 按用户查询  回款case1 获取报表的实际结果 调用的此方法
    def golePayment(self, from_date='2019-07-01', to_date='2019-09-30', type='win_count', dimension='user'):
        _common = common.Common(self.cookie, self.csrf)
        # url = self.base_url+'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension='+str(dimension)+'&from_y_m=&to_y_m=&date=current_month&product_id=12579&product_category_id=16828&goal_type='+str(type)+'&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_rank&from_date=' + str(from_date) +'&to_date=' + str(to_date) +'&goal_types%5B0%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D='+str(type)+'&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B3%5D%5B%5D=product_count%23product_id%2311012&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%96%B0%E5%A2%9E%E5%88%86%E7%B1%BB01)&goal_types%5B4%5D%5B%5D=product_category_count%23product_category_id%2318498&goal_types%5B5%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B5%5D%5B%5D=product_money%23product_id%2311012&_=1547546205858'
        url = self.base_url + 'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&from_y_m=&to_y_m=&date=last_month&product_id=12579&product_category_id=16288&goal_type=' + str(
            type) + '&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_rank&from_date=' + str(
            from_date) + '&to_date=' + str(
            to_date) + '&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=result_contract_rank&goal_types%5B1%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=win_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B2%5D%5B%5D=contract_money&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B3%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B4%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B4%5D%5B%5D=contract_count&goal_types%5B5%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B5%5D%5B%5D=product_category_count%23product_category_id%2316288&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B6%5D%5B%5D=product_count%23product_id%238823&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B7%5D%5B%5D=product_money%23product_id%238823&goal_types%5B8%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B8%5D%5B%5D=win_count&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B9%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B10%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B10%5D%5B%5D=product_money%23product_id%2312579&_=1550226613316'

        response = _common.get_response_json(url, '', '')
        print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取图表数值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        print(percentage_data)
        Actual_result = []
        for i in range(len(categories)):
            # 排除等于null的情况
            if percentage_data[i] == 'null':
                percentage_data[i] = 0
            if percentage_data[i] == '':
                percentage_data[i] = 0
            Actual_body = {
                'count': stats_data[i].replace('¥ ', "").replace(',', ""),
                ' user_name': categories[i],
                # 'goal_data': goal_data[i].replace('¥ ', "").replace(',', ""),
                # 'percentage_data': str(round(float(percentage_data[i]), 1))
            }
            # 应该是没有跑数据  会报ValueError: could not convert string to float:
            Actual_result.append(Actual_body)
        print(u'图表的值')
        print(Actual_result)
        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            # print (span)
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                test.append(t[1])
            # print(test)

        totle_gole = [{
            'count': str(test[0]).replace('¥ ', "").replace(',', ""),
            # 'goal_data': str(test[1]).replace('¥ ', "").replace(',', ""),
            # 'percentage_data': str(test[2].split("%")[0])
        }]
        # print (totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)

            test.append(text_list)
        _result_table = []
        for i in range(len(test)):
            count_info = {
                'count': str(test[i][3]).replace('¥ ', "").replace(',', "") + ".0",
                ' user_name': test[i][1],
                # 'goal_data': str(test[i][4]).replace('¥ ', "").replace(',', "") + ".0",
                # 'percentage_data': str(test[i][5].split("%")[0])
            }
            _result_table.append(count_info)
        # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table

    def gole_contract_rank(self,from_date='2019-01-01',to_date='2019-01-31',type = 'win_money',dimension ='user'):
        _common=common.Common(self.cookie,self.csrf)
        url =self.base_url+'statistic_center/sales_goal/goal_rank_table?dimension=' + str(dimension) +'&controller=statistic_center%2Fsales_goal&action=goal_rank&date=current_month&from_y_m=&to_y_m=&from_date=' + str(from_date) +'&to_date=' + str(to_date) +'&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=result_contract_rank&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id%238823&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B4%5D%5B%5D=product_money%23product_id%238823&goal_type=result_contract_rank&_=1548236863878'
        response =_common.get_response_json(url,'','')
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(str(soup))
        scopesU = re.findall(r"categories = \[(.*)\]", str(soup))
        scopes = re.findall(r"stats_data = \[(.*)\]", str(soup))
        # 如果用户和排名都不为空 打印排名
        if scopesU and scopes:
            userName = str(scopesU[0]).split(',')
            moneyList = str(scopes[0]).split(',')
            # print('业绩类型是：' + goal_type)
            # print(userName)
            # print(moneyList)
            return  userName,moneyList
        else:
            print('排名为空')

    def sales_goal(self,from_date='2019-07-01',to_date='2019-12-31',type = 'win_money',dimension ='month',date ='next_quarter'):
        _common=common.Common(self.cookie,self.csrf)
        url = self.base_url+'statistic_center/sales_goal/goal_stats_table?utf8=%E2%9C%93&dimension='+str(dimension)+'&product_id=&product_category_id=&goal_type='+str(type)+'&from_y_m=&to_y_m=&date='+str(date)+'&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_stats&from_date='+str(from_date)+'&to_date='+str(to_date)+'&_=1548048822251'
        print (url)
        response =_common.get_response_json(url,'','')
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(str(soup))
        scopesU = re.findall(r"categories = \[(.*)\]", str(soup))
        scopes = re.findall(r"stats_data = \[(.*)\]", str(soup))
        # 如果用户和排名都不为空 打印排名
        if scopesU and scopes:
            userName = str(scopesU[0]).split(',')
            moneyList = str(scopes[0]).split(',')
            # print('业绩类型是：' + goal_type)
            print(userName)
            print(moneyList)
            return  userName,moneyList
        else:
            print('排名为空')

    def gole_departments(self,from_date='2019-01-01',to_date='2019-01-31',type = 'win_count',dimension ='department'):
        #业绩完成度排名按照部门
        _common=common.Common(self.cookie,self.csrf)
        url = self.base_url+'statistic_center/sales_goal/goal_rank_table?utf8=%E2%9C%93&dimension='+str(dimension)+'&from_y_m=&to_y_m=&date=current_month&product_id=11012&product_category_id=16288&goal_type='+str(type)+'&department_id=&user_id=&controller=statistic_center%2Fsales_goal&action=goal_rank&from_date=' + str(from_date) +'&to_date=' + str(to_date) +'&goal_types%5B0%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D='+str(type)+'&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B3%5D%5B%5D=product_count%23product_id%2311012&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%96%B0%E5%A2%9E%E5%88%86%E7%B1%BB01)&goal_types%5B4%5D%5B%5D=product_category_count%23product_category_id%2318498&goal_types%5B5%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B5%5D%5B%5D=product_money%23product_id%2311012&_=1547546205858'
        print (url)
        response =_common.get_response_json(url,'','')
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(str(soup))
        categories = re.findall(r"categories = \[(.*)\]", str(soup))
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))
        value_digit = re.findall(r"value_digit = \[(.*)\]", str(soup))
        # 如果用户和排名都不为空 打印排名
        print(categories)
        print(stats_data)
        print(goal_data)
        print(percentage_data)
        print(value_digit)
        # 如果用户和排名都不为空 打印排名
        # if scopesU and scopes:
        #     userName = str(scopesU[0]).split(',')
        #     moneyList = str(scopes[0]).split(',')
        #     # print('业绩类型是：' + goal_type)
        #     # print(userName)
        #     # print(moneyList)
        #     return  userName,moneyList
        # else:
        #     print('排名为空')

    def gole_quarter(self, from_date='2019-01-01', to_date='2019-06-30', type='contract_count', dimension='quarter',
                     data='current_year'):
        # 业绩目标完成度报表
        _common = common.Common(self.cookie, self.csrf)
        url = self.base_url + 'statistic_center/sales_goal/goal_stats_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&product_id=12579&product_category_id=16288&goal_type=' + str(
            type) + '&from_y_m='+from_date+'&to_y_m='+to_date+'&date=' + data + '&department_ids=&user_ids=&controller=statistic_center%2Fsales_goal&action=goal_stats&from_date=' + str(
            from_date) + '&to_date=' + str(to_date) + '&_=1548048143312'
        # print (url)
        response = _common.get_response_json(url, '', '')
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(str(soup))
        scopesU = re.findall(r"categories = \[(.*)\]", str(soup))
        scopes = re.findall(r"stats_data = \[(.*)\]", str(soup))
        # 如果用户和排名都不为空 打印排名
        result_count = []
        if scopesU and scopes:
            monthes = str(scopesU[0]).split(',')
            dataList = str(scopes[0]).split(',')
            count_info_view = {
                'month': monthes,
                'count': dataList
            }
            result_count.append(count_info_view)
            return result_count
        else:
            print('排名为空')

    # 业绩目标完成度报表
    #test product_id=12579&product_category_id=16288 department_ids=6098  staging product_id=19005&product_category_id=16169department_ids=5923
    def gole_completion(self, from_date='2019-01-01', to_date='2019-03-31', type='contract_money', dimension='month',
                     data='other'):
        _common = common.Common(self.cookie, self.csrf)
        url = self.base_url + 'statistic_center/sales_goal/goal_stats_table?utf8=%E2%9C%93&dimension=' + str(
            dimension) + '&product_id=19005&product_category_id=16169&goal_type=' + str(
            type)+'&from_y_m='+from_date+'&to_y_m='+to_date +'&date=' + data+ '&department_ids=5923&user_ids=&controller=statistic_center%2Fsales_goal&action=goal_stats&from_date=' + str(
            from_date) + '&to_date=' + str(to_date) + '&_=1552986745497'
        # print(url)
        response = _common.get_response_json(url, '', '')
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(str(soup))
        #图标的值
        categories = re.findall(r"categories = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        stats_data = re.findall(r"stats_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        goal_data = re.findall(r"goal_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        percentage_data = re.findall(r"percentage_data = \[(.*)\]", str(soup))[0].replace('"', "").split(",")
        # print(categories,stats_data,goal_data,percentage_data)
        Actual_result=[]
        for i in range(len(categories)):
            count_month_info_view = {
                'month': categories[i],
                'count': str(float(stats_data[i])),
                'goal_data': goal_data[i],
                'percentage_data': str(round(float(percentage_data[i]),1))
            }
            Actual_result.append(count_month_info_view)
        print('图表的值实际结果')
        print(Actual_result)

        # 获取表格的值
        html_str = (response.text.split("\n")[0])
        html_str = html_str.replace("\\n", "")
        new_html_str = self.change_to_html(html_str)
        soup = BeautifulSoup(new_html_str, features="html.parser")
        section_list = soup.find_all('section')
        div_list = section_list[1].find_all('div')
        span_list = div_list[0].find_all('span')
        test = []
        for span in span_list:
            if span.text.strip() == "导出全部":
                print(u'跳过')
            else:
                # print(span.text.strip())
                s = span.text.strip()
                t = s.split("：")
                if len(t)>1:
                    test.append(t[1])
        # print(test)
        totle_gole = [{
            'month': categories[i],
            'count': (test[0]).replace('¥ ', "").replace(',', '')+'.0',
            'goal_data': str(test[1]).replace('¥ ', "").replace(',', "")+'.0',
            'percentage_data': str(test[2].split("%")[0])
        }]
        # print(totle_gole)
        tbody = section_list[1].find_all('tbody')[0]
        test = []
        tr_list = tbody.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            text_list = []
            for td in td_list:
                text_list.append((td.text.strip()))
            # print(text_list)
            test.append(text_list)

        _result_table = []
        for i in range(len(test)):
            count_info = {
                'month': str(test[i][0]).replace('\xa0\xa0', ""),
                'count': str(float(test[i][1].replace('¥ ', "").replace(',', ""))),
                'goal_data': str(test[i][2]).replace('¥ ', "").replace(',', "")+'.0',
                'percentage_data': str(test[i][3].split("%")[0])
            }
            _result_table.append(count_info)
        print('中间的值实际结果')
        print(totle_gole)
        print('表格的值实际结果')
        print(_result_table)
        # # 图表值，中间的统计，表格的排名
        return Actual_result, totle_gole, _result_table


    # def get_response_json(self, url, body, content,token ='e0e277989c505b1e2600091688c0f0be'):
    #     s = requests.session()
    #     s.headers.update({'Accept': 'application/json, text/plain, */*'})
    #     s.headers.update({'Authorization': 'Token token=' + str(token) +',device="dingtalk",version_code="3.13.2"'})
    #     response = s.get(url, data=body)
    #     success_str = u'%s， success， response time： %s' % (content, response.elapsed)
    #     fail_str = u'%s， error' % content
    #     print (s.headers)
    #     if response.status_code not in [200, 204]:
    #         self.response = None
    #         return False
    #     else:
    #         self.response = response
    #         return self.response

    def h5_gole(self,from_date='2019-1',to_date='2019-12',type = 'result_contract_rank',userid ='2225219'):
        url = self.base_url+'api/v2/statistic_center/sales_goal/goal_stats?department_id=&dimension=month&from_y_m=' + str(from_date) +'&goal_type=' + str(type) +'&reset_goals=false&to_y_m='+ str(to_date) +'&user_id=' + str(userid) +''
        print (url)
        response =self.get_response_json(url,'','')
        print (response.content)
        print (response.json()["data"])
        categories = (response.json()["data"]['categories'])
        stats_data = (response.json()["data"]['stats_data'])
        Actual_result =()
        Actual_result =(categories,stats_data)
        print (Actual_result)

    # 首页业绩排名 last_month, quarter
    # 合同回款的case2  case1 取工作台实际结果调用的此方法
    # 产品销售额的工作台
    #  按用户 产品分类销量  工作台
    # 按用户 产品分类销售额 工作台
    # 按用户 商机数 工作台
    # 按用户 商机金额 工作台
    # 按用户 合同数 工作台
    # 按用户 合同金额
    def sales_rank(self,type="product_category_count",scope_unit ="year"):
        _common = common.Common(self.cookie, self.csrf)
        url = self.base_url+'api/dashboard/sales_rank?goal_type='+ str(type) +'%23product_category_id%2316288&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=result_contract_rank&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id%238823&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B4%5D%5B%5D=product_money%23product_id%238823&goal_types%5B5%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B5%5D%5B%5D=win_count&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B6%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B7%5D%5B%5D=product_money%23product_id%2312579&goal_types%5B8%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B8%5D%5B%5D=win_money&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B9%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B10%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B10%5D%5B%5D=product_category_count%23product_category_id%2316288&scope_unit='+ str(scope_unit) +'&include_subordinate=-1&product_category_id=16288&is_count_goal_type=true&is_product_count_about=true&save_params_to_cache=false'
        get_count = []
        response = _common.get_response_json(url, '', '')
        for info in response.json():
            print(info)
            username = info['user_name']
            print(username)
            sales_performance = info['sales_performance']
            # print (sales_performance)
            count_info = {
                'count': str((sales_performance['finished_amount'])),
                ' user_name': username,
                'goal_data': str(sales_performance['goal_amount']),
                'percentage_data': str(sales_performance['goal_percent'])
            }
            get_count.append(count_info)
            # print(get_count)
        return get_count

    def sales_rank_completion(self, type="product_category_count", scope_unit="current_month",Actual_result_month="2019 一月"):
        _common = common.Common(self.cookie, self.csrf)
        #url = self.base_url + 'api/dashboard/sales_goal?goal_type='+type+'&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=contract_rank&goal_types%5B1%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=win_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B2%5D%5B%5D=contract_money&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id%238823&goal_types%5B4%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B4%5D%5B%5D=contract_count&goal_types%5B5%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B5%5D%5B%5D=win_count&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B6%5D%5B%5D=product_category_count%23product_category_id%2316288&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B7%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B8%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B8%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B9%5D%5B%5D=product_money%23product_id%2312579&scope_unit='+scope_unit+'&only_own=&is_count_goal_type=false&is_product_count_about=false&save_params_to_cache=true&has_view_business_goal_perm=true'
        url ='https://ding-test.ikcrm.com/api/dashboard/sales_goal?goal_type=product_category_count%23product_category_id%2316288&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=contract_rank&goal_types%5B1%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=win_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B2%5D%5B%5D=contract_money&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id%238823&goal_types%5B4%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B4%5D%5B%5D=contract_count&goal_types%5B5%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B5%5D%5B%5D=win_count&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B6%5D%5B%5D=product_category_count%23product_category_id%2316288&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B7%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B8%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B8%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B9%5D%5B%5D=product_money%23product_id%2312579&scope_unit=current_month&only_own=&product_category_id=16288&is_count_goal_type=true&is_product_count_about=true&save_params_to_cache=false&has_view_business_goal_perm=true'
        get_count = []
        response = _common.get_response_json(url, '', '')
        goal_amount = response.json()['goal_amount']
        finished_amount = response.json()['finished_amount']
        goal_percent = response.json()['goal_percent']
        count_info = {
            'month': Actual_result_month,
            'count': str(finished_amount),
            'goal_data': str(goal_amount),
            'percentage_data': str(round(goal_percent,1))
        }
        get_count.append(count_info)
        print(u'工作台实际结果')
        print(get_count)
        return get_count

    # 产品的id和产品分类id不能同时传 只能另写一个产品的
    #按用户  产品数量的工作台实际结果调用此方法
    def sales_rank_product(self, tpye="product_count", scope_unit="year"):
        _common = common.Common(self.cookie, self.csrf)
        # url = self.base_url + 'api/dashboard/sales_rank?goal_type=' + str(tpye) + '%23product_category_id%2316288&goal_types%5B0%5D%5B%5D=%E5%90%88%E5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=result_contract_rank&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal_types%5B2%5D%5B%5D=contract_count&goal_types%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id%238823&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B4%5D%5B%5D=product_money%23product_id%238823&goal_types%5B5%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B5%5D%5B%5D=win_count&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B6%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B7%5D%5B%5D=product_money%23product_id%2312579&goal_types%5B8%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B8%5D%5B%5D=win_money&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B9%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B10%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B10%5D%5B%5D=product_category_count%23product_category_id%2316288&scope_unit=' + str(scope_unit) + '&include_subordinate=-1&product_category_id=16288&is_count_goal_type=true&is_product_count_about=true&save_params_to_cache=false'

        url =self.base_url+'api/dashboard/sales_rank?goal_type=' + str(
            tpye) + '%23product_id%2312579&goal_types%5B0%5D%5B%5D=%E5%90%88%E' \
                    '5%90%8C%E5%9B%9E%E6%AC%BE%E9%87%91%E9%A2%9D&goal_types%5B0%5D%5B%5D=' \
                    'result_contract_rank&goal_types%5B1%5D%5B%5D=%E5%90%88%E5%90%8C%E9%87%91%E9%A2%9D&goal_types' \
                    '%5B1%5D%5B%5D=contract_money&goal_types%5B2%5D%5B%5D=%E5%90%88%E5%90%8C%E6%95%B0&goal' \
                    '_types%5B2%5D%5B%5D=contract_count&goal_types' \
                    '%5B3%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F' \
                    '(csdcsd)&goal_types%5B3%5D%5B%5D=product_count%23product_id' \
                    '%238823&goal_types%5B4%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(csdcsd)&goal_types%5B4%5D%5B%5D=product_money%23product_id%238823&goal_types%5B5%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E6%95%B0&goal_types%5B5%5D%5B%5D=win_count&goal_types%5B6%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B6%5D%5B%5D=product_count%23product_id%2312579&goal_types%5B7%5D%5B%5D=%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E4%BA%A7%E5%93%8101)&goal_types%5B7%5D%5B%5D=product_money%23product_id%2312579&goal_types%5B8%5D%5B%5D=%E8%B5%A2%E5%8D%95%E5%95%86%E6%9C%BA%E9%87%91%E9%A2%9D&goal_types%5B8%5D%5B%5D=win_money&goal_types%5B9%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E5%94%AE%E9%A2%9D(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B9%5D%5B%5D=product_category_money%23product_category_id%2316288&goal_types%5B10%5D%5B%5D=%E4%BA%A7%E5%93%81%E5%88%86%E7%B1%BB%E9%94%80%E9%87%8F(%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB01)&goal_types%5B10%5D%5B%5D=product_category_count%23product_category_id%2316288&scope_unit='+str(scope_unit)+'&include_subordinate=-1&product_id=12579&is_count_goal_type=true&is_product_count_about=true&save_params_to_cache=false'
        get_count = []
        response = _common.get_response_json(url, '', '')
        print(response.json())
        for info in response.json():
            # print (info)
            username = info['user']['name']
            # print (username)
            sales_performance = info['sales_performance']
            print(sales_performance)
            count_info = {
                'count': str((sales_performance['finished_amount'])),
                ' user_name': username,
                # 'goal_data': str(sales_performance['goal_amount']),
                # 'percentage_data': str(sales_performance['goal_percent'])
            }
            get_count.append(count_info)
            print(get_count)
        return get_count

    def percent(self,num):
        num = num * 100
        num = round(num*10)/10.0
        return float(num)
        # return str(num) + '%'

    def amount_get(self):
        contracts_amount = []
        month_list =[1, 3, 5, 7, 9, 11]
        for a in range(6):
            for i in range(8):
                if self.userlist[i]['usertitle'] == '主辅部门-用户6' and a >=3:
                    id = 1
                else:
                    id = 0
                amount = (self.total_amount_list[i][0] + self.total_amount_list[i][1]) * 2 * (a+1)
                amount_info = {
                    'month': month_list[a],
                    'amount': amount,
                    ' user_name': self.userlist[i]['usertitle'],
                    ' user_department': self.userlist[i]['departments'][id],
                }
                contracts_amount.append(amount_info)
        return(contracts_amount)

# 获取按用户排名的数据
    def add_product_amount_get(self):
        add_product_amount = []
        month_list = [1, 3, 5, 7, 9, 11]
        for a in range(6):
            for i in range(8):
                if self.userlist[i]['usertitle'] == '主辅部门-用户6' and a >= 3:
                    id = 1
                else:
                    id = 0
                add_product_amount1 = (self.add_product_amount_list[i][0] + self.add_product_amount_list[i][1]) * (
                            a + 1) * 2
                amount_info = {
                    'month': month_list[a],
                    'amount': add_product_amount1,
                    ' user_name': self.userlist[i]['usertitle'],
                    'user_department': self.userlist[i]['departments'][id],
                }
                # print ()
                add_product_amount.append(amount_info)
        # print(add_product_amount)
        return add_product_amount
    # 产品 按用户查询
    # 按用户 报表查询  产品金额的预期结果调用此方法
    #  按用户 产品分类销售额 报表
    def product_amount_get_user(self,_months=[1, 2, 3]):
        self.user_info()
        payments_amount_case2_list = result.add_product_amount_get(self)
        result_count = []
        # 定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[' user_name'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' user_name': i,
                # 'goal_data': str(float(len(_months) * 1000)),
                # 'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            # 获取赢单数 目标数  完成率
            a = 0
            for j in result_count:
                count = j['count']
                a = a + count
            # 封装赢单数 目标数  完成率为list形式
            # print
        count_total = {
            'count': str(int(a)),
            # 'goal_data': str(int(len(self.userlist) * len(_months) * 1000)),
            # 'percentage_data': str(self.percent(a / (len(self.userlist) * len(_months) * 1000)))
        }
        result_total.append(count_total)
        # 排序
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        # 把count格式变回str类型
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                # 'goal_data': item['goal_data'],
                # 'percentage_data': item['percentage_data']
            }
            count.append(count_info)
        print(count, result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count
    # 按部门 产品金额 报表 预期结果
    # 按部门  产品分类销售额 报表
    def product_amount_get_department(self,_months=[1], _user_department=['设计部']):
        self.user_info()
        payments_amount_case2_list = result.amount_get(self)
        result_count = []
        result_total = []
        for i in self._user_department:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[
                    ' user_department'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' user_name': i,
                # 'goal_data': str(float(len(_months) * 1000)),
                # 'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            # 获取产品销售额 目标数  完成率
            a = 0
            # 获取总产品销售额
        for j in result_count:
            count = j['count']
            a = a + count
        count_total = {
            'count': str(int(a)),
            # 'goal_data': str(int(len(self._user_department)* len(_months) * 1000)),
            # 'percentage_data': str(self.percent(a / (len(self._user_department)* len(_months) * 1000)))
        }
        # 封装产品销售额 目标数  完成率为list形式
        result_total.append(count_total)
        # 中间的统计值
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                # 'goal_data': item['goal_data'],
                # 'percentage_data': item['percentage_data']
            }
            # 表格的值
            count.append(count_info)
        # print(count,result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count

    def payments_amount_get(self,s=2):
         #case1： s =2；case2： s=8
        contracts_amount = []
        month_list =[1, 3, 5, 7, 9, 11]
        for a in range(6):
            for i in range(8):
                # U1_name = self.userlist[i]['usertitle']
                if self.userlist[i]['usertitle'] == '主辅部门-用户6':
                    for b in range(2):
                        id = b
                        amount = (self.total_amount_list[i][0] + self.total_amount_list[i][1]) * s * (a + 1)
                        amount_info = {
                            'month': month_list[a],
                            'amount': amount,
                            ' user_name': self.userlist[i]['usertitle'],
                            ' user_department': self.userlist[i]['departments'][id],
                        }
                        contracts_amount.append(amount_info)
                        # print (amount_info)
                else:
                    id = 0
                    amount = (self.total_amount_list[i][0] + self.total_amount_list[i][1]) * s * (a+1)
                    amount_info = {
                        'month': month_list[a],
                        'amount': amount,
                        ' user_name': self.userlist[i]['usertitle'],
                        ' user_department': self.userlist[i]['departments'][id],
                    }
                    contracts_amount.append(amount_info)
            # print (s)
        # print (contracts_amount)
        return contracts_amount
    # 按用户查询   回款case1 获取预期结果调用此的方法
    def payments_amount_get_user_case1(self, _months=[1, 2, 3]):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self,s=2)
        # print(payments_amount_case2_list)
        result_count = []
        # 定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[' user_name'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' user_name': i,
                # 'goal_data': str(float(len(_months) * 1000)),
                # 'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            # print(result_count)
            # #获取赢单数 目标数  完成率
            a = 0
            for j in result_count:
                count = j['count']
                a = a + count
            # 封装赢单数 目标数  完成率为list形式
            # print
        count_total = {
            'count': str(int(a)),
            # 'goal_data': str(int(len(self.userlist) * len(_months) * 1000)),
            # 'percentage_data': str(self.percent(a / (len(self.userlist) * len(_months) * 1000)))
        }
        result_total.append(count_total)
        # 排序
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        ##把count格式变回str类型
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                # 'goal_data': item['goal_data'],
                # 'percentage_data': item['percentage_data']
            }
            count.append(count_info)
        ##返回中间的统计值,表格的排名
        return result_total, count
    # 回款的case2  按用户筛选   取预期结果调用的此方法
    def payments_amount_get_user_case2(self, _months=[1, 2, 3]):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self, s=8)
        result_count = []
        # 定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[' user_name'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' user_name': i,
                # 'goal_data': str(float(len(_months) * 1000)),
                # 'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            # 获取赢单数 目标数  完成率
            a = 0
            for j in result_count:
                count = j['count']
                a = a + count
            # 封装赢单数 目标数  完成率为list形式
            # print
        count_total = {
            'count': str(int(a)),
            # 'goal_data': str(int(len(self.userlist) * len(_months) * 1000)),
            # 'percentage_data': str(self.percent(a / (len(self.userlist) * len(_months) * 1000)))
        }
        result_total.append(count_total)
        # 排序
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        # 把count格式变回str类型
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                # 'goal_data': item['goal_data'],
                # 'percentage_data': item['percentage_data']
            }
            count.append(count_info)
        print(count, result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count
    # 按部门查询  回款case1的预期结果调用此方法
    def payments_amount_get_department_case1(self, _months=[1], _user_department=['设计部']):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self,s=2)
        result_count = []
        result_total = []
        for i in self._user_department:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[
                    ' user_department'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' department': i,
                'goal_data': str(1000) + '.0',
                'percentage_data': str(self.percent(c / 1000))
            }
            result_count.append(count_info)
            # 获取产品销售额 目标数  完成率
            a = 0
            # 获取总产品销售额
        for j in result_count:
            count = j['count']
            a = a + count
        count_total = {
            'count': str(int(a)),
            'goal_data': str(int(len(self._user_department) * len(_months) * 1000)),
            'percentage_data': str(self.percent(a / (len(self._user_department) * 1000)))
        }
        # 封装产品销售额 目标数  完成率为list形式
        result_total.append(count_total)
        # 中间的统计值
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' department'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            # 表格的值
            count.append(count_info)
        # print(count,result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count
    #  按部门查询   回款的case2  获取预期结果调用的此方法
    def payments_amount_get_department_case2(self, _months=[1], _user_department=['设计部']):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self,s=8)
        result_count = []
        result_total = []
        for i in self._user_department:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[
                    ' user_department'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' department': i,
                'goal_data': str(float(len(_months)) * 1000),
                'percentage_data': str(self.percent(c/(len(_months) * 1000)))
            }

            result_count.append(count_info)

            # 获取产品销售额 目标数  完成率
            a = 0
            # 获取总产品销售额
        #中间值计算
        for j in result_count:
            count = j['count']
            a = a + count
        count_total = {
            'count': str(int(a)),
            'goal_data': str(int(len(self._user_department) * len(_months) * 1000)),
            'percentage_data': str(self.percent(a / (len(self._user_department) * len(_months)* 1000)))
        }

        # 封装产品销售额 目标数  完成率为list形式
        result_total.append(count_total)
        # 中间的统计值
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' department'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            # 表格的值
            count.append(count_info)
        # print(count,result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count

    def count_get(self,s =2):
        #商机合同数量s=2，  产品销量s=2  产品销量分类销量,s=4
        contracts_count = []
        month_list =[1, 3, 5, 7, 9, 11]
        for a in range(6):
            for i in range(8):
                if self.userlist[i]['usertitle'] == '主辅部门-用户6' and a >=3:
                    id = 1
                else:
                    id = 0
                count = s * (i+1)
                count_info = {
                    'month': month_list[a],
                    'count': count,
                    ' user_name': self.userlist[i]['usertitle'],
                    ' user_department': self.userlist[i]['departments'][id],
                }
                contracts_count.append(count_info)
        return contracts_count

    def user_info(self):
        _user_department1 = []
        for i in self.userlist:
            _usertitle = i['usertitle']
            # print (_usertitle)
            self._username.append(_usertitle)
            department = i['departments'][0]
            _user_department1.append(department)
        for i in _user_department1:
            if i not in self._user_department:
                self._user_department.append(i)
        # print(self._username)
        # print(self._user_department)
#wang   按部门排名的商机 合同 金额
# 按部门 商机金额 预期结果
# 按部门 合同金额 预期结果
    def amount_get_department(self, _months=[1], _user_department=['设计部']):
        self.user_info()
        payments_amount_case2_list = result.amount_get(self)
        result_count = []
        result_total = []
        for i in self._user_department:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[
                    ' user_department'] == i:
                    # if payments_amount_case2['month'] in (1,3) and payments_amount_case2[' user_department'] == i:
                    # if _months.__contains__(payments_amount_case2['month']) and _user_department.__contains__(payments_amount_case2[' user_department']):
                    a = payments_amount_case2['amount']
                    c = c + a
            print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' department': i,
                'goal_data': str(1000) + '.0',
                'percentage_data': str(self.percent(c / 1000))
            }
            result_count.append(count_info)
            # 获取赢单数 目标数  完成率
            a = 0
            # 获取总赢单数
        for j in result_count:
            count = j['count']
            a = a + count
        count_total = {
            'count': str(int(a)),
            'goal_data': str(int(len(self._user_department) * 1000)),
            'percentage_data': str(self.percent(a / (len(self._user_department) * 1000)))
        }
        #封装赢单数 目标数  完成率为list形式
        result_total.append(count_total)
        # 中间的统计值
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' department'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            # 表格的值
            count.append(count_info)
        # print(count,result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count
 # 按用户 产品销售额工作台的预期结果
# 按用户 商机金额 报表的筛选
# 按用户 商机金额 工作台的预期结果
# 按用户 合同金额 报表的筛选
    def amount_get_user(self,_months=[1]):
        self.user_info()
        payments_amount_case2_list = result.amount_get(self)
        result_count = []
        # 定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _months.__contains__(payments_amount_case2['month']) and payments_amount_case2[' user_name'] == i:
                    a = payments_amount_case2['amount']
                    c = c + a
            # print(c, i, _months)
            count_info = {
                'count': (float(c)),
                ' user_name': i,
                'goal_data': str(float(len(_months) * 1000)),
                'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            # 获取赢单数 目标数  完成率
            a = 0
            for j in result_count:
                count = j['count']
                a = a + count
            # 封装赢单数 目标数  完成率为list形式
            # print
        count_total = {
            'count': str(int(a)),
            'goal_data': str(int(len(self.userlist) * len(_months) * 1000)),
            'percentage_data': str(self.percent(a / (len(self.userlist) * len(_months) * 1000)))
        }
        result_total.append(count_total)
        # 排序
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        # 把count格式变回str类型
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            count.append(count_info)
        # print (count,result_total)
        # 返回中间的统计值,表格的排名
        return result_total, count
#wang 按部门获取数量
    # 按部门 产品销量的预期结果调用此方法
    # # # 按部门 产品分类销量 报表
    # 按部门 商机数 报表
    # 按部门 合同数 报表筛选
    def count_get_department(self, _months=[7, 8, 9],s=2):
        self.user_info()
        #获取部门的值
        count_get_list = self.count_get(s)
        result_count = []
        result_total=[]
        for i in self._user_department:
            c = 0
            for count_get in count_get_list:
                if _months.__contains__(count_get['month']) and count_get[' user_department'] == i:
                    #获取部门的值
                    a = count_get['count']
                    c = c + a
            print(c, i, _months)

            count_info = {
                'count': (float(c)),
                ' department': i,
                'goal_data': str(float(len(_months) * 1000)),
                'percentage_data': str(self.percent(c / (len(_months) * 1000)))
            }
            result_count.append(count_info)
            #获取赢单数 目标数  完成率
            a = 0
            #获取总赢单数
        for j in result_count:
            count=j['count']
            a=a+count
        count_total = {
            'count': str(int(a)),
            'goal_data': str(float(len(self._user_department) * len(_months) * 1000)).replace('.0',''),
            'percentage_data': str(self.percent(a / (len(self._user_department) * len(_months) * 1000)))

        }
        ##封装赢单数 目标数  完成率为list形式
        result_total.append(count_total)
        #中间的统计值
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        count = []
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' department'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            #表格的值
            count.append(count_info)
        # print(count,result_total)
        #返回中间的统计值,表格的排名
        return result_total,count
#wang按用户获取数量
    #   按用户查询   回款的case1的工作台预期结果调用的此方法
    #   按用户查询   回款的case2的工作台的预期结果调用的此方法
    #   按用户查询   产品数量预期结果调用的此方法
    #   按用户 产品分类销量  报表
    #   按用户 产品分类销量  工作台
    #   按用户 产品分类销售额 工作台
    #   按用户 商机数 报表
    #   按用户 商机数 工作台
    #   按用户 合同数 报表筛选
    #   按用户 合同数 工作台
    def count_get_user(self, _months=[1, 2, 3],s=2):
        self.user_info()
        count_get_list = self.count_get(s)
        result_count = []
        #定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for count_get in count_get_list:
                if _months.__contains__(count_get['month']) and count_get[' user_name'] == i:
                    a = count_get['count']
                    # print (i, a)
                    c = c + a
            # print (c,i,_months)
            count_info ={
                'count': (float(c)),
                ' user_name': i,
                'goal_data': str(float(len(_months)*1000)),
                'percentage_data': str(self.percent(c/(len(_months)*1000)))
                }
            result_count.append(count_info)
            # 获取赢单数 目标数  完成率
            a = 0
            for j in result_count:
                count = j['count']
                a = a + count
        #封装赢单数 目标数  完成率为list形式
        # print
        count_total = {
            'count': str(int(a)),
            'goal_data': str(int(len(self.userlist)*len(_months) * 1000)),
            'percentage_data': str(self.percent(a/(len(self.userlist)*len(_months) * 1000)))
        }
        result_total.append(count_total)
        #排序
        result_count = sorted(result_count, key=lambda item: item['count'], reverse=True)
        #把count格式变回str类型
        count =[]
        for item in result_count:
            count_info = {
                'count': str(item['count']),
                ' user_name': item[' user_name'],
                'goal_data': item['goal_data'],
                'percentage_data': item['percentage_data']
            }
            count.append(count_info)
        # print (count,result_total)
        #返回中间的统计值,表格的排名
        return result_total,count

    #所有的数量业绩类型  完成度报表 跑这个方法 可以确认数据统计的正确性 页面交互需要看按季度和按年的维度统计是否按月份显示的
    def count_get_completion(self, _months=[1,2,3],_users=['设计部-用户1', '设计部-用户2', '产品部-用户3', '设计部子部门-用户4', '销售部-用户5', '主辅部门-用户6', '同部门下属-用户7', '设计部二级部门-用户8'],_month_view=['2019 一月','2019 二月','2019 三月'],s=2):
        self.user_info()
        payments_amount_case2_list = result.count_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['count']
                c = c + a
        count_info_view = {
            'month':_month_view[-1],
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000))+'.0',
            'percentage_data': str(self.percent(c /(len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        # print(result_totle)
        result_month = []
        for i in range(len(_months)):
            h = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and payments_amount_case2['month'] == \
                        _months[i]:
                    a = payments_amount_case2['count']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                count_month_info_view = {
                    'month': str(_month_view[i]),
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * 1000))+'.0',
                    'percentage_data': str(self.percent(h / (len(_users) * 1000)))
                }
            result_month.append(count_month_info_view)
        print(u'中间值预期结果')
        print(result_totle)
        print(u'表格&图表预期结果')
        print(result_month)
        return result_month, result_totle

        # 产品金额 产品分类销售额 完成度报表 跑这个方法 可以确认数据统计的正确性 页面交互需要看按季度和按年的维度统计是否按月份显示的

    def count_get_completion_quarter(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                               _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],
                                               _month_view=['2019一季度'], s=2):
        self.user_info()
        payments_amount_case2_list = result.count_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['count']
                c = c + a
        count_info_view = {
            'month':_month_view[-1],
            'count': str((float(c))),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print(u'中间值预期结果')
        print(result_totle)

        quarter = self.quarter_get(_months)
        # print(quarter)
        result_quarter = []
        for i in range(len(quarter)):
            h = 0
            # print(quarter[i])
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and quarter[i].__contains__(
                        payments_amount_case2['month']):
                    a = payments_amount_case2['count']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                count_quarter_info_view = {
                    'month': _month_view[i],
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * len(quarter[i]) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * len(quarter[i]) * 1000)))
                }
            result_quarter.append(count_quarter_info_view)
        print(u'图表&表格预期结果')
        print(result_quarter)
        return result_quarter, result_totle
    # 数量 按年 完成度
    def count_get_completion_year(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                           _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'], _month_view=['2019年'], s=2):
        self.user_info()
        payments_amount_case2_list = result.count_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['count']
                c = c + a
        count_info_view = {
            'month': str(_month_view).replace('[', '').replace(']', '').replace("'", ''),
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print(u'预期结果')
        print(result_totle)
        return result_totle

    #合同金额 商机金额 完成度 按月
    def contract_amount_get_completion(self, _months=[1],_users=['设计部-用户1'], _month_view=['2019 一月']):
        self.user_info()
        amount_list = result.amount_get(self)
        print(amount_list)
        result_totle = []
        c = 0
        for amount_info in amount_list:
            if _months.__contains__(amount_info['month']) and _users.__contains__(amount_info[' user_name']):
                a = amount_info['amount']
                c = c + a
        # print(c,  _months)
        count_info_view = {
            'month': _month_view[-1],
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000))+'.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)

        result_month = []
        for i in range(len(_months)):
            h = 0
            for amount_info in amount_list:
                if _users.__contains__(amount_info[' user_name']) and amount_info['month'] == _months[i]:
                    a = amount_info['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                amount_month_info_view = {
                    'month': str(_month_view[i]),
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * 1000)))
                }
            result_month.append(amount_month_info_view)
        print(u'图表&表格预期结果')
        print(result_month)
        print(u'中间值预期结果')
        print(result_totle)
        return result_month,result_totle
    # 合同金额 商机金额 按季度
    def contract_amount_get_completion_quarter(self, _months=[1, 2, 3, 4, ], _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],  _month_view=['2019一季度']):
        self.user_info()
        payments_amount_case2_list = result.amount_get(self)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': _month_view[-1],
            'count': str((float(c))),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print('中间值预期结果')
        print(result_totle)

        quarter = self.quarter_get(_months)
        result_quarter = []
        for i in range(len(quarter)):
            h = 0
            # print(quarter[i])
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and quarter[i].__contains__(
                        payments_amount_case2['month']):
                    a = payments_amount_case2['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                count_quarter_info_view = {
                    'month': _month_view[i],
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * len(quarter[i]) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * len(quarter[i]) * 1000)))
                }
            result_quarter.append(count_quarter_info_view)
        print('图表&表格预期结果')
        print(result_quarter)
        return result_quarter, result_totle
    # 合同 商机金额完成度 按年
    def contract_amount_get_completion_year(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],_month_view=['2019年']):
        self.user_info()
        payments_amount_case2_list = result.amount_get(self)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': str(_month_view).replace('[', '').replace(']', '').replace("'", ''),
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print(u'预期结果')
        print(result_totle)
        return result_totle

    # 合同回款case1 s=2  case2 s=8
    def payments_amount_get_completion(self, s=2,_months=[1, 2, 3], _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],
                                       _month_view=['2019一月', '2019二月', '2019三月'], ):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': _month_view[-1],
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000))+'.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)

        result_month = []
        for i in range(len(_months)):
            h = 0
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and payments_amount_case2['month'] == \
                        _months[i]:
                    a = payments_amount_case2['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                amount_month_info_view = {
                    'month': str(_month_view[i]),
                    'count': str(float(h)),
                    'goal_data': str(int(len(_users)* 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * 1000)))
                }
            result_month.append(amount_month_info_view)
        print(u'图表&表格预期结果')
        print(result_month)
        print(u'中间值预期结果')
        print(result_totle)
        return result_month, result_totle

    # 合同回款case1 s=2  case2 s=8
    def payments_amount_get_completion_quarter(self, _months=[1, 2, 3, 4, ], _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],
                                               _month_view=['2019一季度'],s=2):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': _month_view[-1],
            'count': str((float(c))),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print('中间值预期结果')
        print(result_totle)

        quarter = self.quarter_get(_months)
        result_quarter = []
        for i in range(len(quarter)):
            h = 0
            # print(quarter[i])
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and quarter[i].__contains__(
                        payments_amount_case2['month']):
                    a = payments_amount_case2['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                count_quarter_info_view = {
                    'month': _month_view[i],
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * len(quarter[i]) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * len(quarter[i]) * 1000)))
                }
            result_quarter.append(count_quarter_info_view)
        print('图表&表格预期结果')
        print(result_quarter)
        return result_quarter, result_totle
        # 合同 商机金额完成度 按年

    def payments_amount_get_completion_year(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                            _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'], _month_view=['2019年'],s=2):
        self.user_info()
        payments_amount_case2_list = result.payments_amount_get(self, s)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': str(_month_view).replace('[', '').replace(']', '').replace("'", ''),
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print('预期结果')
        print(result_totle)
        return result_totle



    ##  产品金额 完成度 按月
    def product_amount_get_completion(self, _months=[1],_users=['设计部-用户1', '销售部-用户5',  '同部门下属-用户7'], _month_view=['2019 一月']):
        self.user_info()
        amount_list = result.add_product_amount_get(self)
        result_totle = []
        c = 0
        for amount_info in amount_list:
            if _months.__contains__(amount_info['month']) and _users.__contains__(amount_info[' user_name']):
                a = amount_info['amount']
                c = c + a
        # print(c,  _months)
        count_info_view = {
            'month': _month_view[-1],
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)

        result_month = []
        for i in range(len(_months)):
            h = 0
            for amount_info in amount_list:
                if _users.__contains__(amount_info[' user_name']) and amount_info['month'] == _months[i]:
                    a = amount_info['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                amount_month_info_view = {
                    'month': str(_month_view[i]),
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * 1000)))
                }
            result_month.append(amount_month_info_view)
        print(u'图表&表格预期结果')
        print(result_month)
        print(u'中间值预期结果')
        print(result_totle)
        return result_month, result_totle


    ## 产品金额 产品分类金额 完成度 按季度
    def product_amount_get_completion_quarter(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                               _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],
                                               _month_view=['2019一季度'], s=2):
        self.user_info()
        payments_amount_case2_list = result.add_product_amount_get(self)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': _month_view[-1],
            'count': str((float(c))),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print('中间值预期结果')
        print(result_totle)

        quarter = self.quarter_get(_months)
        result_quarter = []
        for i in range(len(quarter)):
            h = 0
            # print(quarter[i])
            for payments_amount_case2 in payments_amount_case2_list:
                if _users.__contains__(payments_amount_case2[' user_name']) and quarter[i].__contains__(
                        payments_amount_case2['month']):
                    a = payments_amount_case2['amount']
                    h = h + a
                    # print(a,h, payments_amount_case2['month'],payments_amount_case2[' user_name'])
                count_quarter_info_view = {
                    'month': _month_view[i],
                    'count': str((float(h))),
                    'goal_data': str(int(len(_users) * len(quarter[i]) * 1000)) + '.0',
                    'percentage_data': str(self.percent(h / (len(_users) * len(quarter[i]) * 1000)))
                }
            result_quarter.append(count_quarter_info_view)
        print('图表&表格预期结果')
        print(result_quarter)
        return result_quarter, result_totle

    ## 产品销售额  产品分类销售额 完成度 按年
    def product_amount_get_completion_year(self, _months=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                            _users=['设计部-用户1', '销售部-用户5', '同部门下属-用户7'],
                                            _month_view=['2019年']):
        self.user_info()
        payments_amount_case2_list = result.add_product_amount_get(self)
        result_totle = []
        c = 0
        for payments_amount_case2 in payments_amount_case2_list:
            if _months.__contains__(payments_amount_case2['month']) and _users.__contains__(
                    payments_amount_case2[' user_name']):
                a = payments_amount_case2['amount']
                c = c + a
        count_info_view = {
            'month': str(_month_view).replace('[', '').replace(']', '').replace("'", ''),
            'count': str(float(c)),
            'goal_data': str(int(len(_users) * len(_months) * 1000)) + '.0',
            'percentage_data': str(self.percent(c / (len(_users) * len(_months) * 1000)))
        }
        result_totle.append(count_info_view)
        print(u'预期结果')
        print(result_totle)
        return result_totle


    def count_get_month_user(self, _months=[1, 2, 3], s=2):
        self.user_info()
        count_get_list = self.count_get(s)
        result_count = []
        # 定义汇总的list变量
        result_total = []
        for i in self._username:
            c = 0
            for count_get in count_get_list:
                if _months.__contains__(count_get['month']) and count_get[' user_name'] == i:
                    a = count_get['count']
                    c = c + a
            print (c,i,_months)

    def quarter_get(self,_months):
        month = []
        a = []
        b = []
        c = []
        d = []
        for i in range(len(_months)):
            if _months[i] in [1, 2, 3]:
                a.append(_months[i])
            if _months[i] in [4, 5, 6]:
                b.append(_months[i])
            if _months[i] in [7, 8, 9]:
                c.append(_months[i])
            if _months[i] in [10, 11, 12]:
                d.append((_months[i]))
        if len(a) > 0:
            month.append(a)
        if len(b) > 0:
            month.append(b)
        if len(c) > 0:
            month.append(c)
        if len(d) > 0:
            month.append(d)
        # print(month)
        return month


if __name__ == '__main__':
    _contracts_amount =result()
    _login = login.Login()
    _login.login(_contracts_amount.userinfo_user1['username'], _contracts_amount.userinfo_super['password'], _contracts_amount.userinfo_super['role'])
    print(_contracts_amount.userinfo_super['username'])
    _contracts_amount.cookie = _login.cookie
    _contracts_amount.csrf = _login.csrf
    _contracts_amount.contract_amount_get_completion()
    ## 实际结果
    _contracts_amount.gole_completion()
    # 完成度排名
    # _contracts_amount.payments_amount_get_completion_month(s=2)
    # _contracts_amount.payments_amount_get_completion_quarter(s=2)
    # _contracts_amount.payments_amount_get_completion_year(s=2)
    # _contracts_amount.sales_rank_completion()
    # # _contracts_amount.count_get_user()
    # _contracts_amount.count_get_user()
    # _contracts_amount.sales_rank()
    # _contracts_amount.amount_get_user()
    # _contracts_amount.h5_gole()
    # _contracts_amount.amount_get_department()
    # _contracts_amount.count_get_completion()