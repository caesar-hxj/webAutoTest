"""
@Encoding : utf-8
@IDEA : PyCharm
@Time : 2021/4/24 21:20
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
# 通过元素属性模糊查询-定位元素，并点击
text = driver.find_element_by_css_selector("a[name^='tj_br']").click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
