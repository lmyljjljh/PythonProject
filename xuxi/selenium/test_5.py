from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://wh.58.com/chuzu/?PGTID=0d100000-0009-e854-7709-5a2c292d24d8&ClickID=2'

driver.get(url)
time.sleep(3)

el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
for el in el_list:
    print(el.text, el.get_attribute('href'))

