from commons.const import const
from testCase.performance.revisit_logs import customer_revisit_logs
from testCase.performance.revisit_logs import contracts_revisit_logs
from testCase.performance.revisit_logs import lead_revisit_logs
from testCase.performance.revisit_logs import opportunities_revisit_logs

class all_revisit_logs:
    def __init__(self):
        self.base_url = const.BASE_URL
        self.base_url2 = const.SIGN_IN_BASE_URL
        self.csrf = ''
        self.cookie = ''
        # self.userinfo_super = {'username': '15639356523', 'password': 'Ab123456','role':'超管'}
        self.userinfo_super = {'username': '18049905933', 'password': 'Ik123456', 'role': '超管'}
        self.date_list = ['2018-01-10 02:51:58', '2018-03-10 02:51:58', '2018-05-10 02:51:58', '2018-07-10 02:51:58',
                          '2018-09-10 02:51:58 ', '2018-11-10 02:51:58']

        # self.total_amount_list = [[110, -20], [260, -220], [310, 220], [410, 420], [510, -520], [1, 2], [200, 100],
        #                           [220, 230]]
        self.userinfo_list = const.USER
        self.token = ''

        pass

    def revisit_logs(self):
        opportunities_revisit=opportunities_revisit_logs.Opportunities_revisit_logs()
        opportunities_revisit.opportunitie_revisit_logs()

        customer_revisit=customer_revisit_logs.Customers_revisit_logs()
        customer_revisit.customer_revisit_logs()

        contracts_revisit=contracts_revisit_logs.contracts_revisit_logs()
        contracts_revisit.contracts_revisit_logs()

        lead_revisit=lead_revisit_logs.Lead_revisit_logs()
        lead_revisit.lead_revisit_logs()


if __name__ == '__main__':
    _all_revisit_logs =all_revisit_logs()
    _all_revisit_logs.revisit_logs()











