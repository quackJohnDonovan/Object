
import unittest2
from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    case = unittest2.defaultTestLoader.discover("./test_case", "title*.py")
    path = "./report/TestReport.html"
    file = open(path, "wb")
    HTMLTestRunner(stream=file, verbosity=1, title="自动化作业测试报告", description="测试环境：Chrome", tester="何冰").run(case)
