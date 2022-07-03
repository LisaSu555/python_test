from utils.Email import *
from utils.HTMLtestRunner import *
import unittest


def run_case(cases_path=r'E:\project files\python\from_git\dayeleven', cases_file_name="mc_case.py",
             html_file_path='../dayeleven/two_report.html', html_title="My Test Report",
             html_tester="hacker", html_desc="nothing"):
    cases_file = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern=cases_file_name)
    file_my = open(html_file_path, 'wb')
    command = HTMLTestRunner(stream=file_my, title=html_title, tester=html_tester, description=html_desc)
    command.run(cases_file)
    report = new_report(cases_path)
    send_mail(report)
