import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
        pass

    # def test_search(self, search_key, types, price):
    #     """
    #     打开雪球
    #     打开搜索按钮
    #     输入'搜索词' 点击搜索， 'alibaba' or 'xiaomi'
    #     点击第一条搜索结果
    #     去判断股票价格
    #     """
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search').click()
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
    #     path = '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]'
    #     price = self.driver.find_element(MobileBy.XPATH, path).text
    #     current_price = float(price)
    #     expect_price = 210
    #     assert_that(current_price, close_to(expect_price, expect_price * 0.1))
    @pytest.mark.parametrize('search_key, types, expect_price', [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810', 25)
    ])
    def test_search(self, search_key, types, expect_price):
        """
        打开雪球
        打开搜索按钮
        输入'搜索词' 点击搜索， 'alibaba' or 'xiaomi'
        点击第一条搜索结果
        去判断股票价格
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(search_key)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        path = f'//*[@text="{types}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]'
        price_text = self.driver.find_element(MobileBy.XPATH, path).text
        current_price = float(price_text)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
