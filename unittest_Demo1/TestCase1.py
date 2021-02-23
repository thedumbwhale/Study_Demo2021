import unittest


class TestCase1(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    def testCase1(self):
        print("aa")

    def testCase2(self):
        print("aa1")


class TestCase2(unittest.TestCase):
    # def setUp(self):
    # def tearDown(self):
    def testCase1(self):
        print("bb")

    def testCase2(self):
        print("bb1")


if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
    print("UnitTest成功！")
