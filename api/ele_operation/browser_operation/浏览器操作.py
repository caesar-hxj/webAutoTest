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
# 设置浏览器大小600*600
driver.set_window_size(600, 600)
# 设置浏览器位置：300，300
driver.set_window_position(300, 300)
# 浏览器最大化
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
# 后退
driver.back()
# 前进
driver.forward()
# 刷新
driver.refresh()
# 获取标题
print(driver.title)
# 获取url
print(driver.current_url)
driver.back()
driver.find_element_by_partial_link_text("更多").click()
# 关闭当前窗口
driver.close()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
