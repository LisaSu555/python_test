# 深拷贝and浅拷贝：深拷贝出的新对象与源对象地址不一致，是新的对象；
# 浅拷贝出来的新对象中的变量地址和源对象的地址一样，修改副本对象就会影响本体对象，因为地址一样
import copy

list1 = [['what', 'are'], 'you', 'doing']

list_deep_copy_from_list1 = copy.deepcopy(list1)

# 判断地址
if id(list1) == id(list_deep_copy_from_list1):
    # 不执行此打印，上面判断不通过
    print('eq!')

i = 0

