from utils.selenium_chrome_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains


class MapControl(BaseDriver):
    def vict_baidu(self):
        dr = self.get_chrome_driver_init()
        self.get_time().sleep(2)
        ActionChains(dr).move_to_element(dr.find_element("xpath", '//*[@id="s-top-left"]/a[2]')).perform()

        self.get_time().sleep(100)


baidu = MapControl()
baidu.vict_baidu()

