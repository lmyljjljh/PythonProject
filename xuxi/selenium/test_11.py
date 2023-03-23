# chrom无头模式
from selenium import webdriver
import time

url = 'http://www.baidu.com'
# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')

# 配置对象添加使用代理ip命令
# opt.add_argument('--proxy-server=http://27.38.154.143:9999')

# 更换user-agent
opt.add_argument('--user-agent=Mozilla/5.0 python37')

# 创建浏览器对象的时候添加配置对象
deiver = webdriver.Chrome(chrome_options=opt)
deiver.get(url)
time.sleep(3)
# deiver.save_screenshot("1.png")

#
