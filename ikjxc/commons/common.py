# -*- coding: utf-8 -*-
__author__ = 'Sally Wang'

from bs4 import BeautifulSoup
import requests
import random
import datetime
# import MySQLdb
import re
from decimal import Decimal as D
import codecs

class Common:
    def __init__(self,uid,token):
        self.uid = uid
        self.token = token
        self.response =''
        pass


    def post_response_json(self, url, body, content):
        # post方法返回json
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'Authorization':'Token token=%s, uid=%s' %(self.token,self.uid)})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.post(url, data=body)
        # print(response.status_code)
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            return False
        else:
            self.response = response
            # print(response.json())
            return response

    def put_response_json(self, url, body, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'Authorization': 'Token token=%s, uid=%s' % (self.token, self.uid)})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.put(url, data=body)
        response_str = u'%s， response， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        self.check_status_code(response.status_code,200,content,response)
        if response.status_code not in [200, 204]:
            self.response = None
            return False
        else:
            self.response = response
            return self.response

    def delete_response_json(self, url, body, content):
        #需要修改
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.delete(url, data=body)
        fail_str = u'%s， error' % response.text
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            print (fail_str)
            print (u'status code： %s' % response.status_code)
            return False
        else:
            self.response = response
            # print (response.text)
            # print response_str
            return self.response

    def get_response_json(self, url, body, content,):
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'Authorization': 'Token token=%s, uid=%s' % (self.token, self.uid)})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        response = s.get(url, data=body)
        # print(response.status_code)
        # print(s.headers)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            # print fail_str
            # print u'status code： %s' % response.status_code
            return False
        else:
            self.response = response
            return self.response.json()

    def get_tomorrow_srt_yymmddhhmm(self):
        today = datetime.datetime.now()
        delta  = datetime.timedelta(days=1)
        tomorrow = today + delta
        return tomorrow.strftime('%Y-%m-%d %H:%M')

    def check_status_code(self, real_code, expect_code, print_content, response):
        if self.check_same(real_code, expect_code):
            f = codecs.open('status_code_ok.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': '+ print_content + " status_code is right " + str(real_code) + '  ' +  str( expect_code)
            f.write(a + '\n')
            f.close()
        else:
            f = codecs.open('status_code.txt','a','utf-8')
            a = str(self.get_today_str()) + ': '+ response.text + print_content+ " status_code is wrong " + str(real_code) + '  ' +  str( expect_code)
            f.write(a + '\n')
            f.close()

    def check_data(self, base_value1, base_value2, print_content):
        if self.check_same(base_value1, base_value2):
            f = codecs.open('status_code_ok.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': '+ print_content + "  is right " + str(base_value1) + '  ' +  str( base_value2)
            f.write(a + '\n')
            f.close()
        else:
            f = codecs.open('status_code.txt','a','utf-8')
            a = str(self.get_today_str()) + ': '+ print_content+ "  is wrong " + str(base_value1) + '  ' +  str( base_value1)
            f.write(a + '\n')
            f.close()

    def check_same(self, base_value1, base_value2):
        base = D(str(base_value1)) - D(str(base_value2))
        if abs(base) < D(0.01):
            return True
        else:
            return False

    def check_string(self, base_value1, base_value2, print_content):
        if self.check_same_string(base_value1, base_value2):
            f = codecs.open('status_code_ok.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': ' + print_content + "  is right " + str(base_value1) + '  ' + str(
                base_value2)
            f.write(a + '\n')
            f.close()
        else:
            f = codecs.open('status_code.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': ' + print_content + "  is wrong " + str(base_value1) + '  ' + str(
                base_value1)
            f.write(a + '\n')
            f.close()

    def check_same_string(self, base_value1, base_value2):
        if str(base_value1) == str(base_value2):
            return True
        else:
            return False

    def check_string(self, base_value1, base_value2, print_content):
        if self.check_same_string(base_value1, base_value2):
            f = codecs.open('status_code_ok.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': ' + print_content + "  is right " + str(base_value1) + '  ' + str(
                base_value2)
            f.write(a + '\n')
            f.close()
        else:
            f = codecs.open('status_code.txt', 'a', 'utf-8')
            a = str(self.get_today_str()) + ': ' + print_content + "  is wrong " + str(base_value1) + '  ' + str(
                base_value1)
            f.write(a + '\n')
            f.close()

    def check_same_string(self, base_value1, base_value2):
        if str(base_value1) == str(base_value2):
            return True
        else:
            return False

    def get_today_str_yymmddhhmm(self):
        today = datetime.datetime.now()
        return today.strftime('%Y-%m-%d %H:%M')

    def get_today_str(self):
        today = datetime.datetime.now()
        #print today
        #print today.strftime('%Y-%m-%d %H:%M:%S')
        return today.strftime('%Y-%m-%d %H:%M:%S')

    def get_random_int(self, max_num):
        tmp = random.randint(0, max_num)
        if tmp < max_num:
            return tmp
        else:
            return tmp - 1