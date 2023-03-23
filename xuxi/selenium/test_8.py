from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://baidu.com/'

driver.get(url)
time.sleep(3)

print(driver.get_cookies())

cookies = {}
for data in driver.get_cookies():
    cookies[data['name']] = data['name']

print(cookies)
