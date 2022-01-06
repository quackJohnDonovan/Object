# 针对多个接口进行联调测试 接口内容如下：
# 1、用户注册接口
# 2、用户登录接口
# 3、获取用户信息接口
# 4、修改用户信息
# 5、再次获取用户信息
'''
2021/06/04笔记1：
一个def方法中如何返回多个参数，比如注册完了的用户名和密码我都要用在第二个接口
那么可以把参数放进字典，return字典就行
然后在main函数里通过 字典名["参数名"] 的方式取出想用的值
'''
import requests


class workflow_changeuserinfo_test():

    # 1、用户注册接口
    def register_test(self):

        # 配置数据
        url = "http://localhost:8080/jwshoplogin/user/register.do"
        userinfo = {
            "username": "李雷",
            "password": "123456",
            "email": "15648959874@163.com",
            "phone": "15648959874",
            "question": "最喜欢的书籍",
            "answer": "毛泽东选集"
        }

        # 通过数据调用接口
        s = requests.session()
        response = s.post(url, data=userinfo).text

        # 根据返回信息判断测试是否成功
        print(response)
        a = response.find("注册成功")
        if a > 0:
            print("用户注册接口测试成功")
        else:
            print("用户注册接口测试失败")

        return userinfo

    # 2、用户登录接口
    def login_test(self, username, password):

        # 配置数据
        url = "http://localhost:8080/jwshoplogin/user/login.do"
        userinfo = {
            "username": username,
            "password": password,
        }

        # 通过数据调用接口
        s = requests.session()
        response = s.post(url, data=userinfo).text

        # 根据返回信息判断测试是否成功
        print(response)
        a = response.find("登录成功")
        if a > 0:
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")

    # 3、获取用户信息接口
    def get_userinfo_test(self, username, password):

        # 配置数据
        url = "http://localhost:8080/jwshoplogin/user/get_information.do"
        userinfo = {}

        # 通过数据调用接口
        s = requests.session()
        response = s.post(url, data=userinfo).text

        # 根据返回信息判断测试是否成功
        print(response)
        # a = response.find("登录成功")
        # if a > 0:
        #     print("用户注册接口测试成功")
        # else:
        #     print("用户注册接口测试失败")


if __name__ == '__main__':
    workflowObj = workflow_changeuserinfo_test()

    userinfo = workflowObj.register_test()
    username = userinfo["username"]
    password = userinfo["password"]

    workflowObj.login_test(username, password)

    workflowObj.get_userinfo_test(username,password)
