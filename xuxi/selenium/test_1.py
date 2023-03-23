from selenium import webdriver
# 指定driver的绝对路径
diver = webdriver.PhantomJS(executable_path="D:\phantomjs-2.1.1-windows")

# 向一个url发送请求
diver.get('http://www.itcast.cn/')

# 把网页保存为图片
diver.save_screenshot("itcast.png")

# 退出模拟器
diver.quit()