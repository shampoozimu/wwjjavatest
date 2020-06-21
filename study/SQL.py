import pymysql
conn = pymysql.connect(host='rdscbq34656z0ix59br0.mysql.rds.aliyuncs.com', user='ik_qa', passwd='A97ecc1a', charset='utf8')
conn.select_db('crm_test')
cur = conn.cursor()
querystring = 'select id  from  customers a  where organization_id = 10718 '
cur.execute(querystring)
results = cur.fetchall()
print(results)
cnn.commit()
cur.close()
