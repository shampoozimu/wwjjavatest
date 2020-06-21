import pymysql
import math
from commons.const import const
from testCase.login import testLogin as login
from testCase.customers import testAddCustomer as AddCustomers
from testCase.customers import testDeleteCustomer as DeleteCustomers
from testCase.approvals import testApprovalSetting as Approval

class customers_number:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.token =''
        #staging
        self.host = 'rm-m5eu4m6a4rugr22fcno.mysql.rds.aliyuncs.com'
        # test
        # self.host ='rdscbq34656z0ix59br0.mysql.rds.aliyuncs.com'
        self.user = 'ik_qa'
        self.passwd ='31BTsesM';
        self.customers ={}
        # self.userinfo_super = {'username': '15639356523', 'password': 'Ab123456','role':'超管'}
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        self.date_list = ['2019-01-31 02:51:58','2019-03-31 02:51:58','2019-05-31 02:51:58','2019-07-31 02:51:58','2019-09-30 02:51:58 ','2019-11-30 02:51:58']
        # self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
        #                           [220, 230]]
        self.userinfo_list = const.USER
        pass

    def case_1(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = Approval.ApprovalSettings(self.cookie,self.csrf)
        _CustomersApproval.close_approval()
        a = 1
        customers = {}
        for userinfo in self.userinfo_list:
            print (userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie =_login.cookie
            self.csrf = _login.csrf
            _AddCustomers = AddCustomers.AddCustomer(self.cookie,self.csrf)
            _CustomersApprovall = Approval.ApprovalSettings(self.cookie,self.csrf)
            for i in range(6* a):
                month = int(math.ceil((i + 1) / a))
                # print(month)
                if userinfo['username'] == '13799999999' and i>=18 :
                    #添加客户
                    id=_AddCustomers.add_customers(DepartmentId=1)
                else:
                    id =_AddCustomers.add_customers()
                if month not in customers:
                    customers[month] = []
                customers[month].append(id)
            a += 1
        self.customers =customers

        for i in range(6):
            self.sql(self.date_list[i],tuple(customers[i+1]))

        _login.login(self.userinfo_super['username'], self.userinfo_super['password'],
                     self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _CustomersApproval = Approval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.open_approval()
        a = 1
        customers = {}
        customers[1] = []
        for userinfo in self.userinfo_list:
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            print(userinfo['username'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddCustomers = AddCustomers.AddCustomer(self.cookie, self.csrf)
            _CustomersApproval = Approval.ApprovalSettings(self.cookie, self.csrf)

            # 待审批的客户
            customer_id = _AddCustomers.add_customers(approve_status='applying', DepartmentId=0)
            customers[1].append(customer_id)
            # print(customers_data)
            # 审批通过后否决
            customer_id = _AddCustomers.add_customers()
            _CustomersApproval.approve_verify(customer_id)
            _CustomersApproval.deny_approval(customer_id)
            customers[1].append(customer_id)
            # 审批否决的客户
            customer_id = _CustomersApproval.deny_approval(
                _AddCustomers.add_customers(approve_status='applying'))
            customers[1].append(customer_id)
            # 客户撤销
            customer_id = _CustomersApproval.cancel_approval(_AddCustomers.add_customers(approve_status='applying'))
            customers[1].append(customer_id)
            # print(customers_data)
            if userinfo['username'] == '13799999999' :
                for i in range(6 * a):
                    month = int(math.ceil((i + 1) / a))
                    # print(month)
                    if i>=18:
                    # 审批通过的客户
                        customer_id = _CustomersApproval.approve_verify(_AddCustomers.add_customers(approve_status='applying',DepartmentId=1))
                    else:
                        customer_id = _CustomersApproval.approve_verify( _AddCustomers.add_customers(approve_status='applying', DepartmentId=0))
                    if month not in customers:
                        customers[month] = []
                    customers[month].append(customer_id)
            else:

                for i in range(6 * a):
                    month = int(math.ceil((i + 1) / a))
                    # print(month)
                    # 审批通过的客户
                    customer_id = _CustomersApproval.approve_verify(
                        _AddCustomers.add_customers(approve_status='applying', DepartmentId=0))
                    if month not in customers:
                        customers[month] = []
                    customers[month].append(customer_id)
            # print(customers_data)
            a += 1
        print(customers)
        for i in range(6):
            self.sql(self.date_list[i],tuple(customers[i+1]))

    def sql(self,time,ids):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd,charset='utf8')
        conn.select_db('ding_staging')
        cur = conn.cursor()
        querystring = 'update customers_data set created_at="%s" where id in %s ' % (time, ids)
        cur.execute(querystring)
        conn.commit()
        cur.close()

    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        self.token = _login.token
        _CustomersApproval = Approval.ApprovalSettings(self.cookie, self.csrf)
        _CustomersApproval.close_approval()
        _DeleteCustomers = DeleteCustomers.DeleteCustomer(self.cookie, self.csrf,self.token)
        b =_DeleteCustomers.get_customer_ids()
        page =b[0]
        # page =3
        for i in range(int(page)):
             print(i)
             c =_DeleteCustomers.get_customer_ids()
             print(c)
             print(c[1])
             Customers_list = c[1]
             # print(len(Customers_list)-1)              'customer_approve[enable_customer_approve]': '1' ,
             for i in range(len(Customers_list)):
                 _DeleteCustomers.delete_customer(Customers_list[i])


if __name__ == '__main__':
    _customers_number =customers_number()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    _customers_number.case_2()
    _customers_number.case_1()
    # _customers_number.sql()
    # #创建合同数的对象
    # _contract_number = result_contract_number.result_contract_number_user()
    # #按用户 合同数 报表筛选
    # _contract_number.contract_number_baobiao()
    # #按用户 合同数 工作台筛选
    # _contract_number.contract_number_gongzuotai()
    # # #按部门 合同数 报表筛选
    # _contract_number_departments=result_contract_number_departments.result_contract_number_departments()
    # _contract_number_departments.contract_number_d_baobiao()











