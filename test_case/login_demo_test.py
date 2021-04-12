import unittest
from selenium import webdriver

class TestDemo:
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com')
    #
    # def teardown(self):
    #     self.driver.quit()
    #
    def test_demo(self):
        a = 1
        b = 2
        assert a != b