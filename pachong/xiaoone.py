# coding:utf-8
import requests
import json
import time
import random
import smtplib
from email.mime.text import MIMEText

# 学校版


# 有4个地方需要添加内容：list_name \ list_mailbox \ token \ location

# 需添加1
list_name = ['zjh','zzz','yqg','czy','yjq','yyt','gsy','lyx','hh'
    # 'zb', 'cyj', 'mmn', 'sj', 'hsf', 'ch', 'll', 'sdf', 'zcf', 'lm', 'zzn'
]

# 需添加2
list_mailbox = {
    'zjh': '2216662494@qq.com',
    'zzz': '2024418112@qq.com',
    'yqg': '729361308@qq.com',
    'czy': '1248097851@qq.com',
    'yjq': '2586861505@qq.com',
    'yyt': '854121180@qq.com',
    'gsy': '2673829452@qq.com',
    'lyx': '1548746890@qq.com',
    'hh' : '1582255191@qq.com'
    # 'zb': '941407617@qq.com',
}
# 需添加3
token = {
    'zjh': '78aaadc300dc604843f8ad06',
    'zzz': 'c7aaadc300dc604843f8ad06',
    'yqg': '94969b63007436f59c6207f5',
    'czy': '98aaadc300dc604843f8ad06',
    'yjq': 'b7aaadc300dc604843f8ad06',
    'yyt': 'a8aaadc300dc604843f8ad06',
    'gsy': '053f45c300bcda74cc459316',
    'lyx': '708966c300c14aa3ef3ae6f5',
    'hh' : 'e7aaadc300dc604843f8ad06'
    # 'zb': 'fc9aadc300dc604843f8ad06',
}
# 需添加4
location = {
    'zjh': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'zzz': {
            "province": "420000",
            "city": "420100",
            "county": "420115",
            "autoFetch": True,
            "lng": "114.437485",
            "lat": "30.4841"
        },
    'yqg': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'czy': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'yjq': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'yyt': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'gsy': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'lyx': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    'hh': {
        "province": "420000",
        "city": "420100",
        "county": "420115",
        "autoFetch": True,
        "lng": "114.437485",
        "lat": "30.4841"
    },
    # 'zb': {
    #     "province": "420000",
    #     "city": "420100",
    #     "county": "420115",
    #     "autoFetch": True,
    #     "lng": "114.437485",
    #     "lat": "30.4841"
    # },

}


# 随机延迟0~y秒
def delay_0_y_s(random_delay_num):
    y = float(random_delay_num)
    time.sleep(random.random() * 3)


# 发送邮箱
def mail_Status(mailbox, status):
    mail_host = 'smtp.qq.com'
    mail_user = "limengyuan09@qq.com"
    mail_pass = "oguwfguzseseehhg"
    sender = 'limengyuan09@qq.com'
    receivers = mailbox
    message = MIMEText(status, 'plain', 'utf-8')
    message['Subject'] = '小One易统计失效提醒'
    message['From'] = sender
    message['To'] = receivers

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败', e)


# 返回日报id
def get_daily_report_id(name, headers, data):
    daily_report_url = 'https://www.ioteams.com/ncov/api/users/dailyReport'
    res = requests.post(daily_report_url, headers=headers,
                        data=json.dumps(data))  # 发送post请求
    response = res.text  # 将response结果变为test格式
    response_dict = json.loads(response)  # 将html格式转换为python可以识别的字典格式
    if 'code' in response_dict:
        code = response_dict['code']
        if code == 403:  # 403证明已经打卡，返回值为0
            print(name + "   code:'403',今日已经打过卡啦")
            #mail_Status(list_mailbox[name], '今日已经打过卡啦。')
            return 0
        else:
            _id = response_dict['data']['data']['_id']  # 返回日报id
            return _id
    else:  # Token失效返回值也为0
        print(name + " Token失效，今日打卡失败")
        mail_Status(list_mailbox[name], 'Token失效，今日打卡失败，请手动打卡以更新Token。')
        return 0


# 打卡
def report_health(name, headers, data):
    _id = get_daily_report_id(name, headers, data)
    if _id == 0:
        return
    else:
        url = 'https://www.ioteams.com/ncov/api/users/dailyReport/{}'
        requests.put(url.format(_id), headers=headers, data=json.dumps(data))
        #mail_Status(list_mailbox[name], '今日已打卡。')
        print("今日打卡成功")

def lmy():
    for name_use in list_name:
        # print(list_name[list_name[i]]) #遍历token
        # print(location[list_name[i]]) #遍历位置信息

        headers = {
            "Content-Type": "application/json;charset=utf-8",
            "ncov-access-token": token[name_use],
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/86.0.4240.198 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://www.ioteams.com",
            "Host": "www.ioteams.com",
            "Referer": "https://www.ioteams.com/ncov/",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Content-Length": "347",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        data = {
            "address": location[name_use],
            "at_home": True,
            "contacted": False,
            "contacted_beijing": False,
            "description": "",
            "family_confirmed": False,
            "family_suspected": False,
            "fever": False,
            "infected": False,
            "passed_beijing": False,
            "self_confirmed": False,
            "self_suspected": False
        }
        report_health(name_use, headers, data)
        delay_0_y_s(random.uniform(10, 15))
if __name__ == '__main__':

    for name_use in list_name:
        # print(list_name[list_name[i]]) #遍历token
         # print(location[list_name[i]]) #遍历位置信息

        headers = {
            "Content-Type": "application/json;charset=utf-8",
                "ncov-access-token": token[name_use],
                "Connection": "keep-alive",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/86.0.4240.198 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Origin": "https://www.ioteams.com",
                    "Host": "www.ioteams.com",
                    "Referer": "https://www.ioteams.com/ncov/",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Content-Length": "347",
                    "Accept-Language": "zh-CN,zh;q=0.9"
                }
        data = {
                    "address": location[name_use],
                    "at_home": True,
                    "contacted": False,
                    "contacted_beijing": False,
                    "description": "",
                    "family_confirmed": False,
                    "family_suspected": False,
                    "fever": False,
                    "infected": False,
                    "passed_beijing": False,
                    "self_confirmed": False,
                    "self_suspected": False
        }
        report_health(name_use, headers, data)
        delay_0_y_s(random.uniform(10, 15))
