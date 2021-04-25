"""
@encoding : utf-8
@Time : 2021/4/25 12:26
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver

# 实例化driver对象
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位 更多 按钮
more_btn = driver.find_element_by_partial_link_text("更多")
# 将鼠标悬停在 更多 按钮上并执行
ActionChains(driver).move_to_element(more_btn).perform()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
