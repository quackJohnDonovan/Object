import csv

from locust import HttpLocust, TaskSet, task


# class LoginTest(TaskSet):
#     @task
#     def login_test(self):
#         url = "/index.php?controller=simple&action=login"
#         for i in range(1, 101):
#             username = 'htest' + str(i)
#             data = {
#                 # 'callback': "",
#                 'login_info': username,
#                 'password': '123456',
#                 # 'remember': '1'
#             }
#             self.client.post(url, data)
#
#
# class WebSetUser(HttpLocust):
#     host = "http://localhost/iwebshop"
#     task_set = LoginTest
#     min_wait = 2000
#     max_wait = 5000


from locust import HttpLocust, TaskSet, task


class LoginTest(TaskSet):
    @task
    def login_test(self):
        url = "/index.php?controller=simple&action=login"
        data_file = open('userdata.csv', 'r')
        table = csv.reader(data_file)
        for row in table:
            username = row[0]
            password = row[1]
            data = {
                # 'callback': "",
                'login_info': username,
                'password': password,
                # 'remember': '1'
            }
            self.client.post(url, data)
        data_file.close()


class WebSetUser(HttpLocust):
    host = "http://localhost/iwebshop"
    task_set = LoginTest
    min_wait = 2000
    max_wait = 5000
