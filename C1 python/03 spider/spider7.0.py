'''
爬虫
已完成面向过程封装

版本：
1.0完成单条数据的抓取         2021/04/25
2.0使用循环抓取多页数据       2021/04/25
3.0将抓取数据写入txt文件      2021/04/25
4.0面向过程的封装            2021/04/27
5.0面向对象的封装            2021/04/28
6.0代码逻辑优化             2021/04/28
7.0从csv文件中读取关键参数    2021/04/29

'''

# 6.0

import requests
from lxml import etree
import csv


# 定义类
class spider:

    # 全局函数
    def __init__(self, url, page,path,suffix):
        # 将参数传入
        self.url = url
        self.page = page
        self.path = path
        self.suffix = suffix

    # 连接网页
    def link(self):
        # 发送请求
        response = requests.get(self.url)
        # 确定编码格式
        response.apparent_encoding
        # 确定解码格式
        response.encoding = 'gbk'
        # 转换文本类型
        content = response.text
        # 转换json格式
        self.doc = etree.HTML(content)

    # 抓取内容
    def spider(self):
        # 获取指定xpath路径下的内容
        collect = ''
        for i in range(1, 11):
            ele = self.doc.xpath(self.path + str(i) + self.suffix)[0]
            collect = collect + ele + str('\n')
        self.final = collect

    # 将内容写入文件
    def file(self):
        # 创建文件(已有前提下就是打开文件)

        file = open('../spider.txt', 'a')
        # 写入内容
        file.write('第' + str(self.page) + '页')
        file.write('\n')
        file.write(self.final)
        file.write('\n')
        # 关闭文件
        file.close()


if __name__ == '__main__':
    # 从csv文件中获取网址与路径
    file_csv = open('para.csv', 'r')
    rows = csv.reader(file_csv)
    for row in rows:
        url0 = row[0]
        path = row[1]
        suffix = row[2]
        for i in range(1, 11):
            if i == 1:
                url1 = url0+'.html'
            else:
                url1 = url0+'-page-'+str(i)+'.html'
            print(url1)
            spiderObj = spider(url1, i, path, suffix)
            spiderObj.link()
            spiderObj.spider()
            spiderObj.file()

