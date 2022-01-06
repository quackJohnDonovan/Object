import csv

# 预置方法：获取csv文件内容
import os


def test_func_csv(filename):
    # 指定文件路径
    # file_path = r"C:\Users\John Donovan\Desktop\Object\C2 selenium\6 自动化测试框架\test_data\\" + filename
    base_path = os.path.dirname(__file__)
    file_path = base_path.replace("test_func", "test_data/" + filename)
    # 按照路径打开csv文件
    file_csv = open(file_path)
    # 读取内容并赋值
    rows = csv.reader(file_csv)

    # 设定行数为1，文件中行数1为标题，不需要测试
    line = 1
    list = []

    for row in rows:
        if line == 1:
            pass
        else:
            list.append(row)
        line += 1

    file_csv.close()
    return list

# 测试一下上方定义函数，测试完成后注释
# test_func_csv("register_data.csv")
