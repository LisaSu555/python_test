from selenium import webdriver
import unittest
import time


class UnitTest(unittest.TestCase):
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
        self.dr.find_element('xpath', '//*[@id="toolbar-search-input"]').send_keys('java')
        print("case one has been called")

    def test_jingdong(self):
        self.dr.find_element('xpath', '//*[@id="toolbar-search-input"]').send_keys('python')
        print("case two has been called")


if __name__ == "__main__":
    unittest.main()


