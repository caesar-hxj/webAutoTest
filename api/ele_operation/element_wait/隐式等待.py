"""
@encoding : utf-8
@Time : 2021/4/25 15:07
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome()
# 设置隐式等待时间，在此时间内如果找不到该元素，则会报异常：NoSuchElementException
driver.implicitly_wait(30)
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位 更多 按钮
driver.find_element_by_partial_link_text("更多").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
