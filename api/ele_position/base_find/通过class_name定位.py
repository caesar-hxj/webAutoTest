"""
@encoding : utf-8
@Time : 2021/4/25 02:09
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
# 导包
import time

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位输入框，并输入内容
driver.find_element_by_id("kw").send_keys("python")
# 通过class定位元素，如果class属性有多个值，取其中一个值就好
search_btn = driver.find_element_by_class_name("s_btn").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()