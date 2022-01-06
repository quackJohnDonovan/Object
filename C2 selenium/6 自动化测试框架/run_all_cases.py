import unittest2

from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest2.defaultTestLoader.discover("./test_case", "test_*.py")

    # unittest2.TextTestRunner().run(suite)
    path = "./report/TestReport.html"
    file = open(path, "wb")  # w写，b二进制
    HTMLTestRunner(stream=file, verbosity=1, title="自动化测试报告", description="测试环境：Chrome", tester="何冰").run(suite)
