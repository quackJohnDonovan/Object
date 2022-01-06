"""
接口自动化测试

V1.0---2021/05/18
使用requests方法获取登录接口返回信息
关键句：response = requests.post(url, data=userinfo).text

V2.0---2021/05/19
对响应结果进行校验，得出测试结论
关键句：response.find("")查找特定内容，找到就返回大于0的位置坐标

V3.0---2021/05/20
从文件中传入多组测试数据,并对不同的数据配置相对应的预期结果
关键句：
file1 = open("userinfo.csv", "r")
table = csv.reader(file1)

V4.0---2021/05/21
把每一个测试结果写入测试报告
注意：文件关闭后再写入内容，不然会报错
关键句：
file2 = open("testresult.csv", "a", encoding="utf-8-sig")
file2.write(row[0] + "," + row[1] + "," + "步骤" + str(i) + "执行成功" + "\n")

"""

import requests
import csv

# 打开参数文件读取内容
file1 = open("userinfo.csv", "r")
table = csv.reader(file1)

# 提前打开测试结果文件，方便以后写入
file2 = open("testresult.csv", "a", encoding="utf-8-sig")

# 定义传参
url = "http://localhost:8080/jwshoplogin/user/login.do"
userinfo = {"username": "", "password": "", "result": ""}
i = 0
# 按照表格里每一行进行验证，所以用循环
for row in table:
    # 定义传参,意思是向字典userinfo中的username键设定值为某一行第一个参数
    userinfo["username"] = row[0]
    userinfo["password"] = row[1]
    userinfo["result"] = row[2]
    # 使用参数调用post接口
    response = requests.post(url, data=userinfo).text
    print(response)
    # 获取返回信息
    msg = response.find(userinfo["result"])
    i = i + 1
    if msg > 0:
        print("步骤" + str(i) + "执行成功")
        # 在csv文件中，加英文逗号表示换格显示，避免了挤在一起显示的错误
        file2.write(row[0] + "," + row[1] + "," + "步骤" + str(i) + "执行成功" + "\n")
    else:
        print("步骤" + str(i) + "执行失败")
        file2.write(row[0] + "," + row[1] + "," + "步骤" + str(i) + "执行失败" + "\n")

# 随手关灯
file1.close()
file2.close()
