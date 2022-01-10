from locust import HttpLocust, task, TaskSet


# class UserBehavior(TaskSet):
#     # 指定测试任务
#     @task
#     def test_page(self):
#         # 发送首页请求
#         url = "/index.php?controller=simple&action=login"
#         data = {
#             'callback': "",
#             'login_info': 'htest',
#             'password': '1234567',
#             'remember': '1'
#         }
#         self.client.post(url, data)
#
#
# class WebSetUser(HttpLocust):
#     host = "http://localhost/iwebshop"
#     task_set = UserBehavior
#     min_wait = 2000
#     max_wait = 5000
# import csv
#
# data_file = open('userdata.csv', 'r')
# table = csv.reader(data_file)
# print(table)
# for row in table:
#     username = row[0]
#     password = row[1]
#     data = {
#         # 'callback': "",
#         'login_info': username,
#         'password': password,
#         # 'remember': '1'
#     }
#     print(data)
# data_file.close()

import requests

data = {"email": "1@qq.com",
        "username": "htest0",
        "password": "123456",
        "repassword": "123456",
        "captcha": "12345"}
response = requests.post("http://localhost/iwebshop/index.php?controller=simple&action=reg_act", data).text
print(response)
