# -*- coding: utf-8 -*-
__author__ = 'lwang'

from bs4 import BeautifulSoup
import json
import requests
import random


class Ikjxc:
    def __init__(self, base_url='http://test.ikjxc.com/'):
        self.base_url = base_url
        self.csrf = ''
        self.cookie = ''
        self.username = ''
        self.password = ''
        self.response = ''
        pass

    def get_csrf_by_html(self, html_str):
        soup = BeautifulSoup(html_str, 'html.parser')
        csrf = soup.find(attrs={"name": "csrf-token"})['content']
        if len(csrf):
            self.csrf = csrf

    def get_audit_status_by_html(self, html_str):
        soup = BeautifulSoup(html_str, 'html.parser')
        button_list = soup.findAll(name='button')
        audit_status = {
            'pass': '',
            'reject': ''
        }
        for tmp_button in button_list:
            if tmp_button.text == u'审批通过':
                audit_status['pass'] = tmp_button['data-status']
            elif tmp_button.text == u'驳回':
                audit_status['reject'] = tmp_button['data-status']
        return audit_status

    def get_csrf_and_cookie(self):
        url = self.base_url + 'users/sign_in?show_all_version=1'
        response = requests.get(url)
        html_str = response.content
        soup = BeautifulSoup(html_str, 'html.parser')
        self.csrf = soup.find(attrs={"name": "csrf-token"})['content']
        self.cookie = response.headers['set-cookie']

    def get_html(self, url, content):
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'text/html, application/xhtml+xml'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        response = s.get(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            if response.headers['Set-Cookie']:
                self.cookie = response.headers['Set-Cookie']
            self.response = response
            #每次刷新页面后，更新token
            # print self.csrf
            self.get_csrf_by_html(response.text)
            # print self.csrf
            print success_str
            return True

    def get_js(self, url, content):
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        response = s.get(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print success_str
            return True

    def post_js(self, url, content):
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        response = s.post(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print success_str
            return True

    def put_response_json(self, url, body, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.put(url, data=body)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print response.text
            print success_str
            return True

    def post_response_json(self, url, body, content):
        # post方法返回json
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': '*/*'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})



        tmp_list = self.cookie.split(';')
        print tmp_list
        authorization = 'Token '
        for tmp_str in tmp_list:
            if 'token=' in tmp_str:
                authorization += tmp_str + ','
        for tmp_str in tmp_list:
            if 'uid=' in tmp_str:
                authorization += tmp_str
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})

        print s.headers

        response = s.post(url, data=body)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print response.text
            print success_str
            return True

    def get_response_json(self, url, content):
        # put方法返回json
        s = requests.session()
        s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        response = s.get(url)
        success_str = u'%s， success， response time： %s' % (content, response.elapsed)
        fail_str = u'%s， error' % content
        if response.status_code not in [200, 204]:
            self.response = None
            print fail_str
            print u'status code： %s' % response.status_code
            print fail_str
            return False
        else:
            self.response = response
            print response.text
            print success_str
            return True

    # 分析返回为js的情况的，统一处理为字典格式，如
    # $('i#total_inventory').replaceWith('36,926.5000');$('i#total_variety').replaceWith('219.0000');
    # 转化为{'total_inventory':'36,926.5000',  'total_variety':'219.0000'}
    def parse_simple_js(self, js_str):
        tmp_list = js_str.split(';')
        tmp_dic = {}
        for temp_str in tmp_list:
            if 'replaceWith' in temp_str:
                tmp_key = temp_str.split(').replaceWith')[0].split('#')[1][:-1]
                tmp_value = temp_str.split(').replaceWith')[1][1:-1]
                tmp_dic[tmp_key] = tmp_value
        return tmp_dic

    # 分析工作台页面的document的js
    def parse_document_js(self, js_str):
        tmp_list = js_str.split('\');')
        tmp_dic = {}
        for temp_str in tmp_list:
            key = temp_str.split(').find')[0][4:-1]
            tmp_list_2 = temp_str.split('.html(')
            value_list = []
            if len(tmp_list_2) == 2:
                html_str = temp_str.split('.html(')[1][1:]
                html_str = html_str.encode('utf-8').replace('\\"', '"')
                soup = BeautifulSoup(html_str, 'html.parser')
                a_list = soup.findAll(name='a')
                for a in a_list:
                    if a['href'] and 'javascript' not in a['href']:
                        tmp_href_list = a['href'].split('/')
                        id = tmp_href_list[2]
                        type = tmp_href_list[1]
                        value_list.append((id, type))
            if len(key):
                tmp_dic[key] = value_list
        return tmp_dic

    def login(self, username='15600000000', password='111111'):
        if len(self.cookie) == 0:
            self.get_csrf_and_cookie()
        if len(self.cookie) == 0:
            print 'get csrf and cookie error'
            return

        self.username = username
        self.password = password
        url = self.base_url + "users/sign_in"

        body = {
            'utf8': '✓',
            'authenticity_token': self.csrf,
            'user[login]': username,
            'user[password]': password,
            'user[remember_me]': 0,
            'commit': '登 录'
        }

        s = requests.session()
        s.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        s.headers.update({'Accept-Encoding': 'gzip, deflate'})
        s.headers.update({'Accept-Language': 'zh-CN,zh;q=0.8'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'Cookie': self.cookie})
        response = s.post(url=url, data=body)
        if response.status_code == 200:
            print 'login success'
            self.cookie = response.headers['set-cookie']
        else:
            print 'login error'

    def get_purchase_report(self):
        url = self.base_url + 'reports/purchases_report'
        return self.get_html(url, 'get purchases report')

    def get_dashboard(self):
        url = self.base_url + 'dashboard'
        return self.get_html(url, 'get dashboard')

    def get_dashboard_load_statistics(self):
        url = self.base_url + 'dashboard/load_statistics'
        success = self.get_js(url, 'get dashboard load statistics')
        if not success:
            return success
        result_dic = self.parse_simple_js(self.response.text)
        print result_dic
        return success

    def get_dashboard_load_documents(self):
        url = self.base_url + 'dashboard/load_documents'
        success = self.get_js(url, 'get dashboard documents')
        result_dic = self.parse_document_js(self.response.text)
        return result_dic

    def audit_storageios(self, bill_id, is_pass=True):
        # is_pass为true时，审核通过，否则为驳回
        # 先获取到单子的下次审核的状态
        success = self.get_storageios_detail(bill_id)
        if not success:
            return False
        audit_status = self.get_audit_status_by_html(self.response.text)
        print audit_status
        if len(audit_status['pass']) == 0:
            print 'can not audit %s' % bill_id
            return False

        url = self.base_url + 'storageios/%s' % bill_id

        body = {
            'storageio[status]': audit_status['pass'],
            'storageio[reason]': 'auto' + str(random.randint(1, 10000))
        }
        if not is_pass:
            body['storageio[status]'] = audit_status['reject']
        print body
        success = self.put_response_json(url, body, 'audit pass storageios %s' % bill_id)
        if not success:
            return
        response_json = self.response.json()
        if 'code' in response_json:
            if response_json['code'] != 200:
                print self.response.text
                return False
        elif 'status' in response_json:
            if response_json['status']['code'] != 200:
                print response_json['status']['message']
        return True

    def get_storageios_detail(self, bill_id):
        url = self.base_url + 'storageios/%s' % bill_id
        success = self.get_html(url, 'get storageios %s detail' % bill_id)
        return success

    def get_purchases_detail(self, bill_id):
        url = self.base_url + 'purchases/%s' % bill_id

        success = self.get_html(url, 'get purchases %s detail' % bill_id)
        return success

    def audit_purchases(self, bill_id, is_pass=True):
        # is_pass为true时，审核通过，否则为驳回
        # 先获取到单子的下次审核的状态
        success = self.get_purchases_detail(bill_id)
        if not success:
            return False
        audit_status = self.get_audit_status_by_html(self.response.text)
        print audit_status
        if len(audit_status['pass']) == 0:
            print 'can not audit %s' % bill_id
            return False

        url = self.base_url + 'purchases/%s' % bill_id

        body = {
            'purchase[status]': audit_status['pass'],
            'purchase[reason]': 'auto' + str(random.randint(1, 10000))
        }
        if not is_pass:
            body['purchase[status]'] = audit_status['reject']
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % bill_id)
        if not success:
            return False
        response_json = self.response.json()
        if 'code' in response_json:
            if response_json['code'] != 200:
                print self.response.text
                return False
        elif 'status' in response_json:
            if response_json['status']['code'] != 200:
                print response_json['status']['message']
        return True

    def get_sale_orders_detail(self, bill_id):
        url = self.base_url + 'sale_orders/%s' % bill_id
        success = self.get_html(url, 'get sale orders %s detail' % bill_id)
        return success

    def audit_sale_orders(self, bill_id, is_pass=True):
        # is_pass为true时，审核通过，否则为驳回
        # 先获取到单子的下次审核的状态
        success = self.get_sale_orders_detail(bill_id)
        if not success:
            return False
        audit_status = self.get_audit_status_by_html(self.response.text)
        print audit_status
        if len(audit_status['pass']) == 0:
            print 'can not audit %s' % bill_id
            return False

        url = self.base_url + 'sale_orders/%s' % bill_id

        body = {
            'sale_order[status]': audit_status['pass'],
            'sale_order[reason]': 'auto' + str(random.randint(1, 10000))
        }
        if not is_pass:
            body['sale_order[status]'] = audit_status['reject']
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % bill_id)
        if not success:
            return False
        response_json = self.response.json()
        if 'code' in response_json:
            if response_json['code'] != 200:
                print self.response.text
                return False
        elif 'status' in response_json:
            if response_json['status']['code'] != 200:
                print response_json['status']['message']
        return True

    def get_sales_detail(self, bill_id):
        url = self.base_url + 'sales/%s' % bill_id
        success = self.get_html(url, 'get sales %s detail' % bill_id)
        return success

    def audit_sales(self, bill_id, is_pass=True):
        # is_pass为true时，审核通过，否则为驳回
        # 先获取到单子的下次审核的状态
        success = self.get_sales_detail(bill_id)
        if not success:
            return False
        audit_status = self.get_audit_status_by_html(self.response.text)
        print audit_status
        if len(audit_status['pass']) == 0:
            print 'can not audit %s' % bill_id
            return False

        url = self.base_url + 'sales/%s' % bill_id

        body = {
            'sale[status]': audit_status['pass'],
            'sale[reason]': 'auto' + str(random.randint(1, 10000))
        }
        if not is_pass:
            body['sale[status]'] = audit_status['reject']
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % bill_id)
        if not success:
            return False
        response_json = self.response.json()
        if 'code' in response_json:
            if response_json['code'] != 200:
                print self.response.text
                return False
        elif 'status' in response_json:
            if response_json['status']['code'] != 200:
                print response_json['status']['message']
        return True

    def audit_for_dashboard(self, is_pass):
        result_dic = self.get_dashboard_load_documents()
        print result_dic
        for bill_id, bill_type in result_dic['approving-documents']:
            if bill_type == 'purchases':
                self.audit_purchases(bill_id, is_pass)
            elif bill_type == 'suppliers':
                pass
            elif bill_type == 'sales':
                self.audit_sales(bill_id, is_pass)
            elif bill_type == 'customers':
                pass
            elif bill_type == 'sale_orders':
                self.audit_sale_orders(bill_id, is_pass)
            elif bill_type == 'storageios':
                self.audit_storageios(bill_id,  is_pass)
            elif bill_type == 'purchase_orders':
                self.audit_purchase_orders(bill_id,  is_pass)

    def get_members(self):
        # 采购人员列表
        url = self.base_url + 'settings/members/enabled'
        success = self.get_response_json(url, 'get members')
        if not success:
            return []
        return self.response.json()['members']

    def get_warehouses(self):
        # 仓库列表
        url = self.base_url + 'settings/warehouses'
        success = self.get_response_json(url, 'get warehouses')
        if not success:
            return []
        return self.response.json()['warehouses']

    def get_suppliers_for_purchase(self):
        # 供应商列表
        url = self.base_url + 'suppliers/query_for_purchase'
        success = self.get_response_json(url, 'get suppliers for purchase')

        if not success:
            return []
        return self.response.json()['suppliers']

    def get_supplier_detail(self, supplier_id):
        url = self.base_url + 'suppliers/%s' % supplier_id
        success = self.get_response_json(url, 'get supplier %s detail' % supplier_id)
        if not success:
            return {}
        if self.response.json()['status']['code'] != '200':
            return {}
        return self.response.json()['supplier']

    def get_supplier_contact(self, supplier_id):
        url = self.base_url + 'contacts?supplier_id=%s&purchase_order_id=' % supplier_id
        success = self.get_response_json(url, 'get supplier %s contact' % supplier_id)

        if not success:
            return []
        return self.response.json()['contacts']

    def get_product_attr_groups(self):
        url = self.base_url + 'product_attr_groups/query?keyword='
        success = self.get_response_json(url, 'get product attr groups')

        if not success:
            return []
        return self.response.json()['product_attr_groups']

    def get_product_units(self, product_id):
        url = self.base_url + 'products/%s/get_units' % product_id
        success = self.get_response_json(url, 'get product %s units' % product_id)

        if not success:
            return []
        return self.response.json()['units']

    def get_purchase_new(self):
        url = self.base_url + 'purchase_orders/new'
        success = self.get_html(url, 'get purchase new')
        if not success:
            return False
        html_str = self.response.text
        soup = BeautifulSoup(html_str, 'html.parser')
        div = soup.find(name='div', attrs={'data-react-class': 'PurchaseOrdersNew'})
        return json.loads(div['data-react-props'])

    def post_new_purchase_order(self, body):
        url = self.base_url + 'api/purchase_orders.json'
        success = self.post_response_json(url, body, 'post new purchase order')
        if not success:
            return {}
        return self.response.json()

    def get_purchase_orders_detail(self, bill_id):
        url = self.base_url + 'purchase_orders/%s' % bill_id

        success = self.get_html(url, 'get purchase orders %s detail' % bill_id)
        return success

    def audit_purchase_orders(self, bill_id, is_pass=True):
        # is_pass为true时，审核通过，否则为驳回
        # 先获取到单子的下次审核的状态
        success = self.get_purchase_orders_detail(bill_id)
        if not success:
            return False
        audit_status = self.get_audit_status_by_html(self.response.text)
        print audit_status
        if len(audit_status['pass']) == 0:
            print 'can not audit %s' % bill_id
            return False

        url = self.base_url + 'purchase_orders/%s' % bill_id

        body = {
            'purchase_order[status]': audit_status['pass'],
            'purchase_order[reason]': 'auto' + str(random.randint(1, 10000))
        }
        if not is_pass:
            body['purchase_order[status]'] = audit_status['reject']
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % bill_id)
        if not success:
            return False
        response_json = self.response.json()
        if 'code' in response_json:
            if response_json['code'] != 200:
                print self.response.text
                return False
        elif 'status' in response_json:
            if response_json['status']['code'] != 200:
                print response_json['status']['message']
        return True

    def get_purchases_new(self, order_id, category='in'):
        url = self.base_url + 'purchases/new?category=%s&order_id=%s' % (category, order_id)
        print url
        success = self.get_html(url, 'get purchase new')
        if not success:
            return False
        html_str = self.response.text
        soup = BeautifulSoup(html_str, 'html.parser')
        div = soup.find(name='div', attrs={'data-react-class': 'PurchasesNew'})
        return json.loads(div['data-react-props'])

    def get_product_items_for_purchase(self, purchase_order_id):
        url = self.base_url + 'purchases/get_product_items?id=&order_id=%s' % purchase_order_id
        success = self.get_response_json(url, 'get product items for purhcase order %s' % purchase_order_id)
        if not success:
            return {}
        return self.response.json()

    def post_new_purchase(self, body):
        url = self.base_url + 'api/purchases.json'
        success = self.post_response_json(url, body, 'post new purchase')
        if not success:
            return {}
        return self.response.json()

if __name__ == "__main__":
    a_ikjxc = Ikjxc()
    a_ikjxc.login()
    #print a_ikjxc.get_product_attr_groups()
    # a_ikjxc.get_purchase_report()
    # print a_ikjxc.response.content
    # a_ikjxc.get_dashboard()
    # a_ikjxc.get_dashboard_load_statistics()
    # a_ikjxc.get_dashboard_load_documents()
    # a_ikjxc.audit_storageios(5015)
    # a_ikjxc.audit_purchases(11237)
    # a_ikjxc.audit_sale_orders(1136)
    # a_ikjxc.audit_sales(14510, is_pass=False)
    # a_ikjxc.audit_for_dashboard(is_pass=True)
    # a_ikjxc.get_members()
    a_ikjxc.get_purchase_new()
#