"""

"""
import csv

import requests
import unittest2

# class test_register(unittest2.TestCase):
#
#     def setUp(self):
#         self.url = "http://localhost:8080/jwshoplogin/user/register.do"
#         self.userinfo = {
#             "username": "张三",
#             "password": "123456",
#             "email": "13588868881@qq.com",
#             "phone": "13588868881",
#             "question": "最喜欢的水果",
#             "answer": "橘子"
#         }
#
#     # 1、用户注册接口
#     def test_register(self):
#
#         s = requests.session()
#         response = s.post(self.url, data=self.userinfo).text
#         print(response)
#
#         self.assertIn("用户名已经存在", response)
#
#
# if __name__ == '__main__':
#     unittest2.main()

# class test_import(unittest2.TestCase):
#     def setUp(self):
#         self.result = {}
#         self.result_file = open("result.csv", "w")
#         self.file = open("test_info.csv", "r")
#
#     def test_register(self, user_info=None):
#         table = csv.reader(self.file)
#         for raw in table:
#             user_info = {}
#             j = int(raw[6])
#             url = raw[1]
#             self.expect_result = raw[3]
#             self.interface_name = raw[5]
#             for i in range(7, 2 * j + 7, 2):
#                 user_info[raw[i]] = raw[i + 1]
#             s = requests.session()
#             response = s.post(url, data=user_info).text
#             print(response)
#             self.assertIn(self.expect_result, response)
#             print(self.interface_name + "测试完成")
#
#             self.result = {}
#             self.result["接口名称"] = self.interface_name
#             self.result["返回结果"] = response
#
#     def tearDown(self):
#         for key, value in self.result.items():
#             self.result_file.write(str(key) + "," + str(value) + ",")
#         self.result_file.write("\n")
#         self.result_file.close()
#         self.file.close()
#
#
# if __name__ == '__main__':
#     unittest2.TestCase()

import unittest2
import requests


class test_mulinterface(unittest2.TestCase):

    def setUp(self):
        print("setUp")

    # 定义注册接口测试方法

    def test_case1(self):
        print("注册接口")

    # 定义登录测试方法
    def test_case2(self):
        print("登录接口")

    # 定义检查测试方法
    def test_case3(self):
        print("检查接口")

    def tearDown(self):
        print("tearDown")


if __name__ == '__main__':
    # # unittest2.main()
    # 声明测试套对象
    suite = unittest2.TestSuite()
    suite.addTest(test_mulinterface("test_case3"))
    # 运行测试套
    runner = unittest2.TextTestRunner()
    runner.run(suite)



