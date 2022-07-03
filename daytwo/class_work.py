# 1.已知字符串 s = "my,name,is,zhangsan",请用两种办法取出之间的“name”字符。
s = "my,name,is,zhangsan"
s_list = s.split(',')
name1 = s_list[1]
name2 = s[3:7]
print('第一题')
print(name1)
print(name2+'\n')

# 2.将lisi修改为zhangsan？
a2 = 'lisi'
result2 = a2.replace('lisi','zhangsan')
print('第二题')
print(result2+'\n')

# 3.已知如下变量，将a与b拼接成字符串c
a3 = "字符串拼接1"
b3 = "字符串拼接2"
c = a3+b3
print('第三题')
print('%s%s'%(a3, b3))
print(c+'\n')

# 4.请找出第一个"i"出现的位置。
a4 = "i,am,a,boy,in,china"
index_i = a4.index('i')
print('第四题')
print(index_i)

# 5.请计算该字符串一共有几个逗号。
a5 = "i,am,a,boy,in,china"
number = a5.count(',')
print('第五题')
print(number)

# 6.有一个元组 a = (1,2,3)，现在想修改1为11怎么做？
a6 = (1, 2, 3)
alist = list(a6)
index_1 = a6.index(1)
alist[index_1] = 11
a6 = tuple(alist)
print('第六题')
print(a6)

# 7.列表a = [11,22,24,29,30,32]
#  7.1 把28插入到列表的末端
a = [11, 22, 24, 29, 30, 32]
length = len(a)
a.insert(length, 28)
print('第七题第一小题')
print(a)
#  7.2 在元素29后面插入元素57
index_29 = a.index(29)
a.insert(index_29+1, 57)
print('第七题第二小题')
print(a)
#  7.3 把元素11修改成6
index_11 = a.index(11)
a[index_11] = 6
print('第七题第三小题')
print(a)
#  7.4 删除元素32
index_32 = a.index(32)
a.pop(index_32)
print('第七题第四小题')
print(a)
#  7.5 对列表从小到大排序
a.sort()
print('第七题第五小题')
print(a)


# 8.统计字符串中每个元素出现的次数
# st="helloword"
# 如h出现了，e出现几次依次类推
# 法一
str8 = 'helloworld'
char_dic = {}
for i in str8:
    # 同时将键值存入dict
    char_dic[i] = str8.count(i)
print('第八题：')
print(char_dic)

# 法二
length8 = str8.__len__()
yuan8 = tuple(str8)
result_set = set()
for i in range(length8):
    ss = yuan8[i]
    result_set.add((ss, str8.count(ss)))
print(result_set)

# 法三 ， 最简单
st = "helloworld"
for i in set(st):
    a = st.count(i)
    print('%s一共出现了%d次'%(i, a))


# 9.有user_name把这个user_name改变为userName
str9 = 'user_name'
# 拆分成两个部分
str9_list = str9.split('_')
# 将第二部分首字母大写
str9_2 = str9_list[1].title()
# 将两部分拼接
str9_result = str9_list[0]+str9_2
# 然后打印
print('第九题：\n' + str9_result)
# 方法二 简单地替换
str9 = str9.replace('n', 'N')
str9 = str9.replace('_', '')
print(str9)

