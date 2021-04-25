"""
@encoding : utf-8
@Time : 2021/4/25 15:22
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 实例化driver对象
driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 通过显示等待定位元素
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)
# 向下滑动3000像素
scroll_down = "window.scrollTo(0,3000)"
# 向上滑动顶部
scroll_up = "window.scrollTo(0,0)"
# 调用JS方法
driver.execute_script(scroll_down)
# 暂停3秒
time.sleep(3)
# 调用JS方法
driver.execute_script(scroll_up)
# 关闭驱动，退出浏览器
driver.quit()
