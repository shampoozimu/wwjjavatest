
__author__ = 'Sally Wang'

from bs4 import BeautifulSoup
import json
import requests
import random
import datetime
import os
# import MySQLdb
import re
from decimal import Decimal as D
import codecs

class Common:
    def __init__(self):
        #'https://e.ikcrm.com/
        # self.csrf = csrf
        # self.cookie = cookie
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
        pass

    def post_json_response_pc(self, url,body,cookie,csrf,content):
        # post方法返回json
        s = requests.session()
        s.headers.update({'Cookie':cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        # s.headers.update({'Content-Type': 'application/json; charset=UTF-8'})
        #form_json=JSON.
        # print s.headers["Content-Type"]
        # print s.headers
        # print body
        response = s.post(url, data=body)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        # print response.status_code
        if response.status_code not in [200, 204]:
            self.response = None
            return 10000
            print (fail_str)
            print (u'status code： %s' % response.status_code)
            print (fail_str)
            return False

        else:
            self.response = response
            return self.response.json()["code"]


    def post_response_json(self, url, body,token, content):
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/json; charset=UTF-8'})
        s.headers.update({'Authorization': token })
        body = body.encode("utf-8")
        response = s.post(url, data=body)
        # print (s.headers)
        response = s.post(url, data=body)
        response_str = u'%s， response， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            return 100000
        else:
            self.response = response
            # print ('123445678')
            # print (self.response.json())
        print(type(self.response.content))
        return self.response.json()

    def get_response_json(self, url, body,token, content):
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/json; charset=UTF-8'})
        s.headers.update({'Authorization': token })
        response = s.get(url, data=body)
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            return 100000
        else:
            self.response = response

            return self.response.json()["code"]

    def post_response_form(self, url,cookie,csrf, body, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Cookie': cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.post(url, data=body)
        response_str = u'%s， response， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        self.check_status_code(response.status_code,200,content,response)
        # print url
        if response.status_code not in [200, 204]:
            self.response = None
            return False
        else:
            self.response = response
            return self.response

    def put_response_json(self, url, body, content):
        # put方法返回json
        s = requests.session()
        if len(self.given_cookie):
            s.headers.update({'Cookie': self.given_cookie})
        else:
            s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
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
        s = requests.session()
        if len(self.given_cookie):
            s.headers.update({'Cookie': self.given_cookie})
        else:
            s.headers.update({'Cookie': self.cookie})
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
            print (response.text)
            # print (response_str)
            return self.response

    def get_response_json(self, url,body,token, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/json; charset=UTF-8'})
        s.headers.update({'Authorization': token})
        response = s.get(url,data=body)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        self.check_status_code(response.status_code,200,content, response)
        if response.status_code not in [200, 204]:
            self.response = None
            # print (fail_str)
            # print (u'status code： %s' % response.status_code)
            return False
        else:
            self.response = response
        return self.response.json()["code"]

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

    def check_same(self, base_value1, base_value2):
        base = D(str(base_value1)) - D(str(base_value2))

        if abs(base) < D(0.01):
            return True
        else:
            return False

    def cookie_and_csfr(self):
        # f = open('D:\SVN\APITest0524\co\cookie.txt', 'a+')
        f = open('D:\SVN\\TestAutomation\\APITest0524\\co\\cookie.txt', 'r+')
        # path = os.path.join(os.getcwd(), "co", "cookie.txt")
        # f = open(path,"a+")
        index = 0
        line0 = None
        line1 = None
        for line in f:
            if index == 0:
                line0 = line
            elif index == 1:
                line1 = line
            else:
                return
            index += 1
        # print line0
        # print line1
        line0 = line0.split('\n')[0]
        # csrf = line1
        return line0,line1

    def get_today_str_yymmddhhmm(self):
        today = datetime.datetime.now()
        return today.strftime('%Y-%m-%d %H:%M')

    def get_today_str(self):
        today = datetime.datetime.now()
        return today.strftime('%Y-%m-%d %H:%M:%S')

    def get_random_int(self, max_num):
        tmp = random.randint(0, max_num)
        if tmp < max_num:
            return tmp
        else:
            return tmp - 1

if __name__ == "__main__":
    a_commom=Common()
    cookie ="_vcooline_ikcrm_production_ikstaging.ikcrm.com_session=ZFZ3TlFtKzRZc0Y2WGVrZ05wd2FrRnp4OVRvTzdjWGE0Y1YyRSt5N3RuL1o2WXRHNEptUkpJc1VTTEFIVUlCR3c0K25YVFFhY05QSU5WQjJpc0hma1ZUM21TTEszU2ZyOW5uRWs3WTdlV3dXWSt1Z0lJeGlaeHpXb3BKK0w1Y1lpeVZRdm8xdnlLSkxQczJpUVFSZ1BLb3FRVUJxUEM5djAzSXFnNDRObUppMmtYYUNnVEpPY3FHeFJmY2dZcTNydEJra3d1QXBaM2xPR3NmR0ttOW1OTU10OWF4YWZhNzdDRmlIekN5SEhSRzZpa0N6VHV4bXo3VWlHdW5sNEliQzlYVTg2WU13ZmhHK09SNFRkRkh4V013VEhiZ0Q3RkEyT2ZlWWxaZ0ZCNXF5ZnRFWkFFMmExMFF3Q2R3SU1USDNKUW5sa2hLQ0dNdnVJUnZWZzd2RThBPT0tLTMvWEVBcm1LSFVkaldEbEUrTldnbGc9PQ%3D%3D--478d2b8b1ec4c6bde7c4ba69296daea983b48669; domain=.ikcrm.com; path=/; expires=Sun, 26 Aug 2018 09:03:14 -0000; HttpOnly"
    csrf ="ivQUm0OX4r6sn6VpIMh+vxFDVVKlxa2TOf6Ptr5swxYvSFT1Ntk1LQ9M4Uqb/z+X5soYMEJrzWXpQ3H1i2KaQw=="
    body ={'setting_key': 'lead', 'settings[lead][enabled]': '0'}
    url ="http://ikstaging.e.ikcrm.com/settings/duplicates/switch.json"
    content="1234"
    a_commom.post_json_response_pc(url,body,cookie,csrf,content)
