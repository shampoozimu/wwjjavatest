#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from co import const


#定义邮件发送所需要的参数
# sender = "testreport@ikcrm.com"
sender = const.sender
# receiver = ["wang.l@ikcrm.com","you.mq@ikcrm.com","li.jc@ikcrm.com"]
receiver = const.receiver
username = const.username
password = const.password
# password = "eKcaRCuWYVuMv77y"
smtpserver = 'smtp.exmail.qq.com:25' #如163邮箱：mail.163.com

subject = '邮件主题' #主题自定义
body = '<pre><h1>测试报告，请查收~</h1></pre>' #定义邮件正文为html格式

def send_main(filepath,filename):

    # file_path = r"D:\workspace\ikcrm\study\case\2018_04_26_16_44_24.html"
    with open(filepath,'rb') as fp:
        mail_body =fp.read()
    msg =MIMEMultipart()
    msg['from'] = sender
    # msg['to']= receiver
    msg['to']= ";".join(receiver)
    msg['subject']=u"dingding staging test report"


    #添加正文内容到容器
    body = MIMEText(mail_body,'html', 'utf-8')
    msg.attach(body)
    #添加附件到容器
    att = MIMEText(mail_body ,"base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename=%s' %filename
    # att["Content-Disposition"] = 'attachment; filename= “2018_04_26_16_44_24.html"'
    msg.attach(att)


    #返回SMTP()的一个实例
    smtp = smtplib.SMTP()
    #连接服务器
    smtp.connect(smtpserver)
    #登录
    smtp.login(username, password)
    #发送邮件、
    smtp.sendmail(sender, receiver, msg.as_string())
    #关闭服务
    smtp.quit()
    print ('邮件发送成功')
