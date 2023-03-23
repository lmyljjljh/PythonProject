import requests
import random
import json
import smtplib
from email.mime.text import MIMEText

s1 = "abcdefghijklmnopqrstuvwxyz"
strings = ""+random.choice(s1)+random.choice(s1)


headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
}

login_url = "http://szcw.hue.edu.cn/xysf/api/User/App/Login"
cx_url = "http://szcw.hue.edu.cn/xysf/aAppPage/index.aspx/GetRechargeInfo"

cookies = {
    'ASP.NET_SessionId': f'fbzmtsazjkwtxv2pq2053c{strings}',
}
login_data = {
    'xh': '2050300018',
    'pwd': 'o45TAB9PzxlsXRvKt3e+DBnKWsj6fyDiqnf4ualrhg+NrPuKDo6hgqWTzqbX0W3BUjaPpE93eyWVszO/u5C/I+TsLfHRTQCyuZza9+RtrgqvBHwObmNZqmlvxlHdiU0UzP9g73H0N3/AE3+ROWAM/UMEskufD6LuYgfUnce25Sw=',
    'rsaStr': '2555888',
    'ltyp': 'id',
}
cx6528_data = {
    'rybh': '2942',
    'category': 'Synjones',
}
reponse1 = requests.post(login_url, headers=headers, cookies=cookies, json=login_data, verify=False)


reponse2 = requests.post(cx_url, headers=headers, cookies=cookies, json=cx6528_data, verify=False)

x6528dl = reponse2.text
x6528dl = json.loads(x6528dl)
x6528dl = x6528dl['d']['Content']['CzThirdInfo']['Balance']

if x6528dl <= 50:
    mail_host = 'smtp.qq.com'
    mail_user = "limengyuan09@qq.com"
    mail_pass = "oguwfguzseseehhg"
    sender = 'limengyuan09@qq.com'
    receivers = '2216662494@qq.com'
    message = MIMEText(f"528寝室还剩余电量{x6528dl}", 'plain', 'utf-8')
    message['Subject'] = '测试'
    message['From'] = sender
    message['To'] = receivers
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()

