#coding:utf-8

class const:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value):
      if name in self.__dict__:
          raise self.ConstError("can't change const %s" % name)
      if not name.isupper():
          raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
      self.__dict__[name] = value

const = const()
const.BASE_URL = 'http://ikstaging.e.ikcrm.com'
const.SIGN_IN_BASE_URL = 'http://ikstaging.www.ikcrm.com/users/sign_in'
const.H5_BASE_URL = 'http://ding-staging.ikcrm.com/api/v2'



# const.REPORT_TIME = ['all', 'today','week','month','quarter','year','other']
# const.SCOPE = ['all_own', 'my_own', 'my_assist']
# const.DUPLICATE = ['customer', 'lead', 'contact']
# const.USER = [{'username': '13023195853', 'password': '111111'}]
# const.CUSTOMER_ADD_ASSIST_USER_OPERATION_SELECTION = ['append_assist_user', 'replace_assist_user', 'remove_assist_user']
#
# authorization = 'Token token="e98f4bc2a3af26febcbe1de293a5738c",access_token="9ad4a66396ac9fdd8161f77a4b9e0b7cc38c192e4ceccfcbc40fb2fccc85e544066f743e33726c51b2223b",device="dingtalk",version_code="3.13.2"'
# a_ikcrm.set_authorization(authorization)

#定义邮件发送所需要的参数
sender = "testreport@ikcrm.com"
receiver = ["wang.l@ikcrm.com","you.mq@ikcrm.com","li.jc@ikcrm.com"]
username = "testreport@ikcrm.com"
password = "eKcaRCuWYVuMv77y"