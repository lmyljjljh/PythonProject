# 页面等待：
# 强制等待：time.sleep()
# 隐式等待: 设置了一个时间，在这一段时间内判断元素是否定位成功，就进行下一步，在设置时间内没有定位成功，则会报超时加载错
# 显式等待: 明确等待某一个元素

from selenium import webdriver
import time

driver = webdriver.Chrome()

# 隐式等待
driver.implicitly_wait(10)


url = 'https://jn.lianjia.com/'

driver.get(url)
time.sleep(3)