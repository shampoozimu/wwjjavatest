from crm.approvals.driver import BusinessMessage
from testCase.component.oauth import CrmDingdingDeploy, Business
from testCase.component.confiuration import SettingFactory, ServerEnum, EnvironmentEnum, PlatformEnum

SettingFactory.instance(ServerEnum.CRM, EnvironmentEnum.TEST, PlatformEnum.钉钉)

oauth = CrmDingdingDeploy(Business.商机)
oauth.login({"username": "15722222222", "password": "Ik123456", "id": "2225241"})
oauth.apply(BusinessMessage())
