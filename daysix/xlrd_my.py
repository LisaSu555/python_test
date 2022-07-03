import xlrd as read_xlrd

url = r"D:\pcf\save\o.xlsx"
# 得到表格对象
data = read_xlrd.open_workbook(url)
# 得到所有的sheet名称，此时返回一个数组
sheet_name = data.sheets()
# 遍历这个数组
for i in range(len(sheet_name)):
    ss = sheet_name[i]
    # 只需要sheet名称为“第一个”
    if ss.name == "第一个":
        # 循环这个sheet中所有行的内容
        for j in range(1, ss.nrows):
            print(ss.row_values(j))


