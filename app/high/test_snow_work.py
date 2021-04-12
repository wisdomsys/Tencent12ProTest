from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy


class SnowWork:
    def setUpClass(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10',
            'deviceName': 'Q5S5T19424004010',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            'skipDeviceInitialization': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4728:wd/hub',desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print('teardown')
        self.driver.quit()

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown  ')
        self.driver.find_element(MobileBy.XPATH,'')

    def test_work(self):
        """
        使用录制功能完成上面的功能,搜索jd xiaomi alibaba
        进行简单的重构，使用pytest框架
        可以加入参数化，实现多条搜索搜索功能的测试用例
        合理使用set_class,setup,加快执行速度
        添加数据验证，assert
        """
        pass
