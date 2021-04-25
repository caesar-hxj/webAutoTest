"""
@encoding : utf-8
@Time : 2021/4/25 02:10
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
# 获取输入框元素对象
el_input = driver.find_element_by_id("kw")
# 输入框输入python
el_input.send_keys("python")
# 获取点击按钮元素对象
el_search = driver.find_element_by_id("su")
# 点击按钮
el_search.click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()