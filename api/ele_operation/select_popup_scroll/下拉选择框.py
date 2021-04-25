"""
@encoding : utf-8
@Time : 2021/4/25 15:22
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("../web/注册B.html")
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器1
driver.quit()