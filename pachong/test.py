# coding:utf-8
import requests
import json
import time
import random
import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'
mail_user = "limengyuan09@qq.com"
mail_pass = "oguwfguzseseehhg"
sender = 'limengyuan09@qq.com'

receivers = '2630639540@qq.com'
message = MIMEText("这是一个测试", 'plain', 'utf-8')
message['Subject'] = '测试'
message['From'] = sender
message['To'] = receivers

smtpObj = smtplib.SMTP_SSL(mail_host)
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()