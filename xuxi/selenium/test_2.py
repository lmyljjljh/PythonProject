import time
from selenium import webdriver

diver = webdriver.Chrome()

# 向某个url发送请求
diver.get("https://www.baidu.com/")
time.sleep(3)

# 在百度搜索框中搜索‘python’
diver.find_element_by_id('kw').send_keys('python')

# 点击'百度搜索'
diver.find_element_by_id('su').click()

time.sleep(6)
# 退出浏览器
diver.quit()
