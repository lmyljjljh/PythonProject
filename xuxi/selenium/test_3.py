import time

from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome()

driver.get(url)

# 显示源码
print(driver.page_source)

# 显示响应的url
print(driver.current_url)
print(driver.title)

time.sleep(2)

driver.get('http://www.douban.com')

time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
# driver.close()
driver.save_screenshot('douban.png')
driver.quit()
