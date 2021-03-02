import unittest


# 两条测试用例

class Demo1(unittest.TestCase):
    def setUp(self):
        print("———————————**用例执行开始**———————————")

    def tearDown(self):
        print("———————————**用例执行结束**———————————\n")

    def testcase1(self):
        print("测试用例1")

    def testcase2(self):
        print("测试用例2")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(map((Demo1, ['testcase1', 'testcase2'])))
    runner = unittest.TextTestRunner()
    runner.run(suite)
