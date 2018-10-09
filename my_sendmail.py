import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.163.com'
mail_user='15684043728'
mail_pass='841128'

sender='15684043728@163.com'
receivers='yaogang1985@126.com'

msg=MIMEText('send by python on 20180607','plain','utf-8')
msg['From']=sender
msg['To']=receivers


try:
    smtp=smtplib.SMTP()
    smtp.connect(mail_host,900)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receivers,msg.as_string())
    smtp.quit()
    print("Send successfully")
except:
    print('Error')
