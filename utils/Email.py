"""
send_email.py：配置收发邮件
"""
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import os

# ======查找测试目录，找到最新生成的测试报告文件======
# class Sum_Mail():
#     def __init__(self,report_path,new_report=None):
#         self.report_path = report_path
#         self.new_report = new_report
def new_report(report_path):
    lists = os.listdir(report_path)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))  # 按时间排序
    new_report = os.path.join(report_path, lists[-1])  # 获取最新的文件保存到file_new
    return new_report

def send_mail(new_report):
    f = open(new_report, "rb")
    mail_body = f.read()
    f.close()
    username = "382002847@qq.com"  #发件箱的用户名
    password = "sptgihwkvmeacahe"        #发件箱密码（授权码）
    sender = "382002847@qq.com"    #发件人邮箱
    receiver = ["1510684732@qq.com"]  #收件人邮箱
    # 邮件正文是MIMEText
    msg = MIMEText(mail_body, "html", "utf-8")
    # 邮件对象
    msg["Subject"] = Header("自动化测试报告", "utf-8").encode()
    msg["From"] = Header(u"测试机 <%s>"%sender)
    msg["To"] = Header("测试负责人 <%s>"%receiver)
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")