import unittest2
from interface_unittest_v1 import test_mulinterface

if __name__ == '__main__':
    # testdir = "./"
    # discover = unittest2.defaultTestLoader.discover(testdir, pattern="interface*.py")
    # runner = unittest2.TextTestRunner()
    # runner.run(discover)

    # 方法1
    # unittest2.main()
    # 方法2
    # suite = unittest2.TestSuite()
    # suite.addTest(test_mulinterface("test_case1"))
    # runner = unittest2.TextTestRunner()
    # runner.run(suite)
    # 方法3
    testdir = "./"
    discover = unittest2.defaultTestLoader.discover(testdir, pattern="interface*.py")
    runner1 = unittest2.TextTestRunner()
    runner1.run(discover)
