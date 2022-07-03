import utils.selenium_chrome_driver as driver_init
import utils.const_number as const


def vist_csdn():
    url = "https://www.csdn.net/"
    ww = const.windows_width
    wh = const.windows_height
    # 调用封装的方法，开启浏览器，访问输入的网址
    driver = driver_init.get_chrome_driver_init(url, ww, wh)
    # 等待一段时间，等待浏览器加载
    const.sleepTime.sleep(3)
    # 获取页面上的输入框对象
    search_input = driver.find_element("id", "toolbar-search-input")
    # 等待一段时间
    const.sleepTime.sleep(1)
    # 往输入框中填入值
    search_input.send_keys("怎么表白")
    # 等待一段时间
    const.sleepTime.sleep(1)
    # 自动按下回车键
    search_input.send_keys(const.Keys.ENTER)
    # 等待一段时间，这段时间后浏览器会关闭，不知道为什么会关闭，都没有调用close
    const.sleepTime.sleep(6)


vist_csdn()


# 自动化脚本在版本上线之后写
# 自动化测试在回归测试时执行，在第二个版本人工测试时执行前一个版本的脚本自动测试第一个版本
# 自动化测试流程：1.根据业务需求筛选出需要自动化测试的业务
#              2.找出需要自动化的测试场景和功能测试用例
#              3.选择自动化测试工具
#              4.自动化测试框架设计与搭建
#              5.自动化用例输出及执行和维护

