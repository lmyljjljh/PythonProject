import requests
from lxml import etree
class F1(object):
    def __int__(self):
        self.url = "https://www.acwing.com/file_system/gui/window/operate/open/994425/?url_type=json_response&acwing_app_url=message_group_list_pull_message_records"
        self.headers={
            "Cookie" : "csrftoken=jCsYcD0JmkxwSm1Rqt2wwFs3RcE0pdGZ5Diu6v1SJjy5N1xF7vA1y80NVTt8E385; sessionid=6ly8wfdw4ftel3c6vaqky6fh14488o6j",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
        }
    def f1(self):
        html = requests.get(url=self.url,headers=self.headers).text
        self.f2(html)
    def f2(self,html):
        parse_html = etree.HTML(html)
        t1 = parse_html.xpath('//*[@id="form_upload_profileinfo"]/div[1]')
        print(t1)

if __name__ == '__main__':
    t2 = F1()
    t2.f1()