#从网站下载稍修改
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="15684043728"    #用户名
mail_pass="841128"   #口令 
 
 
sender = '15684043728@163.com'
receivers = ['yaogang1985@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('今天下午去神算，为什么发不出去来', 'plain', 'utf-8')
#message['From'] = Header("菜鸟教程", 'utf-8')
#message['To'] =  Header("测试", 'utf-8')
message['From']='yy<15684043728@163.com>'
message['To']='yaogang1985@126.com'
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")

except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

    
