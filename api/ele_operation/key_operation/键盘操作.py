"""
@encoding : utf-8
@Time : 2021/4/25 12:32
@Author : Caesar
@Blog : https://blog.csdn.net/IInmy
@Github : https://github.com/caesar-hxj
"""
import time

from selenium import webdriver

# 实例化driver对象
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 设置要启动的域名
driver.get("https://www.baidu.com/")
# 定位 更多 按钮
input_btn = driver.find_element_by_id("kw")
input_btn.send_keys("python")
# 删除一个字符(相当于Backspace键)
input_btn.send_keys(Keys.BACK_SPACE)
# 全选，相当于（CTRL/COMMAND + A）
input_btn.send_keys(Keys.COMMAND, 'a')
input_btn.send_keys(Keys.COMMAND, 'c')
input_btn.send_keys(Keys.COMMAND, "v")
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
