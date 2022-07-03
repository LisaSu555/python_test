from utils.selenium_chrome_driver import BaseDriver
import unittest


class TestBaidu(BaseDriver, unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 得到浏览器驱动
        cls.dr = BaseDriver.get_chrome_diver()
        cls.dr.get("https://www.baidu.com")
        # 设置窗口大小
        cls.dr.set_window_size(BaseDriver.get_const().windows_width,
                               BaseDriver.get_const().windows_height)
        # 隐藏等待时间
        cls.dr.implicitly_wait(30)
        cls.search_input = cls.dr.find_element('id', 'kw')
        cls.search_button = cls.dr.find_element('id', 'su')

    def setUp(self) -> None:
        BaseDriver.get_time().sleep(2)
        self.search_input.clear()

    def test_01(self):
        self.search_input.send_keys("java")

    def test_02(self):
        self.search_input.send_keys("c++")

    def tearDown(self) -> None:
        self.search_button.click()

    @classmethod
    def tearDownClass(cls) -> None:
        BaseDriver.get_time().sleep(10)


if __name__ == "__main__":
    unittest.main()

