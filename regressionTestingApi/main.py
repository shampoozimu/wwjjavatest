# -*- coding: utf-8 -*-
__autotest__ = 'InterfaceAutomationTest'

import codecs
import os
from testCase.login import testLogin as login
from testCase.customers import testCustomer as customers
from testCase.leads import testLead as leads
from testCase.expense_center import testExpenseCenter as expense_center

from  testCase.lead_commons import testLeadCommon as lead_common
from testCase.customerCommons import testGetCustomerCommons as customer_commons
from testCase.contacts import testContact as contacts
from testCase.reportCenter import testReport as report
from testCase.announcements import testAnnouncement as announcement
from testCase.organizations import testOrganization as organization
from testCase.contracts import testContract as contracts
from testCase.opportunities import testOpportunity as opportunities
from testCase.products import  testProduct as products
from testCase.received_payment_center import testReceivedPaymentCenter as received_payment_center
# from testCase.customFieldSettings import testCustomField as customfield
from testCase.approvals import testApprovalCase as approval
from testCase.roles import  testGetRoles as role
from commons import filters
from commons.const import const
from testCase.departments import testGetDepartment as departments
# from testCase.performance import test1


class Main:
    def __init__(self):
        self.cookie = ''
        self.csrf = ''

if __name__ == "__main__":
    os.remove('status_code_ok.txt')
    os.remove('status_code.txt')
    for userinfo in const.USER:
        # print (userinfo)
        _login = login.Login()
        # _login.private_login(userinfo['username'], userinfo['password'])
        print(userinfo['username'], userinfo['password'])
        _login.uc_login(userinfo['username'], userinfo['password'], userinfo['role'])
        # _login.cook_get()
        # _login.get_csrf_by_home_html()
        main = Main()
        main.cookie = _login.cookie
        main.csrf = _login.csrf

        # 线索
        # _leads = leads.Leads(main.cookie, main.csrf)
        # _leads.testLeads()
        # print(u'%s线索模块已执行完成' %(userinfo['username']))
        # 线索池
        # _lead_common = lead_common.LeadCommon(main.cookie, main.csrf)
        # if '超管'in userinfo['role']:
        #     _lead_common.superior_lead_common()
        # else:
        #     _lead_common.basic_lead_common()
        # 客户
        # _customers = customers.Customers(main.cookie, main.csrf)
        # _customers.testCustomers()
        # print(u'%s客户模块已执行完成'%(userinfo['username']))
        # 客户公海
        # _customer_commons = customer_commons.GetCustomerCommons(main.cookie,main.csrf)
        # _customer_commons.get_all_scope()
        # print('%s客户公海已执行完成' %(userinfo['username']))
        # 联系人
        _contacts = contacts.Contacts(main.cookie, main.csrf)
        _contacts.testContacts()
        print('%s联系人已执行完成' %(userinfo['username']))
        # 商机
        # _opportunities = opportunities.Opportunities(main.cookie, main.csrf)
        # _opportunities.testOpportunities()
        # print('%s商机已执行完成' % (userinfo['username']))
        # # 合同
        # _contracts = contracts.Contracts(main.cookie,main.csrf)
        # _contracts.testContracts()
        # print('%s合同已执行完成' % (userinfo['username']))
        # 产品
        # _products = products.Products(main.cookie, main.csrf)
        # _products.testProducts()
        # print('%s产品已执行完成' % (userinfo['username']))
        # 回款
        # _received_payment_center = received_payment_center.ReceivedPaymentCenter(main.cookie,main.csrf)
        # _received_payment_center.testReceivedPaymentCenter()
        # 报表
        # _report = report.Report(main.cookie, main.csrf)
        # _report.testReport()
        # 费用报销
        # _expense_center = expense_center.ExpenseCenters(main.cookie, main.csrf)
        # _expense_center.testExpenseCenters()
        #公告
        # _announcement = announcement.Announcements(main.cookie, main.csrf)
        # _announcement.testAnnouncements()
        #公司信息
        # _organization = organization.Organization(main.cookie, main.csrf)
        # _organization.testOrganization()
        #
        # _customField = customfield.CustomField(main.cookie, main.csrf)
        # _customField.testCustomField()
        #
        # _contracr = contract.ContractApproval(main.cookie, main.csrf)
        # _contracr.testContract()
        # !!!审批!!!
        # _approval = approval.ApprovalCase(main.cookie, main.csrf)
        # _approval.testCase1()

        # 角色和权限设置
        # _role = role.GetRole(main.cookie, main.csrf)
        # list = ['organization_own', 'self_and_subordinate_department_own', 'self_department_own', 'self_own']
        # _role.ding_set_data_authority('organization_own')
        # _role.set_data_authority()

        #获取部门id
        # _department = departments.GetDepartment(main.cookie, main.csrf)
        # _department.getDepartmentId()
        # _a=test1.getRank(main.cookie, main.csrf)
        # _a.get_rank()