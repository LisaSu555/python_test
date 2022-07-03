from selenium import webdriver
import unittest
import time
# 设置一个全局变量，来控制是否切换窗口
i = 0


# 继承unittest的testcase基类
class Baidu(unittest.TestCase):

    # 开始类，在每个用例运行之前运行一次，有几个用例，这个方法就会运行几次
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.hao123.com')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    # 结束类，在每个用例运行完后运行一次，有几个用例，这个方法就会运行几次
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        # cls.driver.quit()

    def setUp(self) -> None:  # 前置处理，每条用例运行前都会运行setup里面的内容
        global i
        if i > 0:
            # 百度的页面的输入框元素
            self.driver.find_element('xpath', '//*[@id="kw"]').clear()
        else:
            # 默认的火狐页面的输入框元素
            self.driver.find_element('xpath', '//*[@id="search"]/form/div[2]/input').clear()  # 清空输入框
        time.sleep(1)

    def tearDown(self) -> None:  # 后置处理，每条用例运行后都会运行setup里面的内容
        global i
        time.sleep(1)
        # 初始进入浏览器时i就是零
        if i > 0:
            # 从第二次开始将在百度网寻找搜索按键
            self.driver.find_element('xpath', '//*[@id="su"]').click()
        else:
            # 第一次进入浏览器将在火狐网寻找搜索按键
            self.driver.find_element('xpath', '//*[@id="search"]/form/div[3]/input').click()
        time.sleep(1)
        # 得到所有窗口的句柄，返回一个list
        self.handles = self.driver.window_handles
        # 将i设置成1，从此不再火狐网寻找元素
        i = 1
        # 切换窗口操作在点击搜索按键后运行，因为此时一定有两个窗口，所以切换到索引位1的窗口
        self.driver.switch_to.window(self.handles[i])
        # 获取当前页面的标题
        title = self.driver.title
        # self.assertEqual('武汉多测师_百度搜索',title,msg='testcase error!')#通过标题断言
        # 用包含该标题断言
        self.assertIn('多测师_百度搜索', title, msg='你肯定错了！')

    # 跳过当前用例不执行
    # @unittest.skip("test_01")
    def test_01(self):
        self.driver.find_element('xpath', '//*[@id="search"]/form/div[2]/input').send_keys("武汉多测师")

    def test_02(self):
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys("杭州多测师")

    def test_03(self):
        self.driver.find_element('xpath','//*[@id="kw"]').send_keys("上海多测师")

    def test_04(self):
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys("南京多测师")


if __name__ == '__main__':
    unittest.main()

