import time
from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'Q5S5T19424004010',
                        'appPackage': 'com.xueqiu.android', 'appActivity': '.view.WelcomeActivityAlias',
                        'noReset': True, 'skipDeviceInitialization': True, 'unicodeKeyboard': True,
                        'resetKeyboard': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        # time.sleep(5)
        # show_display = self.driver.find_element(By.XPATH, 'com.xueqiu.android:id/title_text and @text="推荐"')
        # print(show_display.is_displayed())
        # if show_display == 'true':
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        get_window_rect = self.driver.get_window_rect()
        width = get_window_rect['width']
        height = get_window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        time.sleep(10)


if __name__ == '__main__':
    pytest.main()
