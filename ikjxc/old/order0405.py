# -*- coding: utf-8 -*-
__author__ = 'lwang'
import requests
from BeautifulSoup import BeautifulSoup
import json
import random
import datetime
import re


class OrderPurchase:
    def __init__(self):
        self.purchase_order_id = 0
        self.purchase_id = 0
        self.username = '15600000000'
        self.password = '111111'
        #self.user = Ikjxc()
        self.purchase_order = {}
        self.warehouses = []
        self.suppliers = []
        self.products = []
        self.members = []
        self.purchase = {}
        self.purchase_order_id = ''
        self.base_url ='http://test.ikjxc.com/'
        #self.base_url ='https://ikjxc.com/'
        self.cookie = ''
        self.purchase_entry_id = ''
        self.cookie_given = ''
        self.sale_id = ''
        self.sale_out_id =''
        self.storageio_id =''
        self.storageio_out_id = ''
        self.storage_transfer_id = ''

    def post_response_json(self, url, body, content):
        # post方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        #s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': '*/*;q=0.5text/javascript, application/javascript, application/ecmascript, application/x-ecmascript'})
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

    def delete_response_json(self, url, content):
        # get方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        #s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
        response = s.delete(url)
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
        # get方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        #s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
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

    def post_response_js(self, url, body, content):
        # post方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
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

    def get_response_js(self, url, content):
        # get方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        #s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
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
            #print success_str
            return True

    def put_response_js(self, url, body, content):
    # post方法返回js
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization': 'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
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

    def put_response_json(self, url, body, content):
        # put方法返回json
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
            s.headers.update({'Cookie': self.cookie})
        # s.headers.update({'Cookie': self.cookie})
        s.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01'})
        #s.headers.update({'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'})
        s.headers.update({'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0'})
        s.headers.update({'X-CSRF-Token': self.csrf})
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        s.headers.update({'Authorization':'Token token=cb5e0c1db161fe92a7f4ce67754821, uid=b9d28be2d18075de7435'})
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

    def get_csrf_and_cookie(self):
        url = self.base_url + 'users/sign_in?show_all_version=1'
        response = requests.get(url)
        html_str = response.content
        soup = BeautifulSoup(html_str)
        self.csrf = soup.find(attrs={"name": "csrf-token"})['content']
        self.cookie = response.headers['set-cookie']

    def get_csrf_by_html(self, html_str):
        soup = BeautifulSoup(html_str)
        csrf = soup.find(attrs={"name": "csrf-token"})['content']
        if len(csrf):
            self.csrf = csrf

    def get_random_int(self, max_num):
        tmp = random.randint(0, max_num)
        if tmp < max_num:
            return tmp
        else:
            return tmp - 1

    def get_today_str(self):
        today = datetime.datetime.now()
        return today.strftime('%Y-%m-%d')

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

    def audit_purchase_order(self, id=''):
        if len(str(id)) == 0:
            purchase_order_id = self.purchase_order['id']
        else:
            purchase_order_id = id
        for i in range(3):
            self.audit_purchase_orders(purchase_order_id)

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
        print url
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

    def get_audit_status_by_html(self, html_str):
        soup = BeautifulSoup(html_str)
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

    def get_purchase_orders_detail(self, bill_id):
        url = self.base_url + 'purchase_orders/%s' % bill_id
        print url
        success = self.get_html(url, 'get purchase orders %s detail' % bill_id)
        return success

    def get_sale_orders_back_detail(self, bill_id):
        url = self.base_url + 'sales/%s' % bill_id
        print url
        success = self.get_html(url, 'get sale orders back %s detail' % bill_id)
        return success

    def get_html(self, url, content):
        s = requests.session()
        if len(self.cookie_given):
            s.headers.update({'Cookie': self.cookie_given})
        else:
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

    #采购单一级审核
    def verify_purchase_orders_first(self, order_id):
        url = self.base_url + 'purchase_orders/%s' % order_id
        print url
        body = {
            'purchase_order[status]':'second_approving',
            'purchase_order[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % order_id)
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
    #采购单二级审核
    def verify_purchase_orders_sec(self, order_id):
        url = self.base_url + 'purchase_orders/%s' % order_id
        print url
        body = {
            'purchase_order[status]':'third_approving',
            'purchase_order[reason]':'sec'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % order_id)
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
    #采购单三级审核
    def verify_purchase_orders_pass(self, order_id):
        url = self.base_url + 'purchase_orders/%s' % order_id
        print url
        body = {
            'purchase_order[status]':'passed',
            'purchase_order[reason]':'pass'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass purchase %s' % order_id)
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
    #采购退货单审核
    def verify_purchase_orders_back_pass(self, order_id):
        url = self.base_url + 'purchases/%s' % order_id
        print url
        body = {
            'purchase[status]':'passed',
            'purchase[reason]':'pass'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass purchase order back %s' % order_id)
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

    #新增采购单
    def post_new_purchase_order(self):
        url = self.base_url + 'api/purchase_orders.json'
        body = {
            'id':'',
            'supplier_id':'5509',
            'warehouse_id':'61',
            'category':'in',
            'number':'test-%s'% self.get_random_int(9999),
            'documented_at':'2017-03-15',
            'delivered_at':'2017-03-15',
            'total_quantity':'2.0000',
            'total_deduction':'0.0000',
            'purchase_member_id':'13356',
            'total_amount':'20.0000',
            'discount':'0.00',
            'deduction':'0.0000',
            'amount':'23.4660',
            'total_tax_amount':'3.4660',
            'total_amount_with_tax':'23.4660',
            'note':'',
            'status':'approving',
            'supplier_address':'',
            'contact_id':'25318',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_address':'',
            'order_items_attributes[0][product_attr_group_id]':'86550',
            'order_items_attributes[0][product_number]':'NEW CP0007',
            'order_items_attributes[0][product_unit_id]':'86800',
            'order_items_attributes[0][attr_names]':'',
            'order_items_attributes[0][product_id]':'124473',
            'order_items_attributes[0][modified]':'price',
            'order_items_attributes[0][name]':'test-wl-01',
            'order_items_attributes[0][spec]':'',
            'order_items_attributes[0][unit]':'冬虫夏草',
            'order_items_attributes[0][quantity]':'2.0000',
            'order_items_attributes[0][price]':'10.0000',
            'order_items_attributes[0][price_with_tax]':'11.7330',
            'order_items_attributes[0][discount]':'0.00',
            'order_items_attributes[0][batch_number]':'',
            'order_items_attributes[0][produced_at]':'',
            'order_items_attributes[0][expired_at]':'',
            'order_items_attributes[0][deduction]':'0.0000',
            'order_items_attributes[0][amount]':'20.0000',
            'order_items_attributes[0][tax_rate]':'17.33',
            'order_items_attributes[0][tax_amount]':'3.4660',
            'order_items_attributes[0][amount_with_tax]':'23.4660',
            'order_items_attributes[0][note]':''
        }
        success = self.post_response_json(url, body, 'post new purchase order')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if self.response.json()['status']['code'] == '200':
            self.purchase_order = self.response.json()['purchase_order']
            self.purchase_order_id =self.purchase_order['id']
            print self.purchase_order['id']
        print self.purchase_order

    def get_purchases_new(self, order_id, category='in'):
        if len(str(order_id)) == 0:
            print 'get purchase new error: there is not an order id'
            return

        url = self.base_url + 'purchases/new?category=%s&order_id=%s' % (category, order_id)
        print url
        success = self.get_html(url, 'get purchase new')
        print self.response.content
        #if not success:
        #    return False
        html_str = self.response.text
        #print u'html %s'% html_str
        soup = BeautifulSoup(html_str)
        #print u'soup %s'% soup
        div = soup.find(name='div', attrs={'data-react-class': 'PurchasesNew'})
        #print u'div %s' % div
        #print u'wangel%s' % json.loads(div['data-react-props'])
        json.loads(div['data-react-props'])
        return json.loads(div['data-react-props'])

    def get_today_str(self):
        today = datetime.datetime.now()
        #print today
        #print today.strftime('%Y-%m-%d %H:%M:%S')
        return today.strftime('%Y-%m-%d')

    def get_today_str_yymmddhm(self):
        today = datetime.datetime.now()
        #print today
        #print today.strftime('%Y-%m-%d %H:%M:%S')
        return today.strftime('%Y-%m-%d %H:%M')

    def get_product_items_for_purchase(self, purchase_order_id):
        url = self.base_url + 'purchases/get_product_items?id=&order_id=%s' % purchase_order_id
        print url
        success = self.get_response_json(url, 'get product items for purhcase order %s' % purchase_order_id)
        if not success:
            return {}
        #return self.response.json()
        print  u'awngle %s' % self.response.json()
    #添加商品
    def add_product(self):
        url = self.base_url + 'api/products'
        print url
        body ={
        'product[number]':'wl-test-auto-%s'% self.get_random_int(9999),
        'product[name]':'毛巾',
        'product[product_category_id]':'14569',
        'product[spec]':'张',
        'product[unit_id]':'1367',
        'product[unit_name]':'张',
         'product[default_unit_id]':'1367',
        'product[note]':'wl-test-auto-%s'% self.get_random_int(9999),
        'product[barcode]':self.get_random_int(99999999999),
        'product[product_images][0][key]':'Ft9hMiA6eF7zf_ubJIvjaTTKwK1w',
        'product[product_images][0][name]':'定时时间.png',
        'product[product_images][0][url]':'https://obbsip92b.qnssl.com/Ft9hMiA6eF7zf_ubJIvjaTTKwK1w?&e=1490776748&token=w2yRBQw0CPY-fsy6hxBjASopjHCTtT7RKFRtQeJz:pklfD33q6_hJeTrKhB7R-DjyMGw=',
        'product[current_warning_policy]':'total',
        'product[split_warning_status]':'split_closed',
        'product[total_warning_status]':'total_opened',
        'product[attr_status]':'attr_opened',
        'product[price_policy_setting]':'product_attr_policy',
        'product[unit_setting]':'single_unit',
        'product[attr_warning_status]':'attr_warning_closed',
        'product[batch_status]':'batch_closed',
        'product[serial_code_status]':'serial_closed',
        #'product[life_warning_days]':'10',
        #'product[life_period]':'30',
        'product[product_units_attributes][0][unit_id]':'1367',
        'product[product_units_attributes][0][unit_name]':'张',
        'product[product_units_attributes][0][price_policy_attributes][sale_price]':'',
        'product[product_units_attributes][0][price_policy_attributes][purchase_price]':'',
        'product[default_product_attr_group][category]':'default_attr',
        'product[default_product_attr_group][product_attr_names]':'',
        'product[default_product_attr_group][product_attr_ids]':'',
        'product[default_product_attr_group][number]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][warehouse_id]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][warehouse_name]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][product_attr_group_id]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][product_attr_group_product_attr_ids]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][product_attr_group_product_attr_names]':'',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][max_amount]':'100',
        'product[default_product_attr_group][inventory_warning_policies_attributes][0][min_amount]':'1',
        'product[product_attr_groups_attributes][0][category]':'default_attr',
        'product[product_attr_groups_attributes][0][product_attr_names]':'',
        'product[product_attr_groups_attributes][0][product_attr_ids]':'',
        'product[product_attr_groups_attributes][0][number]':'',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][warehouse_id]':'',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][warehouse_name]':'',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][product_attr_group_id]':'',

        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][product_attr_group_product_attr_ids]':'',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][product_attr_group_product_attr_names]':'',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][max_amount]':'100',
        'product[product_attr_groups_attributes][0][inventory_warning_policies_attributes][0][min_amount]':'1',
        'product[product_attr_groups_attributes][1][category]':'custom_attr',
        'product[product_attr_groups_attributes][1][product_attr_ids]':'8/40',
        'product[product_attr_groups_attributes][1][product_attr_names]':'玫瑰红/170#L',
        'product[product_attr_groups_attributes][1][number]':'wl-test-auto-8483_1',
        'product[product_attr_groups_attributes][1][price_policy_attributes][product_attr_group_product_attr_ids]':'8/40',
        'product[product_attr_groups_attributes][1][price_policy_attributes][product_attr_group_product_attr_names]':'玫瑰红/170#L',
        'product[product_attr_groups_attributes][1][price_policy_attributes][unit_name]':'张',
        'product[product_attr_groups_attributes][1][price_policy_attributes][sale_price]':'15',
        'product[product_attr_groups_attributes][1][price_policy_attributes][purchase_price]':'10',
        'product[product_attrables_attributes][0][product_attr_id]':'5',
        'product[product_attrables_attributes][0][product_id]':'',
        'product[product_attrables_attributes][1][product_attr_id]':'37',
        'product[product_attrables_attributes][1][product_id]':''

        }
        success = self.post_response_json(url, body,'add product')
        if not success:
            return {}
        #return self.response.json()
        #print  u'awngle %s' % self.response.json()
        id = self.response.json()['product']['id']
        return id
    #获取商品信息
    def get_product_info(self,product_id):
        url = self.base_url+'api/products/%s' % product_id
        #http://test.ikjxc.com/api/products/124488
        success = self.get_response_json(url, 'get product %s info ' % product_id)
        a = self.response.json()
        if not success:
            return {}
        return self.response.json()
    #新增采购订单
    def post_new_purchase_order_new_produce(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        product_info =self.get_product_info(product_id)
        print product_info['product']['product_unit_id']
        url = self.base_url + 'api/purchase_orders.json'
        body = {
            'id':'',
            'supplier_id':'5509',
            'warehouse_id':warehouse_id,
            'category':'in',
            'number':'test-%s'% self.get_random_int(9999),
            'documented_at':self.get_today_str(),
            'delivered_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'total_deduction':'0.0000',
            'purchase_member_id':'13356',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'status':'approving',
            'supplier_address':'',
            'contact_id':'25318',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_address':'',
            'order_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'order_items_attributes[0][product_number]':product_info['product']['number'],
            'order_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'order_items_attributes[0][attr_names]':'',
            'order_items_attributes[0][product_id]':product_id,
            'order_items_attributes[0][modified]':'price',
            'order_items_attributes[0][name]':product_info['product']['name'],
            'order_items_attributes[0][spec]':'',#product_info['product']['name'],
            'order_items_attributes[0][unit]':product_info['product']['unit_name'],
            'order_items_attributes[0][quantity]':total_quantity,
            'order_items_attributes[0][price]':price,
            'order_items_attributes[0][price_with_tax]':price*1.1733,
            'order_items_attributes[0][discount]':'0.00',
            'order_items_attributes[0][batch_number]':'',
            'order_items_attributes[0][produced_at]':'',
            'order_items_attributes[0][expired_at]':'',
            'order_items_attributes[0][deduction]':'0.0000',
            'order_items_attributes[0][amount]':price*total_quantity,
            'order_items_attributes[0][tax_rate]':'17.33',
            'order_items_attributes[0][tax_amount]':price*total_quantity*0.1733,
            'order_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'order_items_attributes[0][note]':''
        }
        success = self.post_response_json(url, body, 'post new purchase order')
        if not success:
            return {}
        #if self.response.json()['status']['code'] == '200':
        if str(self.response.json()['status']['code']) == '200':
            self.purchase_order_id = self.response.json()['purchase_order']['id']
        print self.purchase_order_id
        #print self.purchase_order
        return self.response.json()['purchase_order']['id']
    #新增采购入库订单(直接)
    def post_new_purchase_order_in(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        #product_id=self.add_product()
        product_info =self.get_product_info(product_id)
        print product_info['product']['product_unit_id']
        url = self.base_url + 'api/purchases.json'
        body = {
             'id':'',
            'supplier_id':'5509',
            'warehouse_id': warehouse_id,
            'entry_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'in',
            'number':'CGRKD1704170001',
            'total_deduction':'0.0000',
            'total_amount':total_quantity*price,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount':total_quantity*price*1.1733,
            'total_tax_amount':round(total_quantity*price*0.1733,6),
            'total_amount_with_tax':total_quantity*price*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'purchase_member_id':'13356',
            'purchase_order_id':'',
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'product_items_attributes[0][product_id]':product_info['product']['id'],
            'product_items_attributes[0][name]':product_info['product']['name'],
            'product_items_attributes[0][product_number]':product_info['product']['number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product']['unit_name'],
            'product_items_attributes[0][quantity]': total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':round(price*1.1733,6),
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':round(price*total_quantity*0.1733,6),
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':'price_with_tax'
        }
        print 'wal%s' %body
        success = self.post_response_json(url, body, 'post new purchase order in')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code']) == '200':
            self.purchase_order_in = self.response.json()['purchase']['id']
            ##self.purchase_order_id =self.purchase_order['id']
            #print self.purchase_order['id']
        print self.purchase_order_in
        return self.purchase_order_in

    def get_purchase_new(self):
        url = self.base_url + 'purchase_orders/new'
        success = self.get_html(url, 'get purchase new')
        if not success:
            return False
        html_str = self.response.text
        print html_str
        soup = BeautifulSoup(html_str)
        div = soup.find(name='div', attrs={'data-react-class': 'PurchaseOrdersNew'})
        print json.loads(div['data-react-props'])
        #return json.loads(div['data-react-props'])
        print self.purchase_order.pop('deleted_at')
        print self.purchase_order.pop('order_id')
        print self.purchase_order.pop('approved_level')
        print self.purchase_order.pop('created_at')
        print self.purchase_order.pop('updated_at')
        print self.purchase_order.pop('creator_id')

        #print self.purchase_order['documented_at'] = self.get_today_str()
        #print self.purchase_order['delivered_at'] = self.get_today_str()

        #self.purchase_order['status'] = 'approving'

    def get_product_items_for_purchase(self, purchase_order_id):
        url = self.base_url + 'purchases/get_product_items?id=&order_id=%s' % purchase_order_id
        success = self.get_response_json(url, 'get product items for purhcase order %s' % purchase_order_id)
        if not success:
            return {}
        return self.response.json()
    #采购单生成采购入库单
    def make_new_purchase_wl(self,purchase_order_id,total_quantity,price):
        url = self.base_url + 'api/purchases.json'
        product_info =self.get_product_items_for_purchase(purchase_order_id)
        body= {
            'id':'',
            'supplier_id': product_info['supplier']['id'],
            'warehouse_id': product_info['warehouse']['id'],
            'entry_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'in',
            'number':'CGRKD1703290008',
            'total_deduction':'0.0000',
            'total_amount':total_quantity*price,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount':total_quantity*price*1.1733,
            'total_tax_amount':round(total_quantity*price*0.1733,6),
            'total_amount_with_tax':total_quantity*price*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'purchase_member_id':product_info['purchase_member']['id'],
            'purchase_order_id':product_info['product_items'][0]['orderable_id'],
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'product_items_attributes[0][order_item_id]':product_info['product_items'][0]['order_item_id'],
            'product_items_attributes[0][product_id]':product_info['product_items'][0]['product_id'],
            'product_items_attributes[0][name]':product_info['product_items'][0]['name'],
            'product_items_attributes[0][product_number]':product_info['product_items'][0]['product_number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product_items'][0]['unit'],
            'product_items_attributes[0][quantity]': total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':round(price*1.1733,6),
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':round(price*total_quantity*0.1733,6),
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':product_info['product_items'][0]['modified']
        }
        print 'lware%s' %body
        success = self.post_response_json(url, body, 'post new purchase order')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        #if self.response.json()['status']['code'] == '200':
        if str(self.response.json()['status']['code']) == '200':
            self.purchase_entry_id = self.response.json()['purchase']['id']
        return self.purchase_entry_id
    #获取库存信息及价格
    def get_product_price_warehouse_info(self, product_id):
        url = self.base_url + 'api/reporting/inventories.json?api/reporting/inventories.json?products_search[zero_inventory_filter]=&products_search[warehouse_id]=-1&products_search[product_category_id]=&products_search[product_id]=%s&products_search[Bkeyword]=&products_search[page]=1' % product_id
        #url = self.base_url + 'api/reporting/inventories.json? api/reporting/inventories.json?products_search[zero_inventory_filter]=&products_search[warehouse_id]=3907&products_search[product_category_id]=&products_search[product_id]=%s&products_search[Bkeyword]=&products_search[page]=1' % product_id
        print url
        success = self.get_response_json(url, 'get product %s price and warehouse_info' % product_id)
        if not success:
            return {}
        return self.response.json()

    def get_product_attr_groups(self):
        url = self.base_url + 'product_attr_groups/query?keyword='
        success = self.get_response_json(url, 'get product attr groups')

    def get_purchases_detail(self, bill_id):
        url = self.base_url + 'purchases/%s' % bill_id
        print url
        success = self.get_html(url, 'get purchases %s detail' % bill_id)
        #print self.response.json()
        return success

    def audit_purchasee_m(self,bill_id):
        url = self.base_url + 'purchases/%s' % bill_id

        body = {
            'purchase[status]': 'passed',
            'purchase[reason]': 'auto' + str(random.randint(1, 10000))
        }
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

    def audit_purchase(self, id=''):
        if len(str(id)) == 0:
            purchase_id = self.purchase_id
        else:
            purchase_id = id
        for i in range(3):
                self.audit_purchases(purchase_id)

    def get_product_items_for_purchase_back(self, purchase_back_order_id):
        url = self.base_url + 'purchases/%s/product_items' % purchase_back_order_id
        success = self.get_response_json(url, 'get product items for purhcase back %s' % purchase_back_order_id)
        if not success:
            return {}
        #print self.response.json()
        return self.response.json()
    #生成采购单退货单
    def post_new_purchase_back_order(self, product_id='', warehouse_id=3907,total_quantity=2,price =10.0000,purchase_back_order_id=''):
        product_info =self.get_product_items_for_purchase_back(purchase_back_order_id)
        #print product_info['product']['product_items']
        url = self.base_url + 'api/purchases.json'
        body = {
            'id':'',
            'supplier_id':'5509',
            'warehouse_id':warehouse_id,
            'entry_at':self.get_today_str(),
            'category':'out',
            'number':'wl-back-%s' %self.get_random_int(99999),
            'total_quantity':total_quantity,
            'total_deduction':'0.0000',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':purchase_back_order_id,
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'purchase_member_id':'13356',
            'purchase_order_id':'',
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'product_items_attributes[0][order_item_id]':product_info['product_items'][0]['order_item_id'],
            'product_items_attributes[0][product_id]':product_info['product_items'][0]['product_id'],
            'product_items_attributes[0][name]':product_info['product_items'][0]['name'],
            'product_items_attributes[0][product_number]':product_info['product_items'][0]['product_number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product_items'][0]['unit'],
            'product_items_attributes[0][quantity]':total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.000000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':price*1.1733,
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]': price*0.1733*total_quantity,
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':'quantity',
            'product_items_attributes[0][parent_id]':product_info['product_items'][0]['id']
        }
        print u'wangl%s' % body
        success = self.post_response_json(url, body, 'post  purchase back order')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code']) == '200':
            purchase_back_order = self.response.json()['purchase']['id']
        #    self.purchase_order_id =self.purchase_order['id']
        #    print self.purchase_order['id']
        return purchase_back_order
    #生成采购单退货单不关联采购订单
    def post_purchase_back_order_not_association(self, product_id='', warehouse_id=3907,total_quantity=2,price =10.0000):
        product_info =self.get_product_info(product_id)
        #print product_info['product']['product_items']
        url = self.base_url + 'api/purchases.json'
        body= {
            'id':'',
            'supplier_id': 5509,
            'warehouse_id': warehouse_id,
            'entry_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'out',
            'number':'CGRKD1703290008',
            'total_deduction':'0.0000',
            'total_amount':total_quantity*price,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount':total_quantity*price*1.1733,
            'total_tax_amount':round(total_quantity*price*0.1733,6),
            'total_amount_with_tax':total_quantity*price*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'purchase_member_id':'13356',
            'purchase_order_id':'',
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            #'product_items_attributes[0][order_item_id]':product_info['product_items'][0]['order_item_id'],
            'product_items_attributes[0][product_id]':product_id,
            'product_items_attributes[0][name]':product_info['product']['name'],
            'product_items_attributes[0][product_number]':product_info['product']['number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product']['product_unit_id'],
            'product_items_attributes[0][quantity]': total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':round(price*1.1733,6),
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':round(price*total_quantity*0.1733,6),
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':'price'
        }
        print body
        success = self.post_response_json(url, body, 'post  purchase back order')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            purchase_back_order = self.response.json()['purchase']['id']
        #    self.purchase_order_id =self.purchase_order['id']
        #    print self.purchase_order['id']
        print purchase_back_order
        return purchase_back_order
    #新增销售订单
    def post_new_sale_order(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        #product_id=self.add_product()
        product_info =self.get_product_info(product_id)
        print product_info['product']['product_unit_id']
        url = self.base_url + 'api/sale_orders.json'
        body = {
            'id':'',
            'customer_id':'20265',
            'warehouse_id':warehouse_id,
            'category':'out',
            'number':'test-%s'% self.get_random_int(9999),
            'documented_at':self.get_today_str(),
            'delivered_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'total_deduction':'0.0000',
            'seller_id':'194761',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'status':'approving',
            'contact_id':'25318',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_address':'',
            'address':'',
            'order_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'order_items_attributes[0][product_number]':product_info['product']['number'],
            'order_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'order_items_attributes[0][attr_names]':'',
            'order_items_attributes[0][product_id]':product_id,
            'order_items_attributes[0][modified]':'price',
            'order_items_attributes[0][name]':product_info['product']['name'],
            'order_items_attributes[0][spec]':'',#product_info['product']['name'],
            'order_items_attributes[0][unit]':product_info['product']['unit_name'],
            'order_items_attributes[0][quantity]':total_quantity,
            'order_items_attributes[0][price]':price,
            'order_items_attributes[0][price_with_tax]':price*1.1733,
            'order_items_attributes[0][discount]':'0.00',
            'order_items_attributes[0][batch_number]':'',
            'order_items_attributes[0][produced_at]':'',
            'order_items_attributes[0][expired_at]':'',
            'order_items_attributes[0][deduction]':'0.0000',
            'order_items_attributes[0][amount]':price*total_quantity,
            'order_items_attributes[0][tax_rate]':'17.33',
            'order_items_attributes[0][tax_amount]':price*total_quantity*0.1733,
            'order_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'order_items_attributes[0][note]':''
        }
        success = self.post_response_json(url, body, 'post new purchase order')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.sale_id =self.response.json()['sale_order']['id']
            #print self.purchase_order['id']
        print self.sale_id
    #销售订单一级审核
    def verify_sale_orders_first(self, order_id):
        url = self.base_url + 'sale_orders/%s' % order_id
        print url
        body = {
            'sale_order[status]':'second_approving',
            'sale_order[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass sale order %s' % order_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #销售订单二级审核
    def verify_sale_orders_sec(self, order_id):
        url = self.base_url + 'sale_orders/%s' % order_id
        print url
        body = {
            'sale_order[status]':'third_approving',
            'sale_order[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass sale order %s' % order_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
        #tmp_str = self.response.text
    #销售订单三级审核
    def verify_sale_orders_pass(self, order_id):
        url = self.base_url + 'sale_orders/%s' % order_id
        print url
        body = {
            'sale_order[status]':'passed',
            'sale_order[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass sale order %s' % order_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
        #tmp_str = self.response.text
    #销售出库单审核
    def verify_sale_orders_out_pass(self, sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        print url
        body = {
            'sale[status]':'passed',
            'sale[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit pass sale order out %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
        #tmp_str = self.response.text
    #销售退货单一级审核
    def verify_sale_orders_back_fir(self, sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        print url
        body = {
            'sale[status]':'second_approving',
            'sale[reason]':'fir'
        }
        print body
        success = self.put_response_json(url, body, 'audit  sale order back %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
        #tmp_str = self.response.text
    #销售退货单二级审核
    def verify_sale_orders_back_sec(self, sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        print url
        body = {
            'sale[status]':'third_approving',
            'sale[reason]':'sec'
        }
        print body
        success = self.put_response_json(url, body, 'audit  sale order back %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #销售退货单三级审核
    def verify_sale_orders_back_thi(self, sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        print url
        body = {
            'sale[status]':'passed',
            'sale[reason]':'thi'
        }
        print body
        success = self.put_response_json(url, body, 'audit  sale order back %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #其他一级入库单审核
    def verify_other_orders_in_fir(self,other_order_in_id):
        url = self.base_url + 'storageios/%s' % other_order_in_id
        print url
        body = {
            'storageio[status]':'second_approving',
            'storageio[reason]':''
        }
        print body
        success = self.put_response_json(url, body, 'audit  other order in %s' % other_order_in_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
     #其他二级入库单审核
    def verify_other_orders_in_sec(self,other_order_in_id):
        url = self.base_url + 'storageios/%s' % other_order_in_id
        print url
        body = {
            'storageio[status]':'third_approving',
            'storageio[reason]':''
        }
        print body
        success = self.put_response_json(url, body, 'audit  other order in %s' % other_order_in_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #其他三级入库单审核
    def verify_other_orders_in_pass(self,other_order_in_id):
        url = self.base_url + 'storageios/%s' % other_order_in_id
        print url
        body = {
            'storageio[status]':'passed',
            'storageio[reason]':''
        }
        print body
        success = self.put_response_json(url, body, 'audit  other order in %s' % other_order_in_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #调拨单三级入库单审核
    def verify_storage_transfers_pass(self,storage_transfers_order):
        url = self.base_url + 'storage_transfers/%s' % storage_transfers_order
        print url
        body = {
            'storage_transfer[status]':'passed',
            'storage_transfer[reason]':''
        }
        print body
        success = self.put_response_json(url, body, 'storage_transfers_order %s' % storage_transfers_order)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #采购入库单审核成功后作废
    def purchase_order_in_cancel (self,purchase_order_in_id):
        url = self.base_url + 'purchases/%s' % purchase_order_in_id
        print url
        body = {
            'purchase[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'purchase order in cancel %s' % purchase_order_in_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #调拨单废弃
    def storage_transfers_order_cancel(self,storage_transfers_order_id):
        url = self.base_url + 'storage_transfers/%s' % storage_transfers_order_id
        print url
        body = {
            'storage_transfer[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'storage transfers order id cancel %s' % storage_transfers_order_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #其他入库单废弃
    def other_order_cancel(self,other_order_id):
        url = self.base_url + 'storageios/%s' % other_order_id
        print url
        body = {
            'storageio[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'other order cancel %s' % other_order_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #采购退货单审核成功后作废
    def purchase_order_back_cancel (self,purchase_order_back_id):
        url = self.base_url + 'purchases/%s' % purchase_order_back_id
        print url
        body = {
            'purchase[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'purchase order back cancel %s' % purchase_order_back_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
     #销售出库单审核成功后作废
    def sale_order_out_cancel (self,sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        body = {
            'sale[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'sale order out cancel %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}

     #销售退货单审核成功后作废
    def sale_order_back_cancel (self,sale_order_out_id):
        url = self.base_url + 'sales/%s' % sale_order_out_id
        body = {
            'sale[status]':'deprecated',
        }
        print body
        success = self.put_response_json(url, body, 'sale order back cancel %s' % sale_order_out_id)
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
    #添加客户
    def add_customers(self):
        url = self.base_url + 'customers'
        print url
        body ={
            'utf8':'?',
            'type:':'',
            'customer[name]':'123-auto-%s'% self.get_random_int(9999),
            'customer[number]':'123-auto-%s'% self.get_random_int(9999),
            'customer[customer_type_id]':'1006',
            'customer[first_payment]':'0.0000',
            'customer[address]':'',
            'customer[assigner_id]':'194761',
            'customer[note]':'',
            'customer[contacts_attributes][0][name]':'',
            'customer[contacts_attributes][0][mobile]':'',
            'customer[contacts_attributes][0][telephone]':'',
            'customer[contacts_attributes][0][address]':'',
            'customer[contacts_attributes][0][is_primary]':'not_primary',
            'customer[contacts_attributes][0][is_primary]':'primary',
            'customer[contacts_attributes][0][note]':'',
            'customer[contacts_attributes][0][_destroy]':'false',
            'customer[contacts_attributes][0][org_id]':'209',
        }
        print body
        success = self.post_response_js(url, body,'add customer')
        if not success:
            return {}
        #return self.response.json()
        if not success:
            return {}
        print self.response.text
        tmp_str = self.response.text.split('data-id=\\\"')[1]
        print u'wangle%s' % tmp_str
        data_id = tmp_str.split('\\')[0]
        print data_id
    #获取销售订单商品详情
    def get_product_items_for_sale(self, sale_order_id):
        url = self.base_url + 'sales/get_product_items?id=&order_id=%s' % sale_order_id
        print url
        success = self.get_response_json(url, 'get product items for sale order %s' % sale_order_id)
        if not success:
            return {}
        return self.response.json()
    #新增销售出库订单（直接）
    def post_new_sale_order_out(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        product_info =self.get_product_info(product_id)
        url = self.base_url + 'api/sales.json'
        body = {
            'id':'',
            'customer_id':'20265',
            'warehouse_id':warehouse_id,
            'exited_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'out',
            'number':'test-%s'% self.get_random_int(9999),
            'total_deduction':'0.0000',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'address':'',
            'payment_amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_id':'',
            'contact_name':'',
            'contact_mobile':'',
            'contact_phone':'',
            'saler_id':'13356',
            'sale_order_id':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'product_items_attributes[0][product_id]':product_id,
            'product_items_attributes[0][name]':product_info['product']['name'],
            'product_items_attributes[0][product_number]':product_info['product']['number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',#product_info['product']['name'],
            'product_items_attributes[0][unit]':product_info['product']['unit_name'],
            'product_items_attributes[0][quantity]':total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':price*1.1733,
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':price*total_quantity*0.1733,
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'product_items_attributes[0][modified]':'price',
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
        }
        print body
        success = self.post_response_json(url, body, 'post new sale order out')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.sale_id =self.response.json()['sale']['id']
            #print self.purchase_order['id']
        print self.sale_id
        return self.sale_id
    #新增销售退货单（直接）
    def post_new_sale_order_out_not_association(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        product_info =self.get_product_info(product_id)
        url = self.base_url + 'api/sales.json'
        body = {
            'id':'',
            'customer_id':'20265',
            'warehouse_id':warehouse_id,
            'exited_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'in',
            'number':'test-%s'% self.get_random_int(9999),
            'total_deduction':'0.0000',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'address':'',
            'payment_amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_id':'',
            'contact_name':'',
            'contact_mobile':'',
            'contact_phone':'',
            'saler_id':'13356',
            'sale_order_id':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'product_items_attributes[0][product_id]':product_id,
            'product_items_attributes[0][name]':product_info['product']['name'],
            'product_items_attributes[0][product_number]':product_info['product']['number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',#product_info['product']['name'],
            'product_items_attributes[0][unit]':product_info['product']['unit_name'],
            'product_items_attributes[0][quantity]':total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':price*1.1733,
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':price*total_quantity*0.1733,
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product']['product_unit_id'],
            'product_items_attributes[0][modified]':'price_with_tax',
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
        }
        print body
        success = self.post_response_json(url, body, 'post new sale order out return not association')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.sale_id =self.response.json()['sale']['id']
            #print self.purchase_order['id']
        print self.sale_id
        return self.sale_id
    #销售单生成销售出库单
    def make_new_sale_order_out(self,sale_order_id,total_quantity,price):
        url = self.base_url + 'api/sales.json'
        product_info =self.get_product_items_for_sale(sale_order_id)
        body= {
            'id':'',
            'customer_id':'20265',
            'warehouse_id': product_info['warehouse']['id'],
            'exited_at':self.get_today_str(),
            'total_quantity':total_quantity,
            'category':'out',
            'number':'CGRKD1703290008',
            'total_deduction':'0.0000',
            'total_amount':total_quantity*price,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount':total_quantity*price*1.1733,
            'total_tax_amount':round(total_quantity*price*0.1733,6),
            'total_amount_with_tax':total_quantity*price*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id':'',
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'saler_id':'194761',
            'sale_order_id':sale_order_id,
            #'purchase_member_id':product_info['purchase_member']['id'],
            #'purchase_order_id':product_info['product_items'][0]['orderable_id'],
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'product_items_attributes[0][order_item_id]':product_info['product_items'][0]['order_item_id'],
            'product_items_attributes[0][product_id]':product_info['product_items'][0]['product_id'],
            'product_items_attributes[0][name]':product_info['product_items'][0]['name'],
            'product_items_attributes[0][product_number]':product_info['product_items'][0]['product_number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product_items'][0]['unit'],
            'product_items_attributes[0][quantity]': total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.0000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':round(price*1.1733,6),
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]':round(price*total_quantity*0.1733,6),
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':product_info['product_items'][0]['modified']
        }
        print 'lware%s' %body
        success = self.post_response_json(url, body, 'post new sale order out ')
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.sale_out_id = self.response.json()['sale']['id']
            print self.sale_out_id
        return self.sale_out_id
    #销售退货获取商品信息
    def get_product_items_for_sale_back(self, sale_out_order_id):
            url = self.base_url + 'sales/%s/product_items' % sale_out_order_id
            success = self.get_response_json(url, 'get product items for sale out  order %s' % sale_out_order_id)
            if not success:
                return {}
            #print self.response.json()
            return self.response.json()
    #生成销售退货单
    def post_new_purchase_sale_order_back(self, product_id='', warehouse_id=3907,total_quantity=2,price =10.0000,sale_out_order_id=''):
        product_info =self.get_product_items_for_sale_back(sale_out_order_id)
        #print product_info['product']['product_items']
        url = self.base_url + 'api/sales.json'
        body = {
            'id':'',
            'customer_id':'20265',
            'warehouse_id':warehouse_id,
            'exited_at':self.get_today_str(),
            'category':'in',
            'number':'wl-back-%s' %self.get_random_int(99999),
            'total_quantity':total_quantity,
            'total_deduction':'0.0000',
            'total_amount':price*total_quantity,
            'discount':'0.00',
            'deduction':'0.0000',
            'payment_amount': price*total_quantity*1.1733,
            'total_tax_amount':price*0.1733*total_quantity,
            'total_amount_with_tax':price*total_quantity*1.1733,
            'note':'',
            'address':'',
            'contact_address':'',
            'status':'approving',
            'parent_id': sale_out_order_id,
            'contact_name':'招商',
            'contact_mobile':'',
            'contact_phone':'021005240',
            'contact_id':'25318',
            'saler_id':'194761',
            'sale_order_id':'',
            'purchase_member_id':'13356',
            'purchase_order_id':'',
            'product_items_attributes[0][id]':'',
            'product_items_attributes[0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'product_items_attributes[0][order_item_id]':product_info['product_items'][0]['order_item_id'],
            'product_items_attributes[0][product_id]':product_info['product_items'][0]['product_id'],
            'product_items_attributes[0][name]':product_info['product_items'][0]['name'],
            'product_items_attributes[0][product_number]':product_info['product_items'][0]['product_number'],
            'product_items_attributes[0][attr_names]':'',
            'product_items_attributes[0][spec]':'',
            'product_items_attributes[0][unit]':product_info['product_items'][0]['unit'],
            'product_items_attributes[0][quantity]':total_quantity,
            'product_items_attributes[0][price]':price,
            'product_items_attributes[0][discount]':'0.00',
            'product_items_attributes[0][deduction]':'0.000000',
            'product_items_attributes[0][amount]':price*total_quantity,
            'product_items_attributes[0][price_with_tax]':price*1.1733,
            'product_items_attributes[0][tax_rate]':'17.33',
            'product_items_attributes[0][tax_amount]': price*0.1733*total_quantity,
            'product_items_attributes[0][amount_with_tax]':price*total_quantity*1.1733,
            'product_items_attributes[0][note]':'',
            'product_items_attributes[0][batch_number]':'',
            'product_items_attributes[0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'product_items_attributes[0][produced_at]':'',
            'product_items_attributes[0][expired_at]':'',
            'product_items_attributes[0][modified]':'quantity',
            'product_items_attributes[0][parent_id]':product_info['product_items'][0]['id']
        }
        print body
        success = self.post_response_json(url, body, 'post  sale order back %s' %sale_out_order_id)
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            sale_back_order = self.response.json()['sale']['id']
        #    self.purchase_order_id =self.purchase_order['id']
        #    print self.purchase_order['id']
        print sale_back_order
        return sale_back_order
    #新增其他入库单
    def post_other_order_in(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        product_info =self.get_product_info(product_id)
        print self.get_today_str
        url = self.base_url + 'api/storageios.json'
        print url
        body = {
            'storageio[id]':'',
            'storageio[warehouse_id]':warehouse_id,
            'storageio[number]:':'test-%s'% self.get_random_int(9999),
            'storageio[total_quantity]':total_quantity,
            'storageio[total_amount]':total_quantity*price,
            'storageio[storage_type]':'in',
            'storageio[storaged_at]':self.get_today_str_yymmddhm(),
            'storageio[note]':'',
            'storageio[check_id]':'',
            'storageio[status]':'approving',
            'storageio[product_items_attributes][0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'storageio[product_items_attributes][0][product_number]':product_info['product']['number'],
            'storageio[product_items_attributes][0][product_unit_id]':product_info['product']['product_unit_id'],
            'storageio[product_items_attributes][0][batch_number]':'',
            'storageio[product_items_attributes][0][produced_at]':'',
            'storageio[product_items_attributes][0][expired_at]':'',
            'storageio[product_items_attributes][0][attr_names]':'',
            'storageio[product_items_attributes][0][product_id]':product_id,
            'storageio[product_items_attributes][0][name]':product_info['product']['name'],
            'storageio[product_items_attributes][0][spec]':'',
            'storageio[product_items_attributes][0][unit]':product_info['product']['unit_name'],
            'storageio[product_items_attributes][0][quantity]':total_quantity,
            'storageio[product_items_attributes][0][price]':price,
            'storageio[product_items_attributes][0][amount]':total_quantity*price,
            'storageio[product_items_attributes][0][note]':'',
            'storageio[product_items_attributes][0][modified]':'price'

        }
        success = self.post_response_json(url, body, 'post other order in')
        print body
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.storageio_id =self.response.json()['storageio']['id']
            #print self.purchase_order['id']
        print self.storageio_id
        return self.storageio_id
    #新增其他出库单
    def post_other_order_out(self, product_id='', warehouse_id=3907,total_quantity=3,price =10.0000):
        #product_id=self.add_product()
        product_info =self.get_product_info(product_id)
        #print product_info['product']['product_unit_id']
        print self.get_today_str
        url = self.base_url + 'api/storageios.json'
        print url
        body = {
            'storageio[id]':'',
            'storageio[warehouse_id]':warehouse_id,
            'storageio[number]:':'test-%s'% self.get_random_int(9999),
            'storageio[total_quantity]':total_quantity,
            'storageio[total_amount]':total_quantity*price,
            'storageio[storage_type]':'out',
            'storageio[storaged_at]':self.get_today_str_yymmddhm(),
            'storageio[note]':'',
            'storageio[check_id]':'',
            'storageio[status]':'approving',
            'storageio[product_items_attributes][0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'storageio[product_items_attributes][0][product_number]':product_info['product']['number'],
            'storageio[product_items_attributes][0][product_unit_id]':product_info['product']['product_unit_id'],
            'storageio[product_items_attributes][0][batch_number]':'',
            'storageio[product_items_attributes][0][produced_at]':'',
            'storageio[product_items_attributes][0][expired_at]':'',
            'storageio[product_items_attributes][0][attr_names]':'',
            'storageio[product_items_attributes][0][product_id]':product_id,
            'storageio[product_items_attributes][0][name]':product_info['product']['name'],
            'storageio[product_items_attributes][0][spec]':'',
            'storageio[product_items_attributes][0][unit]':product_info['product']['unit_name'],
            'storageio[product_items_attributes][0][quantity]':total_quantity,
            'storageio[product_items_attributes][0][price]':price,
            'storageio[product_items_attributes][0][amount]':total_quantity*price,
            'storageio[product_items_attributes][0][note]':'',
            'storageio[product_items_attributes][0][modified]':'quantity'

        }
        success = self.post_response_json(url, body, 'post other order in')
        print body
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.storageio_out_id =self.response.json()['storageio']['id']
            #print self.purchase_order['id']
        print self.storageio_out_id
        return self.storageio_out_id
    #获取库存数量
    def get_product_items_for_check(self,warehouse_id,product_id):
            url = self.base_url + 'checks/new?warehouse_id=%s&category_id=&product_id=%s&inventory_filter=closed&_=1491445857642' %(warehouse_id,product_id)
            print url
            success = self.get_response_js(url, 'get product items for check')
            if not success:
                return {}
            #return self.response.json()
            if not success:
                return {}
            print self.response.text
            tmp_str = self.response.text.split('value=\\\"')[1]
            print u'wangle%s' % tmp_str
            amount = tmp_str.split('\\')[0]
            print amount
            return amount
    #新增盘盈单
    def post_inventory_profit(self, product_id='', warehouse_id=3907,add_amount=1):
        #product_id=self.add_product()
        product_info =self.get_product_info(product_id)
        amount = self.get_product_items_for_check(warehouse_id,product_id)

        url = self.base_url + 'checks'
        body = {
            'utf8':'?',
            'check[number]':'wl-auto%s' %self.get_random_int(9999),
            'check[warehouse_id]':warehouse_id,
            'check[product_category_id]':'',
            'check[product_id]':product_id,
            'check[inventory_filter]':'closed',
            'check[check_items_attributes][0][system_quantity]':amount,
            'check[check_items_attributes][0][quantity]':float(amount) + float(add_amount),
            'check[check_items_attributes][0][profit_and_loss]':add_amount,
            'check[check_items_attributes][0][note]':'auto%s' %self.get_random_int(99999),
            'check[check_items_attributes][0][_destroy]':'false',
            'check[check_items_attributes][0][product_id]':product_id,
            'check[check_items_attributes][0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'check[total_profit]':add_amount,
            'check[total_loss]':'0.00',
            'check[note]':'',
            'check[checked_at]':self.get_today_str_yymmddhm,
            'check[status]':'finished'

        }
        success = self.post_response_json(url, body, 'post inventory_profit %s' %add_amount)

        if not success:
            return {}
        print self.response.text
        tmp_str = self.response.text.split('checks/')[1].split('"')[0]
        print u'wangle%s' % tmp_str
        return  tmp_str
    #获取盘盈单信息
    def get_product_items_for_profit(self,profit_id):
            url = self.base_url + 'storageios/get_product_items?check_id=%s&type=profit' %profit_id
            print url
            success = self.get_response_js(url, 'get product items for profit')
            print self.response.json()
            if not success:
                return {}
            #return self.response.json()
            if not success:
                return {}
            return  self.response.json()
            #print self.response.json()['warehouse']['id']
    #盘盈其他入库单
    def post_profit_other_order_in(self,total_quantity=3,price =10.0000,profit_id = ''):
        #product_id=self.add_product()
        product_info = self.get_product_items_for_profit(profit_id)
        print product_info
        #print product_info['product']['product_unit_id']
        print self.get_today_str
        url = self.base_url + 'api/storageios.json'
        print url
        body = {
            'storageio[id]':'',
            'storageio[warehouse_id]':product_info['warehouse']['id'],
            'storageio[number]:':'test-%s'% self.get_random_int(9999),
            'storageio[total_quantity]':total_quantity,
            'storageio[total_amount]':total_quantity*price,
            'storageio[storage_type]':'profit',
            'storageio[storaged_at]':self.get_today_str_yymmddhm(),
            'storageio[note]':'',
            'storageio[check_id]':profit_id,
            'storageio[status]':'approving',
            'storageio[product_items_attributes][0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'storageio[product_items_attributes][0][product_number]':product_info['product_items'][0]['product_number'],
            'storageio[product_items_attributes][0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'storageio[product_items_attributes][0][batch_number]':'',
            'storageio[product_items_attributes][0][produced_at]':'',
            'storageio[product_items_attributes][0][expired_at]':'',
            'storageio[product_items_attributes][0][attr_names]':'',
            'storageio[product_items_attributes][0][product_id]':product_info['product_items'][0]['product_id'],
            'storageio[product_items_attributes][0][name]':product_info['product_items'][0]['name'],
            'storageio[product_items_attributes][0][spec]':'',
            'storageio[product_items_attributes][0][unit]':product_info['product_items'][0]['unit'],
            'storageio[product_items_attributes][0][quantity]':total_quantity,
            'storageio[product_items_attributes][0][price]':price,
            'storageio[product_items_attributes][0][amount]':total_quantity*price,
            'storageio[product_items_attributes][0][note]':'',
            'storageio[product_items_attributes][0][modified]':'quantity'

        }
        success = self.post_response_json(url, body, 'post profit other order in')
        print body
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.storageio_out_id =self.response.json()['storageio']['id']
            #print self.purchase_order['id']
        print self.storageio_out_id
        return self.storageio_out_id
    #新增盘亏单
    def post_inventory_losses(self, product_id='', warehouse_id=3907,reduce_amount=-1):
        #product_id=self.add_product()
        product_info =self.get_product_info(product_id)
        amount = self.get_product_items_for_check(warehouse_id,product_id)

        url = self.base_url + 'checks'
        body = {
            'utf8':'?',
            'check[number]':'wl-auto%s' %self.get_random_int(9999),
            'check[warehouse_id]':warehouse_id,
            'check[product_category_id]':'',
            'check[product_id]':product_id,
            'check[inventory_filter]':'closed',
            'check[check_items_attributes][0][system_quantity]':amount,
            'check[check_items_attributes][0][quantity]':float(amount) + float(reduce_amount),
            'check[check_items_attributes][0][profit_and_loss]':reduce_amount,
            'check[check_items_attributes][0][note]':'auto%s' %self.get_random_int(99999),
            'check[check_items_attributes][0][_destroy]':'false',
            'check[check_items_attributes][0][product_id]':product_id,
            'check[check_items_attributes][0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'check[total_profit]':'',
            'check[total_loss]':reduce_amount,
            'check[note]':'',
            'check[checked_at]':self.get_today_str_yymmddhm,
            'check[status]':'finished'

        }
        success = self.post_response_json(url, body, 'post inventory_losses %s' %reduce_amount)

        if not success:
            return {}
        print self.response.text
        tmp_str = self.response.text.split('checks/')[1].split('"')[0]
        return  tmp_str
    #获取盘亏单信息
    def get_product_items_for_lose(self,loss_id):
            url = self.base_url + 'storageios/get_product_items?check_id=%s&type=loss' %loss_id
            print url
            success = self.get_response_js(url, 'get product items for loss')
            print self.response.json()
            if not success:
                return {}
            #return self.response.json()
            if not success:
                return {}
            return  self.response.json()
    #新增其他盘亏入库单
    def post_lose_other_order_out(self,total_quantity=3,price =10.0000,lose_id = ''):
        #product_id=self.add_product()
        product_info = self.get_product_items_for_lose(lose_id)
        print product_info['product_items'][0]['product_attr_group_id']
        #print product_info['product']['product_unit_id']
        print self.get_today_str
        url = self.base_url + 'api/storageios.json'
        print url
        body = {
            'storageio[id]':'',
            'storageio[warehouse_id]':product_info['warehouse']['id'],
            'storageio[number]:':'test-%s'% self.get_random_int(9999),
            'storageio[total_quantity]':total_quantity,
            'storageio[total_amount]':total_quantity*price,
            'storageio[storage_type]':'loss',
            'storageio[storaged_at]':self.get_today_str_yymmddhm(),
            'storageio[note]':'',
            'storageio[check_id]':lose_id,
            'storageio[status]':'approving',
            'storageio[product_items_attributes][0][id]':'',
            'storageio[product_items_attributes][0][product_attr_group_id]':product_info['product_items'][0]['product_attr_group_id'],
            'storageio[product_items_attributes][0][product_number]':product_info['product_items'][0]['product_number'],
            'storageio[product_items_attributes][0][product_unit_id]':product_info['product_items'][0]['product_unit_id'],
            'storageio[product_items_attributes][0][batch_number]':'',
            'storageio[product_items_attributes][0][produced_at]':'',
            'storageio[product_items_attributes][0][expired_at]':'',
            'storageio[product_items_attributes][0][attr_names]':'',
            'storageio[product_items_attributes][0][product_id]':product_info['product_items'][0]['product_id'],
            'storageio[product_items_attributes][0][name]':product_info['product_items'][0]['name'],
            'storageio[product_items_attributes][0][spec]':'',
            'storageio[product_items_attributes][0][unit]':product_info['product_items'][0]['unit'],
            'storageio[product_items_attributes][0][quantity]':total_quantity,
            'storageio[product_items_attributes][0][price]':price,
            'storageio[product_items_attributes][0][amount]':total_quantity*price,
            'storageio[product_items_attributes][0][note]':'',
            'storageio[product_items_attributes][0][modified]':'quantity'

        }
        success = self.post_response_json(url, body, 'post lose other order out')
        print body
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.storageio_out_id =self.response.json()['storageio']['id']
            #print self.purchase_order['id']
        print self.storageio_out_id
        return self.storageio_out_id
    #新增调拨单
    def post_storage_transfers_order(self,total_quantity=5.000000,from_warehouse_id=3907,to_warehouse_id=3916,product_id=''):
        #product_id=self.add_product()
        product_info = self.get_product_info(product_id)
        url = self.base_url + 'api/storage_transfers.json'
        print url
        body = {
            'storage_transfer[id]':'',
            'storage_transfer[from_warehouse_id]':from_warehouse_id,
            'storage_transfer[to_warehouse_id]':to_warehouse_id,
            'storage_transfer[transferred_at]':self.get_today_str_yymmddhm(),
            'storage_transfer[total_quantity]':total_quantity,
            'storage_transfer[number]:':'test-%s'% self.get_random_int(9999),
            'storage_transfer[note]':'',
            'storage_transfer[status]':'approving',
            'storage_transfer[product_items_attributes][0][product_attr_group_id]':product_info['product']['product_attr_groups_attributes'][0]['id'],
            'storage_transfer[product_items_attributes][0][product_number]':product_info['product']['number'],
            'storage_transfer[product_items_attributes][0][product_unit_id]':product_info['product']['unit_id'],
            'storage_transfer[product_items_attributes][0][batch_number]':'',
            'storage_transfer[product_items_attributes][0][produced_at]':'',
            'storage_transfer[product_items_attributes][0][expired_at]':'',
            'storage_transfer[product_items_attributes][0][attr_names]':'',
            'storage_transfer[product_items_attributes][0][product_id]':product_info['product']['product_attr_groups_attributes'][0]['product']['id'],
            'storage_transfer[product_items_attributes][0][name]':product_info['product']['name'],
            'storage_transfer[product_items_attributes][0][spec]':'',
            'storage_transfer[product_items_attributes][0][unit]':product_info['product']['unit'],
            'storage_transfer[product_items_attributes][0][quantity]':total_quantity,
            'storage_transfer[product_items_attributes][0][note]':'',
            'storage_transfer[product_items_attributes][0][modified]':'quantity'

        }
        success = self.post_response_json(url, body, 'post storage transfers order')
        #print body
        #if not success:
            #return {}
        #return self.response.json()
        print self.response.json()
        if str(self.response.json()['status']['code'])  == '200':
            self.storage_transfer_id =self.response.json()['storage_transfer']['id']
            #print self.purchase_order['id']
        print self.storage_transfer_id
        return self.storage_transfer_id

    def get_reporting_inventories(self,product_id):
        url = self.base_url + 'api/reporting/inventories.json?pproduct_id%5D=%s'
        #api/reporting/inventories.json?products_search%5Bzero_inventory_filter%5D=&products_search%5Bwarehouse_id%5D=-1&products_search%5Bproduct_category_id%5D=&products_search%5' \
                              #'Bproduct_id%5D=124520&products_search%5Bkeyword%5D=&products_search%5Bpage%5D=1'
    #获取应付列表
    def get_funds_payment(self):
        url = self.base_url+'funds/payments'
        print url
        #http://test.ikjxc.com/api/products/124488
        #success = self.get_response_json(url, 'get product info ' )
        success = self.get_response_js(url,'get')
        result_list = re.findall(pattern="data-id=(.*?)id=", string=self.response.text)
        print result_list
        id_list = []
        for a_str in result_list:
            id_list.append(a_str[2:-3])
        print len(id_list)
        print id_list
        print id_list[0]
        if not success:
            return {}
        return id_list[0]
    #获取应付详情
    def get_funds_payment_content(self,payments_ids):
        url = self.base_url+'funds/batch_payments/new?payments_ids=%s&selected_supplier_id=5509'% payments_ids
        print url
        success = self.get_response_js(url,'get')
        str = self.response.text
        tmp_str = str.split(u'<span class="td-wrapper">采购入库单')[1]
        #tmp_str = str.split(u'<label> 付款日期：')[1]
        tmp_str = tmp_str.split('<td data-control-input="number"')[0]
        print tmp_str
        result_list = re.findall(pattern='''<span class="td-wrapper">(.*?)</span>''', string=tmp_str)
        print result_list[2]
        amount_payable =result_list[1]
        amount_paid = result_list[2]
        amount_of_payment = result_list[3]
        tmp_str = str.split(u'data-toggle="tooltip" title="删除">')[1]
        result_list1 = re.findall(pattern='''value="(.*?)" class=''', string=tmp_str)
        a = result_list1[0]
        result_list.append(a)
        return result_list

    def get_tr_info_from_js(self, html_str):
        print html_str
        html_new = html_str.replace('\\"', '"')
        html_new = html_new.replace('<\/', '</')
        html_soup = BeautifulSoup(html_new)
        tr_list = html_soup.findAll('tr')
        result_list = []
        key_list = ['id', 'data_id', 'class']
        for a_tr in tr_list:
            a_tr_result = {}
            for key in key_list:
                a_tr_result[key] = a_tr.get(key)
            td_list = a_tr.findAll('td')
            td_content_list = []
            for a_td in td_list:
                a_td_result = {}
                for key in key_list:
                    a_td_result[key] = a_td.get(key)
                a_td_result['content'] = {}

                # td的文字内容
                a_td_result['content']['text'] = a_td.string

                # 处理超链接， 给出链接地址，文字
                a_list = a_td.findAll('a')
                a_result_list = []
                for a_a in a_list:
                    a_a_result = {}
                    for key in key_list:
                        a_a_result[key] = a_a.get(key)
                    a_a_result['href'] = a_a.get('href')
                    a_a_result['text'] = a_a.string
                    a_result_list.append(a_a_result)
                # print a_result_list
                a_td_result['content']['a'] = a_result_list

                # 处理span内的内容
                span_list = a_td.findAll('span')

                span_result_list = []
                for a_span in span_list:

                    a_span_result = {}
                    for key in key_list:
                        a_span_result[key] = a_span.get(key)
                    a_span_result['text'] = a_span.string
                    # print a_span_result
                    span_result_list.append(a_span_result)
                # print span_result_list
                a_td_result['content']['span'] = span_result_list

                td_content_list.append(a_td_result)
            # print td_content_list
            a_tr_result['td_list'] = td_content_list

            result_list.append(a_tr_result)

        return result_list




     #获取应付列表

    def get_funds_payment_list(self,purchase_entry_id):
        url = self.base_url+'funds/payments?_=1494507847918'
        print url
        success = self.get_response_js(url,'get')
        html_str = self.response.text
        #print html_str
        tr_list = self.get_tr_info_from_js(html_str)
        print tr_list
        result_list = []
        for item in tr_list:
            #print item['td_list'][2]['content']['a'][0]['href']
            if len(item['td_list']) >= 2 and len(item['td_list'][2]['content']['a']) >= 1 and item['td_list'][2]['content']['a'][0]['href'] =='/purchases/%s' %purchase_entry_id:
            #print item['td_list'][2]['content']['a'][0]['href']
        #    if len(item['td_list']) >= 2 and len(item['td_list'][1]['content']['a']) >= 1 and item['td_list'][1]['content']['a'][0]['href'] == '/funds/batch_payments/new?payments_ids=9639&selected_supplier_id=5509':
        #        print item['td_list'][6]['content']['span'][0]['text']
                total_amount =item['td_list'][6]['content']['span'][0]['text']
                #print total_amount
                result_list.append(total_amount)
                exist_amount = item['td_list'][7]['content']['span'][0]['text']
                #print exist_amount
                result_list.append(exist_amount)
                a = item['td_list'][8]['content']['text']
                unpaid_amount = (a.split())[1]
                #print unpaid_amount
                result_list.append(unpaid_amount)
        #print result_list
        return result_list

    #应付 付款
    def funds_payments(self, payments_ids=9495,pay_funds=1,fund_account_amount = 3 ):
        result_list = self.get_funds_payment_content(payments_ids)
        url = self.base_url + 'funds/batch_payments'
        body = {
            'utf8':'✓',
            'supplier_id':'5509',
            'operator_id':'194761',
            'paid_on':self.get_today_str(),
            'number': 'wl-auto%s' %self.get_random_int(9999),
            'payments[0][number]':result_list[3],
            'payments[0][id]':payments_ids,
            'payments[0][batch_payment_amount]':pay_funds,
            'payment_amount_with_decimal':pay_funds,
            'fund_payment_amount':'',
            'fund_accounts[0][id]':'7252',
            'fund_accounts[0][fund_account_amount]':fund_account_amount,
            'fund_accounts[0][fund_account_note]':'',
            'paid_amount_with_decimal':fund_account_amount,
            'note':'',
            'total_amount':fund_account_amount-pay_funds

        }
        success = self.post_response_json(url, body, 'funds pay ')
        if not success:
            return {}
        #print self.response.text
        tmp_str = self.response.text.split('batch_payments/')[1].split('"')[0]
        #print tmp_str
        return  tmp_str

    #付款流水删除
    def funds_payments_delete(self, paymentflow_id=1910 ):
        url = self.base_url + 'funds/batch_payments/%s' % paymentflow_id

        success = self.delete_response_json(url, 'paymentflow %s delete' % paymentflow_id )
        if str(self.response.json()['status']['code'])  != '200':
            print self.response.json()
            return False
        elif 'status' in self.response.json():
                print self.response.json()['status']['message']
        return True
    #应付反结案
    def withdraw_force_close(self,pay_id):
        url = self.base_url + 'funds/payments/%s/withdraw_force_close' % pay_id
        body = {
            'status':''

        }
        success = self.put_response_json(url,body, ' %s withdraw_force_close' % pay_id )
        if not success:
            return {}
        return True
    #应付结案
    def force_close(self,pay_id):
        url = self.base_url + 'funds/payments/%s/force_close' % pay_id
        body = {
            'status':''

        }
        success = self.put_response_json(url,body, ' %s force_close' % pay_id )
        if not success:
            return {}
        return True


    def set_cookie(self, cookie):
        self.cookie_given = cookie

    def set_csrf(self, csrf):
        self.csrf = csrf
        print self.csrf

if __name__ == '__main__':
    a_purchase = OrderPurchase()

    csrf = 'cOC8grWptak98VaueUg5Ob01ix71Km9G940k3mbWIEXTw3H3de5dnZmqqwqvB581AmIg4LoQkttsIf8tNB1lMA=='
    cookie = '_invoicing_session=RFQ0M2dTMm9YbmtZVEdiQlZ6MFpHNzRpcDdJK3R0RFBpaVp1NXlkcVFjWklFMUh3OC9xWjhiV242R3NHMVptN3R5Mzg5Zkg0RUtzajNxZWU4VVZZMm50TFhiZk5FNUN6dmVaOUQycU9vRS9Pc21nRlB4TXAzM2FWaS80TFNkUzJaYnpuWlZVVjNLQUN4eko3TXc3NWhtVThUM1NGeGd4eEJ4MzNGSDJXYjkrbHNjLzhsZnBoZGRNK29hWnRxcTRJUDRuS2dwWjFIMEhvMWxTWXpyeW0zRWs4cFZWMCtzekdhemtDUkViMEY5M3ZOZmFxUVpIeDhpSE11WC8xbDkzL3FhS0Z4Sk8wUnVXY0ZQNTVrWkp2SXlpZFM1Yi9ZQXNvY2lNUWtMVGVUYU9PamVkdUlHSVFPR2xmY04xUEhkenEtLVlJQW9taVM5djZrVmM3Z1NMKzh6Z3c9PQ%3D%3D--514b2a1f66c8a925a08ca46b1f71d1a1b0035c83; path=/; HttpOnly'
    a_purchase.set_cookie(cookie)
    a_purchase.set_csrf(csrf)

    #a_purchase.login()
    #product_id= a_purchase.add_product()
    #print product_id
    #a_purchase.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=3907,total_quantity=10,price =20.000)
    #order_id = a_purchase.purchase_order_id
    #print order_id
    #a_purchase.get_purchase_orders_detail(order_id)
    #a_purchase.verify_purchase_orders_first(order_id)
    #a_purchase.verify_purchase_orders_sec(order_id)
    #a_purchase.verify_purchase_orders_pass(order_id)
    #bill_id = a_purchase.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=2.000000,price=10.000000)
    #a_purchase.audit_purchasee_m(bill_id)
    #a_purchase.get_product_price_warehouse_info(product_id)
    #a_purchase.get_product_items_for_purchase_back(order_id)
    #purchase_back_order = a_purchase.post_new_purchase_back_order(product_id=123, warehouse_id=3907,total_quantity=2,price =10.0000,purchase_back_order_id=bill_id)
    #purchase_back_order = a_purchase.post_new_purchase_back_order(product_id=124520, warehouse_id=3907,total_quantity=2,price =10.0000,purchase_back_order_id='')
    #a_purchase.post_purchase_back_order_not_association(product_id=124520, warehouse_id=3907,total_quantity=2,price =10.0000)
    #print purchase_back_order
    #a_purchase.verify_purchase_orders_back_pass(purchase_back_order)
    #a_purchase.post_new_sale_order(product_id=product_id, warehouse_id=3907,total_quantity=10,price =10.0000)
    #a_purchase.verify_sale_orders_first(order_id=a_purchase.sale_id)
    #a_purchase.verify_sale_orders_sec(order_id=a_purchase.sale_id)
    #a_purchase.verify_sale_orders_pass(order_id=a_purchase.sale_id)
    #a_purchase.make_new_sale_order_out(sale_order_id =a_purchase.sale_id,total_quantity=2,price=10.0000)
    #a_purchase.verify_sale_orders_out_pass(sale_order_out_id=a_purchase.sale_out_id)
    #sale_back_order = a_purchase.post_new_purchase_sale_order_back( warehouse_id=3907,total_quantity=2,price =10.0000,sale_out_order_id=a_purchase.sale_out_id)
    #print sale_back_order
    #a_purchase.get_sale_orders_back_detail(sale_back_order)
    #a_purchase.verify_sale_orders_back_fir(sale_back_order)
    #a_purchase.verify_sale_orders_back_sec(sale_back_order)
    #a_purchase.verify_sale_orders_back_thi(sale_back_order)
    #a_purchase.post_other_order_in(product_id=product_id,warehouse_id=3907,total_quantity=100,price =10.0000)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.post_other_order_in(product_id=product_id,warehouse_id=3903,total_quantity=50,price =8.0000)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_id)
    #a_purchase.post_other_order_out(product_id='124520',warehouse_id=3907,total_quantity=2,price =10.0000)
    #a_purchase.verify_other_orders_in_pass(a_purchase.storageio_out_id)
    #a_purchase.get_product_items_for_check(warehouse_id=3907,product_id=124520)
    #profit_id = a_purchase.post_inventory_profit(product_id=124520, warehouse_id=3907,add_amount=1)
    #a_purchase.get_product_items_for_profit(profit_id)
    #profit_in_id =a_purchase.post_profit_other_order_in(total_quantity=2,price =10.0000,profit_id=profit_id)
    #a_purchase.verify_other_orders_in_fir(profit_in_id)
    #a_purchase.verify_other_orders_in_sec(profit_in_id)
    #a_purchase.verify_other_orders_in_pass(profit_in_id)
    #losses_id = a_purchase.post_inventory_losses(product_id=124520, warehouse_id=3907,reduce_amount=-10)
    #print losses_id
    #losses_out_id = a_purchase.post_lose_other_order_out(total_quantity=3,price =1000.0000,lose_id =losses_id )
    #a_purchase.verify_other_orders_in_pass(losses_out_id)
    #a_purchase.get_product_info(product_id=124520)
    #
    #a_purchase.post_storage_transfers_order(total_quantity=3,from_warehouse_id=3907,to_warehouse_id=3903,product_id=product_id)
    #a_purchase.verify_storage_transfers_pass(a_purchase.storage_transfer_id)
    #a_purchase.post_new_purchase_order_in(product_id='124520', warehouse_id=3907,total_quantity=3,price =10.0000)
    #a_purchase.post_purchase_back_order_not_association(product_id=124520, warehouse_id=3907,total_quantity=2,price =10.0000)
    #a_purchase.post_new_sale_order_out(product_id='124520', warehouse_id=3907,total_quantity=3,price =10.0000)
    #a_purchase.post_new_sale_order_out_not_association( product_id='124520', warehouse_id=3907,total_quantity=3,price =10.0000)
    #a_purchase.purchase_order_in_cancel(purchase_order_in_id=11662)
    #a_purchase.purchase_order_back_cancel(purchase_order_back_id=11658)
    #a_purchase.sale_order_out_cancel(sale_order_out_id=14719)
    #a_purchase.sale_order_back_cancel(sale_order_out_id=14719)
    #a_purchase.storage_transfers_order_cancel(storage_transfers_order_id=5292)
    #a_purchase.other_order_cancel(other_order_id=5282)

    #a_purchase.get_funds_payment()
    #a_purchase.get_funds_payment_content(9429)
    #a_purchase.get_purchases_detail(11813)
    #a_purchase.funds_payments()
    #a_purchase.funds_payments_delete( a_purchase.funds_payments())
    #a_purchase.get_funds_payment_list()
    #a_purchase.withdraw_force_close(9961)
    #a_purchase.add_customers()

    #product_id =124520
    #a_purchase.post_new_purchase_order_new_produce(product_id=product_id, warehouse_id=3903,total_quantity=3,price =4.0000)
    #order_id = a_purchase.purchase_order_id
    #a_purchase.get_purchase_orders_detail(order_id)
    #a_purchase.verify_purchase_orders_first(order_id)
    #a_purchase.verify_purchase_orders_sec(order_id)
    #a_purchase.verify_purchase_orders_pass(order_id)
    #bill_id = a_purchase.make_new_purchase_wl(purchase_order_id=order_id,total_quantity=3.00,price=8.0000)
    #a_purchase.audit_purchasee_m(bill_id)
    #a_purchase.get_product_price_warehouse_info(product_id)

    #for i in range(3):
    #    a_purchase.audit_purchase_orders(bill_id)

    #a_purchase.get_purchases_new(1535)

    #a_purchase.get_product_items_for_purchase(1518)
    #a_purchase.post_new_purchase_order_new_produce()
    #a_purchase.get_purchases_detail(11396)
    a_purchase.get_funds_payment()
