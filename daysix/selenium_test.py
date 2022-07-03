from selenium import webdriver
from time import sleep


# 得到驱动对象
chrome_driver = webdriver.Chrome()
# 设置窗口位置，坐标指的是窗口左上角的坐标，即(0,0)表示窗口贴着左边和上边
chrome_driver.set_window_position(110, 60)
# 设置浏览器打开时的窗口大小
chrome_driver.set_window_size(1280, 760)
# 输入网址进行访问
chrome_driver.get("https://www.baidu.com")
# 暂停一下
sleep(0.2)
# 得到搜索框对象
search_input = chrome_driver.find_element('id', 'kw')
# 在搜索框中输入指定字符
search_input.send_keys("python")
# 得到搜索按键
search_button = chrome_driver.find_element('id', 'su')
# 暂停一下
sleep(0.2)
# 点击这个搜索按键
search_button.click()
