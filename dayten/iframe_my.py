from utils.selenium_chrome_driver import BaseDriver


class IframeMy(BaseDriver):
    def one(self):
        # 得到驱动对象，默认访问百度，当前dr对象只会控制百度页面
        dr = self.get_chrome_driver_init()
        # 京东的js执行代码
        jd = 'window.open("https://www.jd.com")'
        # 再打开一个页签，访问jd网站
        dr.execute_script(jd)
        dr.implicitly_wait(2)
        dr.execute_script('window.open("https://www.taobao.com")')
        dr.implicitly_wait(2)
        dr.execute_script('window.open("https://www.csdn.net")')
        dr.implicitly_wait(2)
        dr.execute_script('window.open("https://www.4399.com")')
        dr.implicitly_wait(2)
        # 此时的dr还是在百度页签里面寻找元素,所以kw找的是百度的id，而不是京东的页面id
        dr.find_element("id", "kw").send_keys("iphone")
        # 获取窗口句柄，dr初始化时使用的什么网址，此时获取的就是那个网址的页签
        current_windows = dr.current_window_handle
        # 获取所有窗口句柄，返回一个列表
        all_windows = dr.window_handles  # b 4 c t j
        print("当前为："+current_windows)
        for i in range(len(all_windows)):
            if current_windows != all_windows[i]:
                print(all_windows[i])
                dr.switch_to.window(all_windows[i])
                print(dr.title+"\n")
        dr.implicitly_wait(2)
        print("循环结束："+dr.title)
        dr.switch_to.window(all_windows[1])
        dr.find_element("id", "smart_input").send_keys("超级马里奥")
        self.wait(0.5)
        dr.find_element("id", "smart_input").send_keys(self.keys().ENTER)
        self.wait(100)

    def wait(self, time):
        self.get_time().sleep(time)

    def keys(self):
        return self.get_const().keyborad


iframe1 = IframeMy()
iframe1.one()


