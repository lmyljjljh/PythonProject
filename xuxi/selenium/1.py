# 【练习1】
# 1. 打开人邮主页，点击 “时政要闻 ” - “ 更多 ”
# 2. 回到主页，点击“工作动态”-“更多”
# 3. 爬出“工作动态”中看到的标题


from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import time

driver = webdriver.Chrome()  # 打开chrome浏览器
driver.get('https://www.ptpress.com.cn/')  # 访问人邮主页
driver.maximize_window()  # 窗口最大化
time.sleep(5)  # 等待是以防数据无法加载

driver.find_element_by_xpath('//*[@id="currentAffairs"]/div[1]/a').click()

driver.find_element_by_xpath('//*[@id="trend"]/div[1]/a').click()
driver.switch_to.window(driver.window_handles[-1])

print(driver.find_element_by_xpath('/html/head/title').text)
