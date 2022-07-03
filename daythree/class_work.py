#
# 题目:
# 1、有一个登录系统需要做这样的一个判断：
# 账号：admin  密码：123456  验证码:ab12
# 判断：如果输入的账号，密码，验证码正确则返回登录成功！！
#      如果输入的账号错误：返回账号错误
#      如果输入的密码错误：返回密码错误
#      如果输入的验证码错误：返回验证码错误
# 通过今天所学的方法实现此题目简单判断
# 2、求出1 / 1 + 1 / 3 + 1 / 5……+1 / 99的和
# 3、用循环语句计算2- 10之间整数的循环相乘的值
# 4、用循环语句求出1-100之和
# 5、用循环语句求出1-100的奇数之和
# 6、用循环语句求出1-100的偶数之和
# 7、求出1-100的奇数之和减去1-100的偶数之和
# 8、实现把字符串 str = ’duoceshi‘中任意字母改成大写，在输入函数中输入
# dce输出结果为;DuoCEshi 输入什么什么就变成大写
# str8 = 'devilmaycry'
# input_you = input("please input some words from 'devilmaycry' \n")
# isOutResult = 0  # 计数器
# for str8_char in str8:  # 使用原字符串中每一个字符和输入的字符串中的每一个字符进行比较
#     for input_you_char in input_you:
#         if input_you_char == str8_char:  # 如果输入的字符存在于原字符串
#             isOutResult += 1  # 计数器就加一
#             str8 = str8.replace(str8_char, str8_char.upper())  # 相等就替换成大写，替换可以将相同字符都替换
# if isOutResult != 0:  # 通过计数器来判断是否输入了正确的字符
#     print("下面是你需要大写后的结果：")
#     print(str8)
# else:
#     print("不要输入无关字符")


# str2 = "helloworld"
# count = 0
# input_you_II = input("please input some words from 'helloworld' \n")
# # input_you_II = 'd'
# for j in str2:
#     for i in input_you_II:
#         if i == j:
#             count += 1
# for i in input_you_II:
#     y = i.upper()  # 将字符串中所有大写字符转换成小写
#     str2 = str2.replace(i, y)  # 替换函数
# if count == 0:
#     print("请输入原字符串中包含的字符")
# else:
#     print(str2)

# 9、求出1900 -2017年的闰年（公历闰年,世纪闰年）
# 公历年份是4的倍数的 能被4整除的
# 实际闰年；被100整除而不能被400整除为平年；被100整除也可
# 被400整除的为闰年。如2000年是闰年，而1900年不是。


# 10、请写一段python代码用for循环删除一个list =[1，3，6，9，1，8]重复的元素
list10 = [1, 3, 6, 9, 1, 8]
for i in range(len(list10) - 1):
    changdu = len(list10)
    for j in range(i + 1, len(list10) - 1 - i):
        if list10[i] == list10[j]:
            list10.pop(j)
print(list10)


# 11、统计字符串中每个元素出现的次数st_r='hellword'
# 如h出现了几次，e出现了几次依次类推,
# 12、把字符串user_conrtoller转换为驼峰命名UserController
# 13、冒泡排序
# 给一组无规律的数据从大到小或者从小到大进行排序
# list1 =[66, 5, 3, 88, 22, 555, 411, 21, 33]
# n = len(list1)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print(list1)


# 14. 打印99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %d" % (i, j, i * j), end="\t")
#     print()
