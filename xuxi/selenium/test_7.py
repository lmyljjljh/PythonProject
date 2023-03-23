from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://qzone.qq.com/'

driver.get(url)
time.sleep(3)

el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
# driver.switch_to.frame('login_frame')
driver.switch_to.frame(el_frame)
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1946483721')
driver.find_element_by_id('p').send_keys('lmy17771569161')
driver.find_element_by_id('login_button').click()
