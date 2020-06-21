__author__ = 'shampoo'
from commons.const import const
from testCase.login import testLogin as login
from testCase.customers import testUpdateCustomer as UpdateCustomers
from testCase.customers import testAddCustomer as AddCustomers
from testCase.approvals import testApprovalSetting as Approval
import pymysql

#客户拜访签到次数，拜访签到客户数
class customers_checkin:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.token =''
        self.ids = []
        self.host = 'rm-m5eu4m6a4rugr22fcno.mysql.rds.aliyuncs.com'
        self.user = 'ik_qa'
        self.passwd = '31BTsesM';
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        self.date_list = ['2019-01-31 02:51:58','2019-03-31 02:51:58','2019-05-31 02:51:58','2019-07-31 02:51:58','2019-09-30 02:51:58 ','2019-11-30 02:51:58']
        # self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
        #                           [220, 230]]
        self.userinfo_list = const.USER
        pass
    # 用于创建客户
    def case_0(self):
        self.current_case = 'case 0'
        _login = login.Login()
        for i in range(8):
            _login.login(self.userinfo_list[i]['username'], self.userinfo_list[i]['password'],self.userinfo_list[i]['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            self.token = _login.token
            _UpdateCustomers = UpdateCustomers.UpdateCustomer(self.cookie, self.csrf, self.token)
            _CustomersApproval = Approval.ApprovalSettings(self.cookie,self.csrf)
            _CustomersApproval.close_approval()
            _AddCustomers = AddCustomers.AddCustomer(self.cookie,self.csrf)
            # 为每一个用户创建客户
            id = _AddCustomers.add_customers()
            self.ids.append(id)
            print(self.ids[i])

    # 在创建客户的下面签到
    def case_1(self):
        self.current_case = 'case 1'
        _login = login.Login()
        for x in range(6):
            for i in range (8):
                _login.login(self.userinfo_list[i]['username'], self.userinfo_list[i]['password'],
                             self.userinfo_list[i]['role'])
                self.cookie = _login.cookie
                self.csrf = _login.csrf
                self.token = _login.token
                _UpdateCustomers = UpdateCustomers.UpdateCustomer(self.cookie, self.csrf, self.token)
                for j in range (i+1):
                    print(self.ids[j])
                    # 用于用户签到
                    _UpdateCustomers.checkins(self.ids[j])
                    # 用于修改刚刚签到的时间
                    print(self.date_list[x],self.ids[j])
                    self.updatetime(self.date_list[x],int(self.ids[j]))

    # 用于更新客户签到的时间
    def updatetime(self,time,ids):
        print(ids)
        self.current_case = 'updatetime'
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd,charset='utf8')
        conn.select_db('ding_staging')
        cur = conn.cursor()
        querystring = 'update checkins set created_at = "%s" where id in (select a.maxid from (select max(id) AS maxid from checkins where checkable_id=%s) AS a)'%(time,ids)
        print(querystring)
        cur.execute(querystring)
        conn.commit()
        cur.close()

if __name__ == '__main__':
    _customers_checkin =customers_checkin()
    _customers_checkin.case_0()
    _customers_checkin.case_1()
    # _customers_checkin.updatetime(time='2019-01-31 02:51:58',ids=1207205)
