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
driver.get("http://localhost:63342/webAutoTest/api/web/%E6%B3%A8%E5%86%8CB.html")
# 通过显示等待定位元素
more_btn = WebDriverWait(driver,
                         timeout=30,
                         poll_frequency=0.5).until(lambda x: x.find_element_by_partial_link_text("更多"))
more_btn.click()
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()