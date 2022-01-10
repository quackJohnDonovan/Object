from locust import HttpLocust, task, TaskSet


class RegisterTest(TaskSet):
    @task
    def register_test(self):
        # 定义测试数据
        for i in range(101, 121):
            url = "/index.php?controller=simple&action=reg_act"
            email = str(i) + "@qq.com"
            username = "htest" + str(i)
            data = {"email": email,
                    "username": username,
                    "password": "123456",
                    "repassword": "123456",
                    "captcha": "12345"}
            response = self.client.post(url, data).text
            num = response.find("恭喜")

            if num > 0:
                print('测试通过')
            else:
                print('测试失败')


class WebSetUser(HttpLocust):
    host = "http://localhost/iwebshop"
    task_set = RegisterTest
    min_wait = 2000
    max_wait = 5000