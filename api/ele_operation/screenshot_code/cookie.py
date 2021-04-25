"""
@encoding : utf-8
@Time : 2021/4/25 15:37
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time
from selenium import webdriver

# 实际的cookie值，登录百度账号后，在开发者模式中查看
cookie_value = "xxx"

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 添加cookie
driver.add_cookie({'name': 'BDUSS', 'valu1`e': cookie_value})
time.sleep(3)
# 刷新页面，更改状态
driver.refresh()
time.sleep(3)
driver.quit()
