from selenium.webdriver.common.action_chains import ActionChains
from utils import selenium_chrome_driver as init_driver
import time
from utils import const_number
url = "https://www.baidu.com"
# url = "https://www.csdn.net"
dr = init_driver.webdriver
# 使用xpath： 选中元素后在html代码处右键选择copy xpath
input_search = dr.find_element("class name", "s_ipt")
time.sleep(2)
input_search.send_keys("怎么表白？")
time.sleep(1)
search_button = dr.find_element("id", "su")
search_button.click()
time.sleep(20)
dr.find_element("link text", "百度首页").click()
ActionChains(dr).move_to_element(dr.find_element("xpath", '//*[@id="s-usersetting-top"]')).perform()
dr.find_element("link text", '关闭热搜').click()
time.sleep(7)

