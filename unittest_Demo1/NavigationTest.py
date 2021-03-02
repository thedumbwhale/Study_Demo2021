import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NavigationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com/')
        driver = cls.driver  # 定义在全局中
        cls.search_field = driver.find_element_by_name('wd')  # 定义在全局中

    def testBrowserNavigation(self):
        self.search_field.clear()
        print('执行test1啊啊啊啊啊啊啊啊啊')

        self.search_field.send_keys('测试机1')
        self.search_field.submit()
        time.sleep(1)

        self.assertEqual('测试机1_百度搜索', self.driver.title)

        self.driver.back()
        self.assertTrue(WebDriverWait(self.driver, 30).until(expected_conditions.title_contains('百度一下')))

    def testBrowserNavigation2(self):
        driver = self.driver
        search_field = driver.find_element_by_name('wd')
        search_field.clear()
        print('执行test2')

        search_field.send_keys('测试机2')
        search_field.submit()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        time.sleep(10)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
