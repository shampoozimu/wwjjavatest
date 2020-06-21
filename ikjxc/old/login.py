# -*- coding: utf-8 -*-
__author__ = 'lwang'

import re
import io
from BeautifulSoup import BeautifulSoup
import json
import requests
import os

def get_csrf_and_cookie():
    url = "http://test.ikjxc.com/users/sign_in?show_all_version=1"
    response = requests.get(url)
    html_str = response.content
    print html_str
    soup = BeautifulSoup(html_str)
    csrf = soup.find(attrs={"name": "csrf-token"})['content']
    cookie = response.headers['set-cookie']
    print csrf
    return csrf, cookie

def login(username, password):
    csrf, cookie = get_csrf_and_cookie()
    if len(csrf) == 0:
        print 'get csrf error'
        return

    url = "http://test.ikjxc.com/users/sign_in"

    body = {
        'utf8': '✓',
        'authenticity_token': csrf,
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
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    s.headers.update({'Cookie': cookie})
    response = s.post(url=url, data=body)
    print response.content

    print response.status_code

def get_response_json(self, url, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.get(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print response.text
            print success_str
            return True




if __name__ == "__main__":
    get_csrf_and_cookie()
    login('15600000000', '111111')
