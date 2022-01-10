import csv

from locust import HttpLocust, task, TaskSet
from lxml import etree


class SearchTest(TaskSet):
    @task
    def search_test(self):
        file = open('searchdata.csv', 'r')
        table = csv.reader(file)

        for row in table:
            response = self.client.get("/index.php?controller=site&action=search_list&word=" + str(row)).text
            # doc = etree.HTML(response)
            # keyword = doc.xpath('/html/body/div[1]/div[6]/div[2]/ul/li/h3/a/text()')
            # print(keyword)


class WebSetUser(HttpLocust):
    host = "http://localhost/iwebshop"
    task_set = SearchTest
    min_wait = 2000
    max_wait = 5000