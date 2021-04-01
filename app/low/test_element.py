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

    def test_search(self):
        print('搜索测试用例')
        """
        打开雪球app
        点击搜索输入框
        向搜索输入框里面输入'阿里巴巴'
        在搜索结果里选择阿里巴巴然后进行点击
        获取这只香港 阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴').click()
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element(By.ID,'com.xueqiu.android:id/current_price').text)
        assert current_price < 225

        sleep(3)


if __name__ == '__main__':
    pytest.main()
