#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from xlutils.copy import copy
import xlrd
import xlwt
import os
from co.const import const
from co.json_utils import JsonUtils

# reload(sys)
# sys.setdefaultencoding('utf8')

class Data_Get():
    def __init__(self):
        self.H5_URL = const.H5_BASE_URL_TEST
        self.PC_URL = const.BASE_URL
        self.dict ={}
        self.table=""
        self.list_data =[]


    def openxls(self):
        # # 打开excel
        # path =os.path.join(os.getcwd(), "datasource","TestInput.xls")
        # path= os.path.join(os.get(),"datasource","TestInput.xls")
        path = "D:\\\Test\\\APITest\\datasource\\TestInput.xls"
        # print path
        data = xlrd.open_workbook(path)
        # # 打开结果保存excel
        newnrows =0
        # for y in range(0,1):
        newnrows = newnrows;
        # 打开excel中的sheet（第二张表格）
        table = data.sheets()[0]
        # 获取到有效数据的行数
        nrows = table.nrows
        nrows =int(nrows)
        # print nrows
        # self.dict["nrows"] = nrows
        # 获取有效数据的列数
        ncols = table.ncols
        disP = {}
        # print ncols, nrows

        for x in range(1, nrows):
            self.dict = {}
            #获取某一行的所有数据
            row = table.row_values(x)
            xls_id = row[0]
            self.dict["xls_id"] = int(xls_id)
            method = row[1]
            self.dict["method"] = method
            name = row[2]
            self.dict["Modular"] = name
            token = row[4]
            self.dict["token"] = token
            Expected_results = row[6]
            # Expected_results =Expected_results.replace("'", '"')
            # Expected_results = json.loads(json.dumps(Expected_results))
            # Expected_results = json.loads(Expected_results)
            # print('============')
            # print(type(Expected_results))
            Expected_results = JsonUtils.toOKStr(Expected_results)
            print(Expected_results)
            Expected_results = json.loads(Expected_results)
            print(Expected_results.items())
            self.dict["Expected_results"] = Expected_results
            print(type(self.dict))
            # method = row[1]
            if method == "login":
                user = int(row[3])
                self.dict["user"] = user
                password =int(row[5])
                self.dict["password"] = password
                # self.list_data.append(self.dict)
            else:
                if method == "post_pc":
                    url = row[3]
                    # url转换为由bytes转化为str
                    #url = bytes.decode(url)
                    url = self.PC_URL + url
                    self.dict["url"] = url
                else:
                    url1 = row[3]
                    url1 = self.H5_URL + str(url1)
                    self.dict["url"] = url1
                body = row[5]
                self.dict["body"] = body
            self.list_data.append(self.dict)
        print (self.list_data)
        return self.list_data


if __name__ == "__main__":
    a_APIGetAdList =Data_Get()
    a_APIGetAdList.openxls()
