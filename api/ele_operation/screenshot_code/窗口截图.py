"""
@encoding : utf-8
@Time : 2021/4/25 15:28
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 输入框输入python
driver.find_element_by_id("kw").send_keys("python")
# 将当前页面进行截图，以search.png保存在当前目录下
driver.get_screenshot_as_file("./search.png")
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
