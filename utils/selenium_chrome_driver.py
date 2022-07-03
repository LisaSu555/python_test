from selenium import webdriver
import time
from utils import const_number


class BaseDriver(object):
    def __init__(self, url=const_number.url_baidu, width=const_number.
                 windows_width, height=const_number.windows_height):
        self.url = url
        self.width = width
        self.height = height

    # 得到浏览器驱动
    @staticmethod
    def get_chrome_diver():
        return webdriver.Chrome()

    # 得到常数
    @staticmethod
    def get_const():
        return const_number

    # 得到睡眠
    @staticmethod
    def get_time():
        return time

    # 控制浏览器
    def get_chrome_driver_init(self):
        chrome_driver = self.get_chrome_diver()
        # 异常捕获
        try:
            # 设置窗口位置，坐标指的是窗口左上角的坐标，即(0,0)表示窗口贴着左边和上边
            chrome_driver.set_window_position(110, 60)
            # 设置浏览器打开时的窗口大小
            chrome_driver.set_window_size(self.width, self.height)
            time.sleep(0.2)
            # 输入网址进行访问
            chrome_driver.get(self.url)
            # 如果出现异常
        except Exception as e:
            # 打印这个异常
            print("出现了错误：" + str(e))
        else:
            # 没有出现异常就运行下面code
            print("成功得到驱动对象")
            # 返回这个浏览器对象
            return chrome_driver
