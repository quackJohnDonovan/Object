# 针对多个接口进行联调测试 接口内容如下：
# 1、用户注册接口
# 2、用户登录接口
# 3、忘记密码接口
# 4、提交密保问题答案
# 5、回答完密保问题后修改密码接口
"""
接口测试联调V1.0--2021/06/03
每个接口自己传入url，参数，结果。没什么特别的，使用了面向对象方法
"""
# 定义一个测试类
import requests


class workflow_forgetpassword_test():
    # 1、用户注册接口
    def register_test(self):
        url = "http://localhost:8080/jwshoplogin/user/register.do"
        userinfo = {
                     "username": "张三",
                     "password": "123456",
                     "email": "13588868881@qq.com",
                     "phone": "13588868881",
                     "question": "最喜欢的水果",
                     "answer": "橘子"
                    }
        s = requests.session()
        response = s.post(url, data=userinfo).text
        print(response)

        a = response.find("注册成功")
        if a > 0:
            print("用户注册接口测试成功")
        else:
            print("用户注册接口测试失败")

    # 2、用户登录接口
    def login_test(self):
        url = "http://localhost:8080/jwshoplogin/user/login.do"
        userinfo = {
                     "username": "张三",
                     "password": "123456",
                    }
        s = requests.session()
        response = s.post(url, data=userinfo).text
        print(response)

        a = response.find("登录成功")
        if a > 0:
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")

    # 3、忘记密码接口
    def forget_password_test(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
        userinfo = {
                     "username": "张三",
                    }
        s = requests.session()
        response = s.post(url, data=userinfo).text
        print(response)

        a = response.find("最喜欢的水果")
        if a > 0:
            print("忘记密码接口测试成功")
        else:
            print("忘记密码接口测试失败")

    # 4、提交密保问题答案
    def commit_answer_test(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo = {
                    "username": "张三",
                    "question": "最喜欢的水果",
                    "answer": "橘子"
                    }
        s = requests.session()
        response = s.post(url, data=userinfo).text
        print(response)

        # 定义字典
        dic = {}
        # 将text类型转换为字典
        dic = eval(response)
        # 取出字典中的token字段
        token = dic["data"]
        print(token)

        a = response.find("data")
        if a > 0:
            print("提交密保问题答案接口测试成功")
        else:
            print("提交密保问题答案接口测试失败")

        return token

    # 5、回答完密保问题后修改密码接口
    def change_password_test(self, token):
        url = "http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo = {
                    "username": "张三",
                    "passwordNew": "111111",
                    "forgetToken": token
                    }
        s = requests.session()
        response = s.post(url, data=userinfo).text
        print(response)

        a = response.find("修改密码成功")
        if a > 0:
            print("修改密码接口测试成功")
        else:
            print("修改密码接口测试失败")


if __name__ == '__main__':
    workflowObj = workflow_forgetpassword_test()
    workflowObj.register_test()
    workflowObj.login_test()
    workflowObj.forget_password_test()
    token = workflowObj.commit_answer_test()
    workflowObj.change_password_test(token)
    workflowObj.register_test()
