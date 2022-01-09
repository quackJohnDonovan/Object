from locust import HttpLocust, task, TaskSet


class UserBehavior(TaskSet):
    # 指定测试任务
    @task
    def test_page(self):
        # 发送首页请求
        url = "/index.php?controller=simple&action=login"
        data = {
            'callback': "",
            'login_info': 'htest',
            'password': '123456',
            'remember': '1'
        }
        self.client.post(url, data)


class WebSetUser(HttpLocust):
    host = "http://localhost/iwebshop"
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000
