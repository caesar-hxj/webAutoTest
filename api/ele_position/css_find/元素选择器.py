"""
@encoding : utf-8
@Time : 2021/4/25 02:08
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
# 通过元素选择器定位元素，一般情况下，只有页面有且只有一个此元素标签时，才使用元素选择器；如果定位的元素过多时，返回第一个元素
driver.find_element_by_css_selector("input")
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()