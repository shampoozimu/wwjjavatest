# -*- coding: utf-8 -*-
__author__ = 'lwang'

import requests
from commons.const import const
from commons import common

class Login:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.uid = ''
        self.token =''
        pass


    def login(self, username, password,role):
        self.username = username
        self.password = password
        url = self.base_url2
        body = {
            'login': username,
            'password': password,
        }
        s = requests.session()
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'Content-Type': 'application/json'})
        response = s.post(url, data=None, json=body)
        print(response.json())
        self.uid=response.json()['auth']['uid']
        self.token=response.json()['auth']['token']


if __name__ == "__main__":
    a_Login =Login()
    a_Login.login("13701649175","111111","1234567")
    # a_Login.uc_login("13701649175","111111","1234567")
    # a_Login.AppUrls()
    # a_Login.cook_get()
    # a_Login.get_ticket()
    # a_Login.uc_lixiao_login('4500785')
