import win32gui
import win32con
import win32clipboard as w
from time import sleep


# 主体函数
def QqSend(msg="测试代码", name="接受消息的qq昵称"):
    # 将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    # 填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    # 回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


# 循环控制主体函数的函数，循环次数按照自己需求修改，修改QqSend方法里面的参数即可
def loop_send():
    i = 0
    while i < 200:
        QqSend("hello"+str(i), "")
        sleep(0.1)
        i += 1


# 执行
loop_send()
