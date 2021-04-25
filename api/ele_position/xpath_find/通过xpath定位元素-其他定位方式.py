"""
@encoding : utf-8
@Time : 2021/4/25 02:13
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
# 通过文本内容xxx定位：//*[text()='xxx']
driver.find_element_by_xpath("//*[text()='更多']").click()
# 通过含有xxx元素定位：//*[contains(@attribute,'xxx')]
driver.find_element_by_xpath("//*[contains(@value,'百度')]").send_keys("python")
# 通过属性以xxx开头的元素：//*[start-with(@attribute,'xxx')]
driver.find_element_by_xpath("//*[starts-with(@value,'百度')]").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()