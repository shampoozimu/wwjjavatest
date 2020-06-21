# coding:utf-8
import json
a ='{"code": 0, "data": {"id": 200388, "name": "wwrfdfg\ncgghjjj\ndhjdjdjdjdj", "company_name": "", "status": "113410", "source": "", "source_mapped": "", "department": "", "job": "", "note": "", "created_at": "2019-03-06 15:32", "status_mapped": "未处理", "updated_at": "2019-03-06 15:32", "is_own": "ture", "status_display": "未处理", "attachment": {}, "turned_to_customer": False, "revisit_remind_at": "", "turned_customer_id": 0, "turned_to_customer_name": "", "qixinbao_id": "", "creator": {"id": 2223686, "email": "nlnongling@163.com", "created_at": "2018-04-09 19:13", "name": "农玲", "organization_id": 10857, "phone": "", "role_id": 2768, "workflow_state": "new", "job": "CEO", "tel": "", "avatar_url": "https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient", "department_name": "WTG信息技术有限公司"}, "is_editable": "ture", "is_user_self": "ture", "card_attachment": {}, "lead_common_setting_id": None, "before_lead_common_setting_id": None, "flow_into_at": "", "text_asset_863cc6": None, "numeric_asset_ab2a77": "0.0", "text_asset_9493e7": "", "text_asset_30aa18": [], "datetime_asset_db82c8": "", "text_asset_4615aa": "38", "text_asset_0b40fc": None, "text_asset_9593a4": None, "text_area_asset_59d483": None, "numeric_asset_5589c9": 1223, "numeric_asset_e94699": 156.655, "text_asset_9593a4_hidden_result": "", "need_hidden_dispose": False, "text_asset_9493e7_display": None, "text_asset_30aa18_display": "", "user": {"id": 2223686, "email": "nlnongling@163.com", "created_at": "2018-04-09 19:13", "name": "农玲", "organization_id": 10857, "phone": "", "role_id": 2768, "workflow_state": "new", "job": "CEO", "tel": "", "avatar_url": "https://dn-ikcrm-files-dev.qbox.me/attachments/files/34883/123.jpg?imageMogr2/thumbnail/!100x100r/crop/!100x100/format/jpg/auto-orient", "department_name": "WTG信息技术有限公司"}, "address": {"id": 324350, "country": {}, "province": {}, "city": {}, "district": {}, "tel": "", "tel_hidden_result": "", "phone": "", "phone_hidden_result": "", "email": "", "qq": "", "fax": "", "wechat": "", "wangwang": "", "zip": "", "url": "", "detail_address": "", "lat": 0.0, "lng": 0.0, "distance": "未知", "region_info": None, "off_distance": -1, "gaode_staticmap": "", "full_address": ""}, "owned_department": {"id": 5685, "name": "WTG信息技术有限公司"}, "before_user": None, "before_owned_department": None}}'
# print(type(a))
# Expected_results = json.loads(a)
# print(Expected_results)
# j = {"accessToken": "521de21161b23988173e6f7f48f9ee96e28", "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_131)"}
# str = json.loads(a)
#
c=json.loads(a,strict=False)

# c =(json.loads(json.dumps(a)))
print(c)
print(type(c))
#
# print(str)
# print(type(str))

