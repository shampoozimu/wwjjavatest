# -*- coding: utf-8 -*-
__author__ = 'lwang'

from bs4 import BeautifulSoup
import json
import os
import requests
import random
import datetime
# import MySQLdb
import re
from decimal import Decimal as D
from APITest0524.co.const import const

class Login:
    def __init__(self):
        #'https://e.ikcrm.com/
        # self.base_url = base_url
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.username = ''
        self.password = ''
        self.response = ''
        self.csrf1 = ''
        self.given_cookie = ''  # 用于存储人工指定的cookie，一旦设置后，就不使用页面内获取的cookie
        self.authorization = ''
        self.lead_ids = []
        self.user_id = ''
        self.customers_id =[]
        self.customers_id1 = ''
        self.contracts_id = ''
        self.sql_host = 'rdscbq34656z0ix59br0.mysql.rds.aliyuncs.com'
        self.products_id = ''
        self.expense_id = ''
        self.expense_id_list = []
        self.expense_accounts_id = ''
        self.payment_id_list = []
        self.payslip_stats_list = []
        self.commission_rules_id = []
        self.performance_indicator_id  = ''
        self.stations_id = ''
        self.revisit_logs_list = []
       # 某些post或是get时要求header里带的信息，应该是一个帐户对应于唯一一个
        # 格式类似于：'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'
        pass

    def get_csrf_and_cookie(self):
        response = requests.get(self.base_url)
        html_str = response.content
        soup = BeautifulSoup(html_str,"html.parser")
        #<meta name="csrf-token" content="jSoItF5xtWY0xvgUR5iIk7uphiyHGuCcVrAY8hBci42WBHPSxABibG07sMc0aSdnODraUrZ14rfd2uFEytfy+Q==" />
        self.csrf = soup.find(attrs={"name": "csrf-token"})['content']
        self.cookie = response.headers['Set-Cookie']

    def get_csrf_by_html(self, html_str):
        soup = BeautifulSoup(html_str,"html.parser")
        #print u'wnagle%s' %soup
        csrf = soup.find(attrs={"name": "csrf-token"})['content']
        if len(csrf):
            self.csrf = csrf
            # print self.csrf

    def get_html(self, url, content):
        s = requests.session()
        if len(self.given_cookie):
            s.headers.update({'Cookie': self.given_cookie})
        else:
            s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'text/html, application/xhtml+xml'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        response = s.get(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            # print fail_str
            # print u'status code： %s' % response.status_code
            return False
        else:
            if response.headers['Set-Cookie']:
                self.cookie = response.headers['Set-Cookie']
            self.response = response
            #每次刷新页面后，更新token
            #print response.text
            self.get_csrf_by_html(response.text)
            #print success_str
            #result_list = re.findall(r'''<meta name="csrf-token" content="(.*?)" />''', string=response.text)
            #<meta name="csrf-token" content="Rs6HThAWr6F1MdrlkEU5MahJmB9QE2ef6oDBjtTbU7Wq3/4gZCFczbMKhv2aHg7Osc/h7dlSn7UJ7cohW5NaUQ==" />
            #print result_list[0]
            return True

    def get_csrf_by_home_html(self):
        url = self.base_url
        success = self.get_html(url, 'get csrf by home html')
        # path = os.paht.join(os.get(), "co", "cookie.txt")
        # print (path)
        path = 'D:\SVN\\TestAutomation\\APITest0524\\co\\cookie.txt'
        f = open (path, 'r+')
        a = str(self.cookie +'\n'+ self.csrf)
        f.write(a)
        return success

    def login(self, username, password):
        if len(self.cookie) == 0:
            self.get_csrf_and_cookie()
        if len(self.cookie) == 0:
            print ('get csrf and cookie error')
            return
        self.username = username
        self.password = password

        url = self.base_url2
        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'user[login]': username,
            'user[password]': password,
            'user[remember_me]': 0,
            'commit': '登 录'
        }

        s = requests.session()
        s.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        s.headers.update({'Accept-Encoding': 'gzip, deflate'})
        s.headers.update({'Accept-Language': 'zh-CN,zh;q=0.8'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'Cookie': self.cookie})
        response = s.post(url=url, data=body)
        # print response.status_code
        print ('login response status code')
        # print response.status_code
        if response.status_code == 200:
            print ('login success')
            self.cookie  = response.headers['Set-Cookie']
            #print self.cookie
        else:
            print ('login error')
        return response.status_code

if __name__ == "__main__":
    a_login =Login()
    # print a_login.base_url
    # print a_login.base_url2
    a_login.login(13701649176,111111)
    a_login.get_csrf_by_home_html()
    print (a_login.cookie)
    print (a_login.csrf)



