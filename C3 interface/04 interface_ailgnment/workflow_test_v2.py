# 针对多个接口进行联调测试 接口内容如下：
# 1、用户注册接口
# 2、用户登录接口
# 3、忘记密码接口
# 4、提交密保问题答案
# 5、回答完密保问题后修改密码接口
"""
接口测试联调V1.0--2021/06/03
每个接口自己传入url，参数，结果。没什么特别的，使用了面向对象方法

接口测试联调V2.0--2021/06/04
把url，参数，结果放在文档里，读取csv文件中内容通过main传入方法并调用接口，可以根据行数来循环读取数据调用接口
"""
import csv
import requests


class workflow_forgetpassword_test:

    def workflow_test(self, url, userinfo, expect_result, interface_name):
        result = {}
        result["接口名称"] = interface_name

        s = requests.session()
        response = s.post(url, data=userinfo).text
        result["返回结果"] = response
        # print(response)
        a = response.find(expect_result)
        if a > 0:
            print(interface_name + "测试成功")
        else:
            print(interface_name + "测试失败")


if __name__ == '__main__':
    workflowObj = workflow_forgetpassword_test()

    file = open("test_info.csv", "r")
    table = csv.reader(file)
    for raw in table:
        user_info = {}
        j = int(raw[6])
        url = raw[1]
        expect_result = raw[3]
        interface_name = raw[5]
        for i in range(7, 2 * j + 7, 2):
            user_info[raw[i]] = raw[i + 1]
        # print(user_info)
        workflowObj.workflow_test(url, user_info, expect_result, interface_name)
