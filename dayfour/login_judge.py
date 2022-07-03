# 导入随机数
import random
# 定义成功和失败的code
success_code = "0000"
failed_code = "0001"
# 随机从范围内产生余额
balance = random.randint(0, 100)


"""
   定义一个判断登录成功与否的方法 
   @:return 成功或者失败的代码
"""


def is_login(name, password):
    # name和psw都正确则返回成功的代码，否则返回失败的代码
    if name == "tiger" and password == "123456":
        return success_code
    else:
        return failed_code


"""
    定义一个查询余额的方法
"""


def query_balance():
    # 输入两个值
    username = input("please input your username:\n")
    password = input("please input your password:\n")
    # 调用方法后得到结果
    login_result = is_login(username, password)
    # 判断结果的正确性
    if login_result.__eq__(success_code):
        print("your balance is $%d" % balance)
    else:
        print("username or password is error,please try again")


# 调用查询方法
query_balance()

