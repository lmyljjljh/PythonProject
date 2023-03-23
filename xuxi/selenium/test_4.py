from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)
time.sleep(3)  # 在网络不稳定的情况下可能网页并没有完全加载完成，但是这个时候我们已经开始进行xpath路径解析了。这样就会导致找不到我们想要的内容也是会报错。

# 通过xpath进行元素定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python3')
# 通过css选择器进行元素定位
# driver.find_element_by_css_selector('#kw').send_keys('python3')
# 通过name值进行元素定位
# driver.find_element_by_name('wd').send_keys('python3')
# 通过class名字进行元素定位
# driver.find_element_by_class_name('s_ipt').send_keys('python3')

# driver.find_element_by_id('su').click()

# 通过链接文本进行元素定位
# driver.find_element_by_link_text('hao123').click()
# 通过部分链接文本进行元素定位
# driver.find_element_by_partial_link_text('hao').click()
# 目标元素在当前html中是唯一标签或是众多定位出来的标签中的第一个的时候才能使用
driver.find_element_by_tag_name('div')



