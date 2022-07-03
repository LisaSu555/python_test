from utils.selenium_chrome_driver import BaseDriver


class IframeMy2(BaseDriver):
    def one(self):
        dr = self.get_chrome_driver_init("https://www.jd.com")
        dr.find_element("link text", '你好，请登录').click()
        self.time(2)
        dr.find_element('xpath', '//*[@id="kbCoagent"]/ul/li[1]/a/span').click()
        # dr.switch_to.frame(dr.find_element('tag name', 'iframe'))
        dr.switch_to.frame(0)  #
        dr.find_element('id', 'switcher_plogin').click()
        print("点了")
        self.time(0.5)
        dr.back()
        self.time(0.5)
        dr.back()
        dr.find_element('id', 'key').send_keys("iphone")
        self.time(1000)

    def time(self, t):
        return self.get_time().sleep(t)


if2 = IframeMy2()
if2.one()

