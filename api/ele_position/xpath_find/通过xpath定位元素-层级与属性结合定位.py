"""
@encoding : utf-8
@Time : 2021/4/25 02:13
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
# 通过xpath-层级与属性结合定位元素，并点击
driver.find_element_by_xpath("//div[@id='s-top-left']/div/a").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()