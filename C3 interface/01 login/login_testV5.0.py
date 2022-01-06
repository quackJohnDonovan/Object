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

V5.0---2021/05/22
面向对象封装
"""

import requests
import csv


class login_test:

    def __init__(self):
        self.url = "http://localhost:8080/jwshoplogin/user/login.do"
        self.userinfo = {"username": "",
                         "password": "",
                         "result": ""}
        self.path1 = "userinfo.csv"
        self.path2 = "testresult.csv"
        self.num = 0

    def open_file(self):
        # 打开用户信息文件并读取数据
        self.file1 = open(self.path1, "r")
        self.table = csv.reader(self.file1)
        # 打开结果记录文件
        self.file2 = open(self.path2, "w")  # 也可以用a，不覆盖之前内容续写

    def login(self):
        for row in self.table:
            # 定义传参,意思是向字典userinfo中的username键设定值为某一行第一个参数
            self.userinfo["username"] = row[0]
            self.userinfo["password"] = row[1]
            self.userinfo["result"] = row[2]
            # 使用参数调用post接口
            # response = requests.post(self.url, data=self.userinfo).text
            s = requests.session()
            response = s.post(self.url, data=self.userinfo).text
            print(response)
            # 获取返回信息
            msg = response.find(self.userinfo["result"])
            self.num += 1
            if msg > 0:
                print("步骤" + str(self.num) + "执行成功")
                # 在csv文件中，加英文逗号表示换格显示，避免了挤在一起显示的错误
                self.file2.write(row[0] + "," + row[1] + "," + "步骤" + str(self.num) + "执行成功" + "\n")
            else:
                print("步骤" + str(self.num) + "执行失败")
                self.file2.write(row[0] + "," + row[1] + "," + "步骤" + str(self.num) + "执行失败" + "\n")

    def close_file(self):
        self.file1.close()
        self.file2.close()


if __name__ == '__main__':
    login_obj = login_test()
    login_obj.open_file()
    login_obj.login()
    login_obj.close_file()
