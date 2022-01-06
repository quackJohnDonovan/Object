# 对更新用户信息的脚本进行测试，使用unittest框架
# 接口信息
# 接口访问地址
# http://localhost:8080/jwshoplogin/user/update_information.do
# 接口传参
# 1、email 2、phone 3、question 4、answer
# 接口预期返回结果
# 1、更新个人信息成功 2、更新个人信息失败 3、email已存在,请更换email再尝试更新

# 脚本实现
import unittest2
import requests


class test_uploaduser(unittest2.TestCase):

    def setUp(self):
        url = "http://localhost:8080/jwshoplogin/user/login.do"
        userinfo = {
            "username": "张三",
            "password": "111111",
        }

        response = requests.post(url, data=userinfo)
        self.sessionID = dict(response.cookies)['JSESSIONID']
        # print(self.sessionID)
        print(response)

    def test_case1(self):
        # 传入参数
        url = "http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo = {
            "email": "1725439952@qq.com",
            "phone": "13252026161",
            "question": "最喜欢吃的水果",
            "answer": "橘子"
        }

        session = {"JSESSIONID":self.sessionID}
        # 接口调用
        response = requests.post(url, data=userinfo, cookies=session).text
        print(response)
        self.assertIn("更新个人信息成功", response)


if __name__ == '__main__':
    unittest2.main()
