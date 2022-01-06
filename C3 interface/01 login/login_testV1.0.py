"""
接口自动化测试
版本V1.0---2021/05/22

使用requests方法获取登录接口返回信息
关键句：response = requests.post(url, data=userinfo).text

"""

import requests

# 定义传参
url = "http://localhost:8080/jwshoplogin/user/login.do"
userinfo = {"username": "李明", "password": "123456"}
# 使用参数调用post接口
response = requests.post(url, data=userinfo).text

print(response)
