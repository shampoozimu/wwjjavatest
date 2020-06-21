# -*- coding: utf-8 -*-
__autotest__ = 'InterfaceAutomationTest'

import codecs
import os
from testCase.login import testLogin as login
from commons.const import const
from testCase.reportCenter.ProductReport import ProductReport
from testCase.basicdata import testAdd as testAdd



class Main:
    def __init__(self):
        self.uid = ''
        self.token = ''

if __name__ == "__main__":
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    for userinfo in const.USER:
        # _login = login.Login()
        # _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
        uid ='9c133f68c8d44354f3db'
        token ='fd9c740897d6a7946a09446c818eee'
        main = Main()
        main.uid =uid
        main.token =token
        # main.uid = _login.uid
        # main.token = _login.token

        # 基础数据
        _ProductReport =ProductReport(main.uid,main.token)
        _ProductReport.case_1()#库存明细

