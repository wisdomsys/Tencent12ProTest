from time import sleep

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'Q5S5T19424004010',
                        'appPackage': 'com.xueqiu.android', 'appActivity': '.view.WelcomeActivityAlias',
                        'noReset': True, 'skipDeviceInitialization': True, 'unicodeKeyboard': True,
                        'resetKeyboard': True}
        # desired_caps['dontStopAppOnReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_attr(self):
        """
        打开雪球app
        定位首页搜索输入框
        判断搜索框的是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索输入框里面输入'alibaba'
        判断阿里巴巴是否可见
        如果可见，打印搜索成功 并点击，如果不可见，打印'搜索失败'
        """
        element = self.driver.find_element(By.ID, 'com.xueqiu.android:id/home_search')
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled:
            element.click()
            self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_element = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # alibaba_element.is_displayed()
            # print(alibaba_element.get_attribute('displayed'))
            element_display = alibaba_element.get_attribute('displayed')
            if element_display == 'true':
                print('搜索成功')
            else:
                print('搜索失败')


if __name__ == '__main__':
    pytest.main()
