"""
@Encoding : utf-8
@IDEA : PyCharm
@Time : 2021/4/24 22:34
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
# 浏览器窗口最大化
driver.maximize_window()
# 获取 更多 按钮的元素对象
more_btn = driver.find_element_by_partial_link_text("更多")
# 获取元素大小并打印
print(more_btn.size)
# 获取元素文本并打印
print(more_btn.text)
# 获取元素的[name]属性值
more_name = more_btn.get_attribute("name")
print(more_name)
# 判断元素是否可见
print("更多按钮是否可见：", more_btn.is_displayed())
# 判断元素是否可用
print("更多按钮是否可用：", more_btn.is_enabled())
# 暂停3秒
time.sleep(3)
# 关闭驱动，退出浏览器
driver.quit()
