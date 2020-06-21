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

# test环境调试
const.BASE_URL = 'https://lixiaojxc-test.ikcrm.com/'
const.SIGN_IN_BASE_URL = 'https://lixiaojxc-test.ikcrm.com/api/auth/get_token.json'

# 独立版本
const.USER = [{'username': '13701649175', 'password': 'Aa123456','role':'超管'}]
