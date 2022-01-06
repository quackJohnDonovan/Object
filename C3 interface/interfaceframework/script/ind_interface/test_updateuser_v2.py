# v2.0 通过CSV文件导入数据
import os

import unittest2
import requests
import csv


class test_uploaduser(unittest2.TestCase):
    def setUp(self):
        path = os.getcwd()
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        fpath = p2 + r"\testdatafile\ind_interface\test_updatauser.csv"
        file = open(fpath, "r")
        table = csv.reader(file)
        for row in table:
            userinfo = {}
            url = row[1]
            j = int(row[6])
            for i in range(7, 2 * j + 7, 2):
                userinfo[row[i]] = row[i + 1]

        response = requests.post(url, data=userinfo)
        self.sessionID = dict(response.cookies)["JSESSIONID"]
        print(self.sessionID)

    def testcase1(self):
        # 传入参数
        url = "http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo = {
            "email": "1725439952@qq.com",
            "phone": "13252026161",
            "question": "最喜欢吃的水果",
            "answer": "橘子1"
        }

        session = {"JSESSIONID": self.sessionID}
        print(session)
        # 接口调用
        response = requests.post(url, data=userinfo, cookies=session).text
        print(response)
        self.assertIn("更新个人信息成功", response)


if __name__ == '__main__':
    unittest2.main()
