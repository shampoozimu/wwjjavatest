from decimal import Decimal as D
from commons import common
from commons.const import const
from testCase.login import testLogin as login
from testCase.contracts import testDeleteContract as DeleteContract
from testCase.contracts import testUpdateContract as UpdateContract
from testCase.contracts import testSettingsContractsApproval as ContractsApproval
from testCase.contracts import testAddContract as AddContract
class contracts_revisit_logs:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        self.date_list = ['2018-01-10 02:51:58', '2018-03-10 02:51:58', '2018-05-10 02:51:58', '2018-07-10 02:51:58',
                          '2018-09-10 02:51:58 ', '2018-11-10 02:51:58']
        self.userinfo_list = const.USER
        self.token = ''
        pass


    #关闭审批
    def approvaled(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # 关闭合同审批
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.close_contract_approval()
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 用户1合同
            # contract_id = _AddContract.add_contracts()
            # list.append(contract_id[0])

        a = list
        print(list)
        # a=[100313, 100314, 100315, 100316, 100317, 100318, 100319, 100320]
        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='关闭审批')
            b = b + 1
    # 待审批
    def approvaling(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        # a =0
        # contract_id = ''
        # dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 待审批的合同
            contract_id = _AddContract.add_contracts(approve_status='applying', DepartmentId=0)
            # dict.update({userinfo['username']: contract_id})
            list.append(contract_id[0])
            # print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='待审批')
            b = b + 1

    #审批通过
    def approve_verify(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 待审批的合同
            contract_id = _AddContract.add_contracts()
            _ContractsApproval.verify_contracts(contract_id)
            list.append(contract_id[0])
            # print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批通过')
            b = b + 1

    #审批驳回
    def deny_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        # a =0
        customer_id = ''
        dict = {}
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 审批通过后驳回
            contract_id = _AddContract.add_contracts()
            _ContractsApproval.verify_contracts(contract_id[0])
            _ContractsApproval.deny_contracts(contract_id[0])
            list.append(contract_id[0])
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批驳回')
            b = b + 1

     # 审批否决
    def deny_approval_customer(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的客户
            ##添加 待审批的客户后否决
            contract_id = _AddContract.add_contracts(approve_status='applying', DepartmentId=0)
            # 审批被否决
            _ContractsApproval.deny_contracts(contract_id[0])
            list.append(contract_id[0])
            print(list)
        a = list
        # a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批否决')
            b = b + 1
    # 审批撤销
    def cancel_approval(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf

        # a =0
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
            _ContractsApproval.open_contract_approval()
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)

            ##添加 审批撤销
            contract_id =_AddContract.add_contracts(approve_status='applying')
            _ContractsApproval.cancel_contracts(contract_id[0])
            list.append(contract_id[0])
        print(list)
        a = list
        ## a = [1233194, 1233195, 1233196, 1233197, 1233198, 1233199, 1233200, 1233201]

        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='审批撤销')
            b = b + 1

# 开启审批 新增草稿
    def contracts_caogao(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # 关闭合同审批
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.open_contract_approval()
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 用户1合同
            # 添加草稿
            contract_id= _AddContract.add_contracts(approve_status='draft')
            list.append(contract_id[0])

        a = list
        print(list)
        # a = [97078, 97079]
        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='合同草稿')
            b = b + 1
    # 关闭审批 新增草稿
    def contracts_caogao2(self):
        self.current_case = 'case 1'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie = _login.cookie
        self.csrf = _login.csrf
        # 关闭合同审批
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.close_contract_approval()
        list = []
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _AddContract = AddContract.AddContract(self.cookie, self.csrf)
            # 8个用户新增一条关闭审批的合同
            ##添加 用户1合同
            # 添加草稿
            contract_id= _AddContract.add_contracts(approve_status='draft',DepartmentId=1)
            list.append(contract_id[0])

        a = list
        print(list)
        # a = [97078, 97079]
        b = 1
        for userinfo in self.userinfo_list:
            print(userinfo['username'])
            _login.login(userinfo['username'], userinfo['password'], userinfo['role'])
            self.cookie = _login.cookie
            self.csrf = _login.csrf
            _UpdateContract = UpdateContract.UpdateContract(self.cookie, self.csrf)
            for i in range(b):
                for j in range(6):
                    _UpdateContract.add_contract_revisit_log(a[b - 1 - i], date_list=self.date_list[j],data='合同草稿2')
            b = b + 1
   ## 删除
    def case_2(self):
        self.current_case = 'case 2'
        _login = login.Login()
        _login.login(self.userinfo_super['username'], self.userinfo_super['password'], self.userinfo_super['role'])
        self.cookie =_login.cookie
        self.csrf = _login.csrf
        _ContractsApproval = ContractsApproval.Approvals(self.cookie, self.csrf)
        _ContractsApproval.close_contract_approval()
        _DeleteContract = DeleteContract.DeleteContract(self.cookie, self.csrf)
        b =_DeleteContract.get_contract_ids()
        page =b[0][0]
        print (page)
        for i in range(int(page)):
             c =_DeleteContract.get_contract_ids()
             Contract_list = c[1]
             for Contract in Contract_list:
                 _DeleteContract.delete_contract(Contract)


    def contracts_revisit_logs(self):
        _revisit_logs = contracts_revisit_logs()
        # 先跑关闭审批的
        # 关闭审批 新增合同草稿
        _revisit_logs.contracts_caogao2()
        # 关闭审批
        _revisit_logs.approvaled()
        # 待审批
        _revisit_logs.approvaling()
        # 审批通过
        _revisit_logs.approve_verify()
        # 撤销
        _revisit_logs.cancel_approval()
        # 开启审批 新增合同草稿
        _revisit_logs.contracts_caogao()

if __name__ == '__main__':
    _revisit_logs = contracts_revisit_logs()
    # os.remove('status_code_ok.txt')
    # os.remove('status_code.txt')
    # _revisit_logs.case_2()
    # 先跑关闭审批的
    # 关闭审批 新增合同草稿
    # _revisit_logs.contracts_caogao2()
    # 关闭审批
    _revisit_logs.approvaled()

    # 待审批
    # _revisit_logs.approvaling()
    # 审批通过
    # _revisit_logs.approve_verify()
    # 撤销
    # _revisit_logs.cancel_approval()
    # 开启审批 新增合同草稿
    # _revisit_logs.contracts_caogao()



    # 驳回
    # _revisit_logs.deny_approval()
    # 否决
    # _revisit_logs.deny_approval_customer()
    #

    #









