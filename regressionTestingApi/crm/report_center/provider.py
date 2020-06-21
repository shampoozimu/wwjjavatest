from crm.utils import AndroidDeploy, PrivateDeploy, DingdingDeploy, PcDeploy
from testCase.component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum

# 该文件为所有审批功能的数据提供者（approval）
# PC/Android/IOS大部分用户及配置信息为公用
# 所有公用配置信息存储在IOS下
# PC专用用户存储在PC下
users = {EnvironmentEnum.私有化: {PlatformEnum.IOS: [{"id": "2223353", "username": "13866666666 ", "name": "用户11", "authority": "超管", "department": ""}]},
         EnvironmentEnum.TEST: {PlatformEnum.IOS: [{"id": "5501614", "username": "13660139205 ", "name": "用户11", "authority": "超管", "department": "5502686"}]},
         EnvironmentEnum.STAGE: {PlatformEnum.IOS: [{"id": "5000479", "username": "11188888888 ", "name": "用户11", "authority": "超管", "department": ""}]}}

oauth_classes = {
    EnvironmentEnum.私有化: {
        PlatformEnum.IOS: AndroidDeploy,
        PlatformEnum.ANDROID: AndroidDeploy,
        PlatformEnum.PC: PrivateDeploy
    },
    EnvironmentEnum.TEST: {
        PlatformEnum.钉钉: DingdingDeploy,
        PlatformEnum.IOS: AndroidDeploy,
        PlatformEnum.ANDROID: AndroidDeploy,
        PlatformEnum.PC: PcDeploy
    },
    EnvironmentEnum.STAGE: {
        PlatformEnum.IOS: AndroidDeploy,
        PlatformEnum.ANDROID: AndroidDeploy,
        PlatformEnum.PC: PcDeploy
    }
}



data = [
    # 合同汇总表
    [{"authority": "超管", "amount": 100, "sign_date": "2019-05-10", "start_at": "2019-05-10", "end_at": "2019-05-30"}]
]
