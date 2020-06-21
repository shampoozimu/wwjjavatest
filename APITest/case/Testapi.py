#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import unittest
import ddt
from co import common
from co import datas
from co import login
import json

@ddt.ddt
class Test(unittest.TestCase):
    # def __init__(self):
    #     self.cookie = ''
    #     self.csrf =''

    def setUp(self):
        print ("start!")

    def tearDown(self):
        print ("end!")

    testData =datas.Data_Get().openxls()
    print (u"testData%s" % testData)
    @ddt.data(*testData)
    def test_api(self,data):
        '''测试用例'''
        print (u"当前测试数据ID%s" % data["xls_id"])
        s=common.Common()
        r=login.Login()

        if  data["method"] == "post":
            code = s.post_response_json(data["url"], data["body"], data["token"],data["Modular"])
            # str(code)
            print(code)
            print(data["Expected_results"])
            # self.assertIn(str(code),data["Expected_results"])
            # self.assertIn(data["Expected_results"],str(code))
            assert set(data["Expected_results"].items()).issubset(set(code.items()))

        elif data["method"] == "get":
            code = str(s.get_response_json(data["url"], data["body"],data["token"],data["Modular"]))
            # print code
            self.assertEqual(code, data["Expected_results"])

        elif data["method"] == "delete":
            code = s.delete_response_json(data["url"], data["body"],data["token"],data["Modular"])
            self.assertEqual(code, data["Expected_results"])

        elif data["method"] == "put":
            code = s.put_response_json(data["url"], data["body"],data["token"],data["Modular"])
            self.assertEqual(code, data["Expected_results"])

        elif data["method"] == "post_pc":
            token = s.cookie_and_csfr()
            body = ast.literal_eval(data["body"])
            code = s.post_json_response_pc(data["url"], body,token[0],token[1],data["Modular"])
            code = int(code)
            self.assertEqual(code, data["Expected_results"])

        elif data["method"] == "login":
            print (data["user"],data["password"])
            code =r.login(data["user"],data["password"])
            self.assertEqual(code, data["Expected_results"])
            r.get_csrf_by_home_html()
            # print r.cookie
            # print r.csrf
        else:
            pass



if __name__ == "__main__":
    unittest.main()

