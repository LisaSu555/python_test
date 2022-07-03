import unittest
import time
from utils.selenium_chrome_driver import BaseDriver
# 设置一个全局变量，来控制是否切换窗口
i = 0
# 声明一个全局驱动
dr = BaseDriver(BaseDriver.get_const().url_hao123).get_chrome_driver_init()


# 继承unittest的testcase基类
class BaiDu(unittest.TestCase):

    # 开始类，在每个用例运行之前运行一次，有几个用例，这个方法就会运行几次
    @classmethod
    def setUpClass(cls) -> None:
        dr.implicitly_wait(30)

    def setUp(self) -> None:  # 前置处理，每条用例运行前都会运行setup里面的内容
        if i > 0:  # 不知道为什么有地方需要global，有地方不需要
            # 百度的页面的输入框元素
            dr.find_element('xpath', '//*[@id="kw"]').clear()
        else:
            # 默认的火狐页面的输入框元素
            dr.find_element('xpath', '//*[@id="search"]/form/div[2]/input').clear()  # 清空输入框
        time.sleep(1)

    def tearDown(self) -> None:  # 后置处理，每条用例运行后都会运行setup里面的内容
        global i  # 不知道为什么有地方需要global，有地方不需要
        time.sleep(1)
        # 初始进入浏览器时i就是零
        if i > 0:
            # 从第二次开始将在百度网寻找搜索按键
            dr.find_element('xpath', '//*[@id="su"]').click()
        else:
            # 第一次进入浏览器将在火狐网寻找搜索按键
            dr.find_element('xpath', '//*[@id="search"]/form/div[3]/input').click()
        time.sleep(1)
        # 得到所有窗口的句柄，返回一个list
        self.handles = dr.window_handles
        # 将i设置成1，从此不再火狐网寻找元素
        i = 1
        # 切换窗口操作在点击搜索按键后运行，因为此时一定有两个窗口，所以切换到索引位1的窗口
        dr.switch_to.window(self.handles[i])
        # 获取当前页面的标题
        title = dr.title
        # self.assertEqual('武汉多测师_百度搜索',title,msg='testcase error!')#通过标题断言
        if not title.__eq__("百度安全验证"):
            # 用包含该标题断言
            self.assertIn('多测师_百度搜索', title, msg='你肯定错了！')
    # 跳过当前用例不执行
    # @unittest.skip("test_01")
    def test_01(self):
        dr.find_element('xpath', '//*[@id="search"]/form/div[2]/input').send_keys("武汉多测师")

    def test_02(self):
        dr.find_element('xpath', '//*[@id="kw"]').send_keys("杭州多测师")

    def test_03(self):
        dr.find_element('xpath','//*[@id="kw"]').send_keys("上海多测师")

    def test_04(self):
        dr.find_element('xpath', '//*[@id="kw"]').send_keys("南京多测师")

    # 结束类，在每个用例运行完后运行一次，有几个用例，这个方法就会运行几次
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(1)
        dr.quit()


if __name__ == '__main__':
    unittest.main()

