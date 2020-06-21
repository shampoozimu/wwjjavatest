
class JsonUtils:
    def __init__(self):
        pass

    @staticmethod
    def toOKStr(json_str):
        tmp_str = json_str
        tmp_str = tmp_str.replace("'", '"')
        tmp_str = tmp_str.replace('\r\n', '')
        tmp_str = tmp_str.replace('\n', '')
        tmp_str = tmp_str.replace('True', 'true')
        tmp_str = tmp_str.replace('False', 'false')
        tmp_str = tmp_str.replace('None', 'null')
        tmp_str = tmp_str.replace('NULL', 'null')
        '''
        python里面并没有NULL这种类型, python类型与json类型间的转化关系可参考：
        https://www.cnblogs.com/nancyzhu/p/8905749.html
        '''
        return tmp_str

    @staticmethod
    def is_contain(a_dict, b_dict):
        for key in a_dict:
            if key not in b_dict:
                print('%s, %s not in d_dict' % (key, a_dict[key]))
                return False
            if type(a_dict[key]) != type(b_dict[key]):
                print('%s in a_dict not as the same type as in d_dict' % key)
                return False
            if str(type(a_dict[key])) == "<class 'dict'>":
                return JsonUtils.is_contain(a_dict[key], b_dict[key])
            elif str(type(a_dict[key])) == "<class 'list'>":
                for item in a_dict[key]:
                    if item not in b_dict[key]:
                        print('%s, %s in a_dict not in d_dict' % (key, item))
                        return False
            elif a_dict[key] != b_dict[key] and a_dict[key] not in b_dict[key]:
                print('%s, %s in a_dict not in d_dict' % (key, a_dict[key]))
                return False
        print('a_dict is in b_dict, ok!')
        return True


if __name__ == '__main__':
    c = {'code': 100407, 'message': '你已经有相同自定义整数的线索', 'error': 'entity_duplicate_error'}
    d = {'code': 100407, 'message': '你已经有相同自定义整数的线索', }
    a = {'code': [1,2,3, {'message': '你已经有相同自定义整数的线索2'}]}
    b = {'code': [1,2,3,4, {'message': '你已经有相同自定义整数的线索'}]}
    # a = {'code': 0,
    #      'data': {'id': 200484, 'name': 'wwrfdfg\ncgghjjj\ndhjdjdjdjdj', 'company_name': '', 'status': '113410',
    #               'source': '', 'source_mapped': '', 'department': '', 'job': '', 'note': '',
    #               'created_at': '2019-03-08 11:04', 'status_mapped': '未处理', 'updated_at': '2019-03-08 11:04',
    #               'is_own': True, 'status_display': '未处理', 'attachment': {}, 'turned_to_customer': False,
    #               'revisit_remind_at': '', 'turned_customer_id': 0, 'turned_to_customer_name': '', 'qixinbao_id': '',
    #               'creator': {'id': 2223686, 'email': 'nlnongling@163.com', 'created_at': '2018-04-09 19:13',
    #                           'name': '农玲', 'organization_id': 10857, 'phone': '', 'role_id': 2768,
    #                           'workflow_state': 'new', 'job': 'CEO', 'tel': '',
    #                           'avatar_url': 'https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient',
    #                           'department_name': 'WTG信息技术有限公司'}, 'is_editable': True, 'is_user_self': True,
    #               'card_attachment': {}, 'lead_common_setting_id': None, 'before_lead_common_setting_id': None,
    #               'flow_into_at': '', 'text_asset_863cc6': None, 'numeric_asset_ab2a77': '0.0', 'text_asset_9493e7': '',
    #               'text_asset_30aa18': [], 'datetime_asset_db82c8': '', 'text_asset_4615aa': '134',
    #               'text_asset_0b40fc': None, 'text_asset_9593a4': None, 'text_area_asset_59d483': None,
    #               'numeric_asset_5589c9': 1223, 'numeric_asset_e94699': 156.655, 'text_asset_9593a4_hidden_result': '',
    #               'need_hidden_dispose': False, 'text_asset_9493e7_display': None, 'text_asset_30aa18_display': '',
    #               'user': {'id': 2223686, 'email': 'nlnongling@163.com', 'created_at': '2018-04-09 19:13', 'name': '农玲',
    #                        'organization_id': 10857, 'phone': '', 'role_id': 2768, 'workflow_state': 'new',
    #                        'job': 'CEO', 'tel': '',
    #                        'avatar_url': 'https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient',
    #                        'department_name': 'WTG信息技术有限公司'},
    #               'address': {'id': 324446, 'country': {}, 'province': {}, 'city': {}, 'district': {}, 'tel': '',
    #                           'tel_hidden_result': '', 'phone': '', 'phone_hidden_result': '', 'email': '', 'qq': '',
    #                           'fax': '', 'wechat': '', 'wangwang': '', 'zip': '', 'url': '', 'detail_address': '',
    #                           'lat': 0.0, 'lng': 0.0, 'distance': '未知', 'region_info': None, 'off_distance': -1,
    #                           'gaode_staticmap': '', 'full_address': ''},
    #               'owned_department': {'id': 5685, 'name': 'WTG信息技术有限公司'}, 'before_user': None,
    #               'before_owned_department': None}}
    # b = {'code': 0,
    #      'data': {'name': 'wwrfdfg\ncgghjjj\ndhjdjdjdjdj', 'company_name': '', 'status': '113410', 'source': '',
    #               'source_mapped': '', 'department': '', 'job': '', 'note': '', 'created_at': '2019-03-07 13:10',
    #               'status_mapped': '未处理', 'updated_at': '2019-03-07 13:10', 'is_own': True, 'status_display': '未处理',
    #               'attachment': {}, 'turned_to_customer': False, 'revisit_remind_at': '', 'turned_customer_id': 0,
    #               'turned_to_customer_name': '', 'qixinbao_id': '',
    #               'creator': {'id': 2223686, 'email': 'nlnongling@163.com', 'created_at': '2018-04-09 19:13',
    #                           'name': '农玲', 'organization_id': 10857, 'phone': '', 'role_id': 2768,
    #                           'workflow_state': 'new', 'job': 'CEO', 'tel': '',
    #                           'avatar_url': 'https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient',
    #                           'department_name': 'WTG信息技术有限公司'}, 'is_editable': True, 'is_user_self': True,
    #               'card_attachment': {}, 'lead_common_setting_id': None, 'before_lead_common_setting_id': None,
    #               'flow_into_at': '', 'text_asset_863cc6': None, 'numeric_asset_ab2a77': '0.0', 'text_asset_9493e7': '',
    #               'text_asset_30aa18': [], 'datetime_asset_db82c8': '', 'text_asset_4615aa': '106',
    #               'text_asset_0b40fc': None, 'text_asset_9593a4': None, 'text_area_asset_59d483': None,
    #               'numeric_asset_5589c9': 1223, 'numeric_asset_e94699': 156.655, 'text_asset_9593a4_hidden_result': '',
    #               'need_hidden_dispose': False, 'text_asset_9493e7_display': None, 'text_asset_30aa18_display': '',
    #               'user': {'id': 2223686, 'email': 'nlnongling@163.com', 'created_at': '2018-04-09 19:13', 'name': '农玲',
    #                        'organization_id': 10857, 'phone': '', 'role_id': 2768, 'workflow_state': 'new',
    #                        'job': 'CEO', 'tel': '',
    #                        'avatar_url': 'https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient',
    #                        'department_name': 'WTG信息技术有限公司'},
    #               'address': {'id': 324418, 'country': {}, 'province': {}, 'city': {}, 'district': {}, 'tel': '',
    #                           'tel_hidden_result': '', 'phone': '', 'phone_hidden_result': '', 'email': '', 'qq': '',
    #                           'fax': '', 'wechat': '', 'wangwang': '', 'zip': '', 'url': '', 'detail_address': '',
    #                           'lat': 0.0, 'lng': 0.0, 'distance': '未知', 'region_info': None, 'off_distance': -1,
    #                           'gaode_staticmap': '', 'full_address': ''},
    #               'owned_department': {'id': 5685, 'name': 'WTG信息技术有限公司'}, 'before_user': None,
    #               'before_owned_department': None}}

    JsonUtils.is_contain(a, b)

