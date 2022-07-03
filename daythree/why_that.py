# 好方法
list10 = [1, 3, 6, 9, 1, 8, 1, 3, 6, 1]
list_result = []
for number_in_list10 in list10:
    if number_in_list10 not in list_result:
        list_result.append(number_in_list10)
print(list_result)