from utils.Email import *
from utils.HTMLtestRunner import *
import unittest


def run_case(cases_path=r'E:\project files\python\from_git\dayeleven', cases_file_name="mc_case.py",
             html_file_path='E:\\project files\\python\\from_git\\html', html_title="My Test Report",
             html_tester="hacker", html_desc="nothing"):
    # 寻找需要执行的用例py文件
    cases_file = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern=cases_file_name)
    # html报告存放地址
    file_my = open(html_file_path + "\\report.html", 'wb')
    # 将数据写入html报告中的命令
    command = HTMLTestRunner(stream=file_my, title=html_title, tester=html_tester, description=html_desc)
    # 命令执行找到的用例py文件
    command.run(cases_file)
    # 得到report文件对象
    report = new_report(html_file_path)
    # send_mail(report)


run_case()

