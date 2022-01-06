"""
接口自动化测试

V1.0---2021/05/22
使用requests方法获取登录接口返回信息
关键句：response = requests.post(url, data=userinfo).text

V2.0---2021/05/22
编写预期结果
关键句：response.find("")

"""

import requests

# 定义传参
url = "http://localhost:8080/jwshoplogin/user/login.do"
userinfo = {"username": "李明", "password": "123456"}

# 使用参数调用post接口
response = requests.post(url, data=userinfo).text
print(response)

# 获取返回信息
msg = response.find("登录成功")

if msg > 0:
    print("用例执行成功")
else:
    print("用例执行失败")