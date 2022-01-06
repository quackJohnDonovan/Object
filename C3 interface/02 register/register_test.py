import requests
import csv


class login_test:

    def __init__(self):
        self.file1 = None
        self.url = "http://localhost:8080/jwshoplogin/user/register.do"
        self.userinfo = {"username": "",
                         "password": "",
                         "email": "",
                         "phone": "",
                         "question": "",
                         "answer": ""}
        self.path1 = "registerinfo.csv"
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
            self.userinfo["email"] = row[2]
            self.userinfo["phone"] = row[3]
            self.userinfo["question"] = row[4]
            self.userinfo["answer"] = row[5]
            self.userinfo["result"] = row[6]
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
                self.file2.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + "步骤" + str(self.num) + "执行成功" + "\n")
            else:
                print("步骤" + str(self.num) + "执行失败")
                self.file2.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + "步骤" + str(self.num) + "执行失败" + "\n")

    def close_file(self):
        self.file1.close()
        self.file2.close()


if __name__ == '__main__':
    login_obj = login_test()
    login_obj.open_file()
    login_obj.login()
    login_obj.close_file()
