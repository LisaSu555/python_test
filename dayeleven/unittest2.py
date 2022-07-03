from selenium import webdriver
import unittest
import time
"""
不知道怎么回事
"""

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("start")

    @classmethod
    def tearDownClass(cls) -> None:
        print("end")

    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        # self.dr.execute_script("window.open('https://www.csdn.net')")
        self.dr.implicitly_wait(20)
        self.dr.get("https://www.csdn.net")
        self.dr.maximize_window()
        time.sleep(0.1)

    def tearDown(self) -> None:
        self.dr.find_element('xpath', '//*[@id="toolbar-search-button"]').click()
        time.sleep(5)
        self.dr.quit()

    def test_baidu(self):
        self.dr.find_element('xpath', '//*[@id="toolbar-search-input"]').send_keys('百度')
        print("case one has been called")

    def test_jingdong(self):
        self.dr.find_element('xpath', '//*[@id="toolbar-search-input"]').send_keys('京东')
        print("case two has been called")

    def test_jave(self):
        self.dr.find_element('xpath', '//*[@id="toolbar-search-input"]').send_keys('java')
        print("case two has been called")


if __name__ == "__main__":
    # 生成对象，套件
    suite = unittest.TestSuite()
    # 将需要运行的用例装在一个list
    cases = [UnitTest("test_baidu"), UnitTest("test_jingdong")]
    # 往套件对象传入需要执行的用例的list，如果只想执行一个用例，
    # 可以在list里面写一个，也可以suite.addTest，不加s的方法，
    # 比如 suite.addTest(UnitTest("test_java"))
    suite.addTests(cases)
    # 生成运行对象
    runner = unittest.TextTestRunner()
    # 执行
    runner.run(suite)

