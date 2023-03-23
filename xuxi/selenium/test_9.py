from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://jn.lianjia.com/'

driver.get(url)
time.sleep(3)

# 滚动条的拖动
js = 'scrollTo(0,600)'  # scrollTo(x,y) x水平移动，y竖直移动
driver.execute_script(js)
