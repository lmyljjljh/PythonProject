# 窗口切换
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://wh.58.com'

driver.get(url)
time.sleep(3)

# 定位并点击租房按钮
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a').click()

# 获取当前所以标签页的句柄构成的列表
current_windows = driver.window_handles
print(driver.current_url)
print(current_windows)
# 窗口重定位
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_url)
el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')

for el in el_list:
    print(el.text, el.get_attribute('href'))
