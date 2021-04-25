"""
@Encoding : utf-8
@IDEA : PyCharm
@Time : 2021/4/24 21:58
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@github : https://github.com/caesar-hxj
"""
# 导包
import time

from selenium import webdriver

# 实例化driver对象
driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位输入框
ele_input = driver.find_element_by_id("kw")
# 模拟输入内容
ele_input.send_keys("Java")
# 暂停2s，便于观察
time.sleep(2)
# 再次模拟输入之前，必须先清空原来的内容，否在会在后面追加
ele_input.clear()
# 暂停2s，便于观察
time.sleep(2)
# 模拟输入内容
ele_input.send_keys("python")
# 暂停2s，便于观察
time.sleep(2)
# 定位 搜索 按钮，并进行点击操作
driver.find_element_by_id("su").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
