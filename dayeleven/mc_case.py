from selenium import webdriver
import unittest
import time

i = 0


class Baidu(unittest.TestCase):  # 继承unittest的testcase基类

    @classmethod
    def setUpClass(cls) -> None:  # 开始类
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.hao123.com')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls) -> None:  # 结束类
        time.sleep(3)
        # cls.driver.quit()

    def setUp(self) -> None:  # 前置处理，每条用例运行前都会运行setup里面的内容
        global i
        # print("setup:"+i)
        if i > 0:
            self.driver.find_element('xpath', '//*[@id="kw"]').clear()
        else:
            self.driver.find_element('xpath', '//*[@id="search"]/form/div[2]/input').clear()  # 清空输入框
        time.sleep(2)

    def tearDown(self) -> None:  # 后置处理，每条用例运行后都会运行setup里面的内容
        global i
        time.sleep(2)
        if i > 0:
            self.driver.find_element('xpath', '//*[@id="su"]').click()
        else:
            self.driver.find_element('xpath', '//*[@id="search"]/form/div[3]/input').click()
        time.sleep(2)
        self.handles = self.driver.window_handles
        if i < 1:
            i += 1
        self.driver.switch_to.window(self.handles[i])
        title = self.driver.title  # 获取当前页面的标题
        # self.assertEqual('武汉多测师_百度搜索',title,msg='testcase error!')#通过标题断言
        self.assertIn('多测师_百度搜索', title, msg='你肯定错了！')  # 用包含该标题断言

    # @unittest.skip("test_01")  # 跳过当前用例不执行
    def test_01(self):
        self.driver.find_element('xpath', '//*[@id="search"]/form/div[2]/input').send_keys("武汉多测师")
        time.sleep(3)

    def test_02(self):
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys("杭州多测师")
        time.sleep(3)

    def test_03(self):
        self.driver.find_element('xpath','//*[@id="kw"]').send_keys("上海多测师")
        time.sleep(3)

    def test_04(self):
        self.driver.find_element('xpath', '//*[@id="kw"]').send_keys("南京多测师")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

