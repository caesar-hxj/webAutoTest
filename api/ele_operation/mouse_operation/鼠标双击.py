"""
@Encoding : utf-8
@IDEA : PyCharm
@Time : 2021/4/24 22:53
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@github : https://github.com/caesar-hxj
"""
# 导包
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 实例化driver对象

driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位输入框，获取元素对象
ele_input = driver.find_element_by_id("kw").send_keys("python")
# 获取鼠标操作的行为对象
action = ActionChains(driver)
# 对元素执行动作
action.double_click(ele_input)
# 执行操作
action.perform()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
