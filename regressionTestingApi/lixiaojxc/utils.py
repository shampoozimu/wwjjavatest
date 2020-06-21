import logging
from calendar import monthrange
from datetime import datetime, timedelta
from os import path

import pandas, numpy
# 通用功能模块
# 审批人类型
from lixiaojxc.pojo import EnumStatus, EnumSale
from testCase.component.oauth import BaseOauth, Accept, ContentType, Header, UcDeploy
from testCase.component.utils import Arrays


class Oauth(BaseOauth):
    # 新增业务
    def apply(self):
        logging.info("新增%s：%s" % (self._business.enum_type.name, self._business.number))
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        self.set_authorization(token=self.token, uid=self.uid)
        url = "%s/api/%s.json" % (self._str_domain, self._business.plural)
        self.http_response = self._http_session.post(url, data=self._business.apply(self.user))
        self._business.id = self.get_json_property("sale", "id")
        return self._assert_response()

    # 审批业务
    def approve(self, enum_status):
        logging.info("审批%s：%s" % (self._business.enum_type.name, self._business.number))
        self._set_head(Accept.JSON, ContentType.FORM, Header.X_REQUESTED_WITH)
        self.set_authorization(token=self.token, uid=self.uid)
        url = "%s/api/%s/%s.json" % (self._str_domain, self._business.plural, self._business.id)
        self.http_response = self._http_session.put(url, data=self._business.approve(enum_status))
        return self._assert_response()


class DingdingDeploy(Oauth):
    def login(self, user):
        self.user = user
        self.token = self.user.token
        self.uid = self.user.uid
        self.get(self._str_domain + "/dingtalk/sessions/new", body={"token": self.user.token, "uid": self.user.uid})
        self.cookie = self.get_cookies()
        self._set_head(Accept.HTML, ContentType.FORM)
        self.get(self._str_domain + "/dashboard")
        self.csrf = self.get_csrf()
        return self


class Statistic:
    def __init__(self, workbook, worksheet):
        # # 转换成二位数组
        # self.lis_provider = Arrays(list_provider).dual_vector_foil()
        # # 数据格式标准化
        # self.lis_provider = [serialize(prov).get() for prov in self.lis_provider]
        # # 数组-字典转换成字典-数组
        # self.dict_provider = self.__list_to_dict(self.lis_provider)
        # # 字典-数组转换成pandas.DataFrame
        # self.data_frame = self.__data_frame = pandas.DataFrame(self.dict_provider)
        # logging.info(path.dirname(__file__))
        # workbook = pandas.ExcelFile("进销存.xlsx")
        self.__data_frame = pandas.read_excel("%s/%s" % (path.dirname(__file__), workbook), sheet_name=worksheet)
        self.__data_frame["日期"] = pandas.to_datetime(self.__data_frame["日期"])
        self.data_frame = self.__data_frame

        # df2 = df1.merge(df_abbrev, on='state')  # 类似数据库的 inner join，不匹配数据不会显示

    def to_datetime(self, *args):
        for column in args:
            self.__data_frame[column] = pandas.to_datetime(self.__data_frame[column])
        return self

    #  回复出厂设置
    #  重置group/resample/切片/set_index等，但不会重置to_datetime等数据类型变换操作
    def restore(self):
        self.data_frame = self.__data_frame
        return self

    def set_index(self, index):
        self.data_frame = self.data_frame.set_index(index)
        return self



    def day(self, delta=0):
        date_time = datetime.today() + timedelta(days=delta)
        self.data_frame = self.data_frame[date_time.strftime("%Y-%m-%d"):date_time.strftime("%Y-%m-%d")]
        return self

    def month(self, delta=0):
        # 目前只能实现上个月和当月，不能用于其他情况
        last_month = datetime.now().replace(day=1) - timedelta(days=1)
        date_time = datetime.today() + timedelta(days=delta * last_month.day)
        self.data_frame = self.data_frame[date_time.strftime("%Y-%m")]
        return self

    def resample(self, resample, aggregate="sum"):
        self.data_frame = self.data_frame.resample(resample).aggregate(aggregate)
        return self

    def group(self, group, aggregate="sum"):
        self.data_frame = self.data_frame.groupby(self.data_frame[group]).aggregate(aggregate)
        return self

    def log(self):
        logging.info("\n" + self.data_frame.__str__())

        # logging.info("\n" + self.data_frame[self.data_frame.时间==datetime.strptime("").month].__str__())

    def providers(self):
        list_provider = list()
        list_keys = self.data_frame.keys()
        for record in self.data_frame.values:
            dict_record = dict(zip(list_keys, record))
            list_provider.append([dict_record])
        return list_provider

        # return [self.__business_factory(dict(zip(, x))) for x in self.data_frame.values]

    def __business_factory(self, dict_provider):
        return dict_provider["business"].value(dict_provider)

    # logging.info("\n" + data_frame_by_time.resample("w").agg({"amount": numpy.sum, "outbound": "sum", "return_form": "sum"}).__str__())

    # for name, group in data_frame.groupby("io_at_week"):
    #     logging.info(name)
    #     # logging.info(group["product"].sum())
    #     logging.info(group["amount"].sum())

    # group.apply(lambda row: 'Dear Mr. %s' % row.last_name if row.gender == 'Male' else 'Dear Ms. %s' % row.last_name, axis=1)

    def __list_to_dict(self, list_provider):
        dict_provider = {k: list() for k in list_provider[0].keys()}
        for provider in list_provider:
            for k, v in provider.items():
                dict_provider[k].append(v)
        return dict_provider
