import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestGetAttr:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10',
            'deviceName': 'Q5S5T19424004010',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'automationName': 'uiautomator2'
        }
        # desired_caps['dontStopAppOnReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_search(self):
        """
        打开雪球
        打开搜索按钮
        输入'搜索词' 点击搜索， 'alibaba' or 'xiaomi'
        点击第一条搜索结果
        去判断股票价格
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        path = '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]'
        current_price = self.driver.find_element(MobileBy.XPATH, path).text
        print(type(current_price))
        expect_price = 226
        assert_that(current_price, close_to(expect_price, 10))
