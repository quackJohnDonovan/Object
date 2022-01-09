from locust import HttpLocust, task, TaskSet


class UserBehavior(TaskSet):
    @task
    def test_login(self):
        self.client.get("/")


class WebSiteUser(HttpLocust):
    host = "http://localhost:8080/jwshoplogin/user/login.do"
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 2000000
