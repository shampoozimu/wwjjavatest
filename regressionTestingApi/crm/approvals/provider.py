from crm.approvals.framework import MultistepEnum, ResultEnum
from crm.utils import PcDeploy, AndroidDeploy, PrivateDeploy, DingdingDeploy
from testCase.component.confiuration import ServerEnum, EnvironmentEnum, PlatformEnum

# 该文件为所有审批功能的数据提供者（approval）
# PC/Android/IOS大部分用户及配置信息为公用
# 所有公用配置信息存储在IOS下
# PC专用用户存储在PC下
users = {
    EnvironmentEnum.私有化: {
        PlatformEnum.IOS: [{"id": "2223346", "username": "15666666664", "name": "用户1", "director": {"username": "13898981111"}, "authority": ["applier"], "department": "5434"},
                           {"id": "2223340", "username": "13898981111", "name": "用户2", "director": {"username": "13612344321"}},
                           {"id": "2223339", "username": "13612344321", "name": "用户3", "director": {"username": "15932147413"}, "authority": ["normal"]},
                           {"id": "2223345", "username": "15932147413", "name": "用户4", "director": {"username": "13816393837"}, "authority": ["normal"]},
                           {"id": "2223347", "username": "13816393837", "name": "用户5", "director": {"username": "13012345678"}},
                           {"id": "2223341", "username": "13012345678", "name": "用户6", "director": {"username": "15800000000"}},
                           {"id": "2223349", "username": "15800000000", "name": "用户7", "director": {"username": "13677777777"}},
                           {"id": "2223351", "username": "13677777777", "name": "用户8"},
                           {"id": "2223344", "username": "14715807411 ", "name": "用户9", "authority": ["super"]},
                           {"id": "2223352", "username": "13688888888 ", "name": "用户10", "authority": ["illegal"]},
                           {"id": "2223353", "username": "13866666666 ", "name": "用户11", "authority": ["pc"],
                            "oauth_class": PcDeploy}]
    },
    EnvironmentEnum.TEST: {
        PlatformEnum.钉钉: [
            {"id": "2225241", "username": "15722222222", "role": "1234", "name": "设计部-用户1", "director": {"username": "15083739037"}, "authority": ["super", "applier"],
             "department": "4824"},
            {"id": "2225236", "username": "15083739037", "name": "设计部-用户2", "director": {"username": "17111111111"}, "authority": ["super"]},
            {"id": "2225233", "username": "17111111111", "name": "产品部-用户3", "authority": ["super"]},
            {"id": "2225240", "username": "18444444444", "name": "设计部子部门-用户4", "authority": ["normal"]},
            {"id": "2225238", "username": "19111111111", "name": "销售部-用户5 账号", "authority": ["normal"]},
            {"id": "2225234", "username": "14033334444", "name": "主辅部门-用户6 账号", "authority": ["illegal"]}],
        PlatformEnum.IOS: [{"id": "5501063", "username": "15802179832", "name": "用户1", "director": {"username": "15639358511"}, "authority": ["applier"], "department": "5502686"},
                           {"id": "5501060", "username": "15639358511", "name": "用户2", "director": {"username": "15000249334"}},
                           {"id": "5501051", "username": "15000249334", "name": "用户3", "director": {"username": "18749651655"}, "authority": ["normal"]},
                           {"id": "5501054", "username": "18749651655", "name": "用户4", "director": {"username": "15802176807"}, "authority": ["normal"]},
                           {"id": "5501071", "username": "15802176807", "name": "用户5", "director": {"username": "15802179759"}},
                           {"id": "5501070", "username": "15802179759", "name": "用户6", "director": {"username": "15802176830"}},
                           {"id": "5501064", "username": "15802176830", "name": "用户7", "director": {"username": "15802178093"}},
                           {"id": "5501068", "username": "15802178093", "name": "用户8"},
                           {"id": "5501081", "username": "13916111689 ", "name": "用户9", "authority": ["super"]},
                           {"id": "5501092", "username": "13918797937 ", "name": "用户10", "authority": ["illegal"]},
                           {"id": "5501614", "username": "13660139205 ", "name": "用户11", "authority": ["pc"], "oauth_class": PcDeploy}]
    },
    EnvironmentEnum.STAGE: {
        PlatformEnum.IOS: [{"id": "5000473", "username": "11788888888", "name": "用户1", "director": {"username": "12788888888"}, "authority": ["applier"], "department": "5002305"},
                           {"id": "5000470", "username": "12788888888", "name": "用户2", "director": {"username": "13788888888"}},
                           {"id": "5000471", "username": "13788888888", "name": "用户3", "director": {"username": "14788888888"}, "authority": ["normal"]},
                           {"id": "5000466", "username": "14788888888", "name": "用户4", "director": {"username": "15788888888"}, "authority": ["normal"]},
                           {"id": "5000468", "username": "15788888888", "name": "用户5", "director": {"username": "16788888888"}},
                           {"id": "5000469", "username": "16788888888", "name": "用户6", "director": {"username": "17788888888"}},
                           {"id": "5000476", "username": "17788888888", "name": "用户7", "director": {"username": "19788888888"}},
                           {"id": "5000472", "username": "19788888888", "name": "用户8"},
                           {"id": "5000477", "username": "19988888888 ", "name": "用户9", "authority": ["super"]},
                           {"id": "5000478", "username": "10788888888 ", "name": "用户10", "authority": ["illegal"]},
                           {"id": "5000479", "username": "11188888888 ", "name": "用户11", "authority": ["pc"], "oauth_class": PcDeploy}]
    }
}
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
    # 一级审批
    # [MultistepEnum.负责人主管, ResultEnum.通过,1],[MultistepEnum.负责人主管, ResultEnum.否决,1],[MultistepEnum.负责人主管, ResultEnum.撤销,1],[MultistepEnum.负责人主管, ResultEnum.驳回,1],[MultistepEnum.负责人主管, ResultEnum.无权限,1],
    # [MultistepEnum.任意一人, ResultEnum.通过,1], [MultistepEnum.任意一人, ResultEnum.否决,1], [MultistepEnum.任意一人, ResultEnum.撤销,1], [MultistepEnum.任意一人, ResultEnum.驳回,1], [MultistepEnum.任意一人, ResultEnum.无权限,1],
    # [MultistepEnum.多人会签, ResultEnum.通过,1], [MultistepEnum.多人会签, ResultEnum.否决,1], [MultistepEnum.多人会签, ResultEnum.撤销,1], [MultistepEnum.多人会签, ResultEnum.驳回,1], [MultistepEnum.多人会签, ResultEnum.无权限,1],
    # [MultistepEnum.超管, ResultEnum.通过,1], [MultistepEnum.超管, ResultEnum.否决,1], [MultistepEnum.超管, ResultEnum.驳回,1],
    # 二级审批
    # [MultistepEnum.任意一人,MultistepEnum.负责人主管,ResultEnum.通过,2],[MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.否决,2],[MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.驳回,2],[MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.无权限,2],
    # [MultistepEnum.负责人主管,MultistepEnum.任意一人, ResultEnum.通过,2], [MultistepEnum.负责人主管,MultistepEnum.任意一人, ResultEnum.否决,2],  [MultistepEnum.负责人主管,MultistepEnum.任意一人, ResultEnum.驳回,2], [MultistepEnum.负责人主管,MultistepEnum.任意一人, ResultEnum.无权限,2],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.通过,2], [MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.否决,2],  [MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.驳回,2], [MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.无权限,2],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.通过,2], [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,2], [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.驳回,2], [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.无权限,2],
    # [MultistepEnum.超管,MultistepEnum.超管, ResultEnum.通过,2], [MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,2],
    # [MultistepEnum.超管,MultistepEnum.超管, ResultEnum.驳回,2],
    # 三级审批
    # [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管,ResultEnum.通过,3],[MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管, ResultEnum.否决,3], [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管, ResultEnum.驳回,3],[MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管, ResultEnum.无权限,3],
    # [MultistepEnum.负责人主管, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.通过, 3],[MultistepEnum.负责人主管, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.否决, 3],[MultistepEnum.负责人主管, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.驳回, 3],[MultistepEnum.负责人主管, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.无权限, 3],
    # [MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.通过, 3],
    # [MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.否决, 3],
    # [MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.驳回, 3],
    # [MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.无权限, 3],
    # [MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, ResultEnum.通过, 3],
    # [MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, ResultEnum.否决, 3],
    # [MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, ResultEnum.驳回, 3],
    # [MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, ResultEnum.无权限, 3],
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.通过,3], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,3], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.驳回,3],
    # 四级审批
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.负责人主管,ResultEnum.通过,4],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.否决,4],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.驳回,4],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.无权限,4],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.通过, 4],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.否决, 4],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.驳回, 4],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.任意一人, ResultEnum.无权限, 4],
    # [MultistepEnum.多人会签, MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.通过, 4],
    # [MultistepEnum.多人会签, MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.否决, 4],
    # [MultistepEnum.多人会签, MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.驳回, 4],
    # [MultistepEnum.多人会签, MultistepEnum.任意一人, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, ResultEnum.无权限, 4],
    # [MultistepEnum.任意一人, MultistepEnum.任意一人, MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.通过, 4],
    # [MultistepEnum.任意一人, MultistepEnum.任意一人, MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决, 4],
    # [MultistepEnum.任意一人, MultistepEnum.任意一人, MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.驳回, 4],
    # [MultistepEnum.任意一人, MultistepEnum.任意一人, MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.无权限, 4],
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.通过,4], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,4], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.驳回,4],
    # 五级审批
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,ResultEnum.通过,5],
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管, ResultEnum.否决,5],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, MultistepEnum.负责人主管, ResultEnum.驳回, 5],
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管, ResultEnum.无权限,5],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,ResultEnum.通过,5],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人, ResultEnum.否决,5],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人, ResultEnum.驳回,5],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人, ResultEnum.无权限,5],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.多人会签,ResultEnum.通过,5],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.否决,5],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.驳回,5],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.多人会签, ResultEnum.无权限,5],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,ResultEnum.通过,5],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,5],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.驳回,5],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.无权限,5],
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.通过,5], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,5], [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.驳回,5],
    # 六级审批
    # [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管,ResultEnum.通过,6],
    # [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.否决,6],
    # [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人, MultistepEnum.负责人主管,ResultEnum.驳回,6],
    # [MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.任意一人,MultistepEnum.负责人主管, ResultEnum.无权限,6],
    # [MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.任意一人,ResultEnum.通过, 6],
    # [MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.任意一人,ResultEnum.否决,6],
    # [MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.任意一人,ResultEnum.驳回,6],
    # [MultistepEnum.任意一人,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.任意一人,MultistepEnum.任意一人,ResultEnum.无权限,6],
    # [MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签,ResultEnum.通过,6],
    # [MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签, ResultEnum.否决,6],
    # [MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, MultistepEnum.多人会签,ResultEnum.驳回,6],
    # [MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.多人会签, ResultEnum.无权限,6],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,ResultEnum.通过,6],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,6],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管,ResultEnum.驳回,6],
    # [MultistepEnum.任意一人,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.多人会签,MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管, ResultEnum.无权限,6],
    # [MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管,ResultEnum.通过, 6],
    # [MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管,ResultEnum.否决, 6],
    # [MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管, MultistepEnum.超管,ResultEnum.驳回, 6],

    # 设置六级审批 六级全审批通过，在第六级否决
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,ResultEnum.通过,6],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,6],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, MultistepEnum.负责人主管,ResultEnum.驳回,6],
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.无权限,6],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,ResultEnum.通过,6],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,6],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, MultistepEnum.任意一人,ResultEnum.驳回,6],
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.无权限,6],
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,ResultEnum.通过,6],
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,6],
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, MultistepEnum.多人会签,ResultEnum.驳回,6],
    # [MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.多人会签, MultistepEnum.多人会签, ResultEnum.无权限, 6],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,ResultEnum.通过,6],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,6],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, MultistepEnum.上一级审批人主管,ResultEnum.驳回,6],
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.无权限,6],

    #  设置六级审批，六级审批人都设置负责人主管，第一级审批否决
    #  [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,1],
    # 设置六级审批，六级审批人都设置负责人主管，第二级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,2],
    # 设置六级审批，六级审批人都设置负责人主管，第三级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,3],
    # 设置六级审批，六级审批人都设置负责人主管，第四级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,4],
    # 设置六级审批，六级审批人都设置负责人主管，第五级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管,MultistepEnum.负责人主管, ResultEnum.否决,5],

    # 设置六级审批，六级审批人都设置任意一人，第一级审批否决
    #  [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,1],
    # 设置六级审批，六级审批人都设置任意一人，第二级审批否决
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,2],
    # 设置六级审批，六级审批人都设置任意一人，第三级审批否决
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,3],
    # 设置六级审批，六级审批人都设置任意一人，第四级审批否决
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,4],
    # 设置六级审批，六级审批人都设置任意一人，第五级审批否决
    # [MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人,MultistepEnum.任意一人, ResultEnum.否决,5],

    # 设置六级审批，六级审批人都设置多人会签，第一级审批否决
    #  [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,1],
    # 设置六级审批，六级审批人都设置多人会签，第二级审批否决
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,2],
    # 设置六级审批，六级审批人都设置多人会签，第三级审批否决
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,3],
    # 设置六级审批，六级审批人都设置多人会签，第四级审批否决
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,4],
    # 设置六级审批，六级审批人都设置多人会签，第五级审批否决
    # [MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签,MultistepEnum.多人会签, ResultEnum.否决,5],

    # 设置六级审批，六级审批人一级审批设置负责人主管，其他五级都设置上一级审批人主管，第一级审批否决
    #  [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,1],
    # 设置六级审批，六级审批人一级审批设置负责人主管，其他五级都设置上一级审批人主管，第二级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,2],
    # 设置六级审批，六级审批人一级审批设置负责人主管，其他五级都设置上一级审批人主管，第三级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,3],
    # 设置六级审批，六级审批人一级审批设置负责人主管，其他五级都设置上一级审批人主管，第四级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,4],
    # 设置六级审批，六级审批人一级审批设置负责人主管，其他五级都设置上一级审批人主管，第五级审批否决
    # [MultistepEnum.负责人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管,MultistepEnum.上一级审批人主管, ResultEnum.否决,5],

    # 设置六级审批，超管审批，第一级审批否决
    #  [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,1],
    # 设置六级审批，超管审批，第二级审批否决
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,2],
    # 设置六级审批，超管审批，第三级审批否决
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,3],
    # 设置六级审批，超管审批，第四级审批否决
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,4],
    # 设置六级审批，超管审批，第五级审批否决
    # [MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管,MultistepEnum.超管, ResultEnum.否决,5],
    [{"approve": [MultistepEnum.负责人主管, MultistepEnum.上一级审批人主管, MultistepEnum.多人会签, MultistepEnum.任意一人, ResultEnum.驳回], "result": ResultEnum.驳回, "interrupt": 5}],
    [
        MultistepEnum.负责人主管,
        MultistepEnum.上一级审批人主管,
        MultistepEnum.多人会签,
        MultistepEnum.任意一人,

        5
    ],
    # [
    #     MultistepEnum.负责人主管,
    #     MultistepEnum.上一级审批人主管,
    #     MultistepEnum.任意一人,
    #     ResultEnum.通过,
    #     1
    # ]
]
