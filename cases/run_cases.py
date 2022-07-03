from utils.Email import *
from utils.HTMLtestRunner import *
import unittest

cases_path = r'D:\pcf\soft\project\python\fron_git\cases'
cases_file = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern='test_baidu.py')
# runner = unittest.TextTestRunner()
# runner.run(cases_file)
file_my = open('../dayeleven/one_report.html', 'wb')
command = HTMLTestRunner(stream=file_my, title="My Test Report", tester="hacker", description="nothing")
command.run(cases_file)
report = new_report(cases_path)
send_mail(report)

