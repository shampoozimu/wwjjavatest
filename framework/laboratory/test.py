import json
import math
from enum import Enum, unique, IntEnum
import itertools
from functools import reduce

import arrow

# @unique
# class Gender(Enum):
#     MALE = '男', '阳刚之力'
#     FEMALE = '女', '柔顺之美'
#
#     def __init__(self, cn_name, desc):
#         self._cn_name = cn_name
#         self._desc = desc
#
#     @property
#     def desc(self):
#         return self._desc
#
#     @property
#     def cn_name(self):
#         return self._cn_name
#
#
# # 访问FEMALE的name
# print('FEMALE的name:', Gender.FEMALE.name)
# # 访问FEMALE的value
# print('FEMALE的value:', Gender.FEMALE.value)
# # 访问自定义的cn_name属性
# print('FEMALE的cn_name:', Gender.FEMALE.cn_name)
# # 访问自定义的desc属性
# print('FEMALE的desc:', Gender.FEMALE.desc)


#

# self._http_session.headers.update({'X-CSRF-Token': self.csrf})
# self._http_session.headers.update({'Cookie': self.cookie})
import random

from component.interface import DynamicEnum, IWrapper


#
# class TestTest:
#     @classmethod
#     def set_up(cls, **kwargs):
#         [cls.__pr for k, v in kwargs.items()]
#         return cls
#
# aaa = {"a": 1, "ffv": 9}
# bbb = TestTest.set_up(**aaa);
# print(bbb)

#  里程：A：100km；B：1000km；C：1万km；D：10万km
#  年份：A：1年；B：2年；C：5年；D：10年以上
#  评级：里程和年份两者取大
#
#  生成随机数据，要求ABCD四个档次基本平均分布

# x  100,1000,10000,100000
# 10^x^2
# x = random.uniform(0, 2)
# print()


# print(set(["c","a","b","b","c"]))

# js = {"su":{"ge":{"de":1}}}
# path = ["su","ge","de"]
# # path.insert(0,js)
# aa= reduce(lambda x,y:x[y] ,[js,*path])
# print([js,*path])
# print(aa)

from operator import methodcaller


a = 0
b=3
c = a or b
print(c)




