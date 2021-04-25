"""
@encoding : utf-8
@Time : 2021/4/25 02:12
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
# 通过tag_name(标签名)来定位输入框
driver.find_element_by_tag_name("input").send_keys("python")
# 通过id定位查找按钮
search_btn = driver.find_element_by_id("su").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()