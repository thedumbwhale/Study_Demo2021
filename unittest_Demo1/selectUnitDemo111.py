import unittest


class SQL168(unittest.TestCase):
    def setUp(self) -> None:
        print("a")

    def tearDown(self) -> None:
        print("b")

    def testcase1(self):
        print("Case1")
        print("Case2")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(map((SQL168, ['testcase1'])))
    runner = unittest.TextTestRunner()
    runner.run(suite)
