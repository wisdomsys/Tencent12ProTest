import pytest
from appium import webdriver


class TestGetAttr:
    def setup(self):
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
        # desired_caps['dontStopAppOnReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
        print(search_ele.get_attribute('content-desc'))
        print(search_ele.get_attribute('resourceId'))
        print(search_ele.get_attribute('enabled'))
        print(search_ele.get_attribute('clickable'))
        print(search_ele.get_attribute('bounds'))
        assert 'search' in search_ele.get_attribute('resourceId')

    def test_case(self):
        a = 10
        b = 20
        assert a < b
