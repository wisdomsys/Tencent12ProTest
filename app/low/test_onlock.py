from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestOnLock:
    def setup(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'Q5S5T19424004010',
                        'appPackage': 'cn.kmob.screenfingermovelock', 'appActivity': 'com.samsung.ui.FlashActivity',
                        'noReset': True, 'skipDeviceInitialization': True, 'unicodeKeyboard': True,
                        'resetKeyboard': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_on_locking(self):
        action = TouchAction(self.driver)
        # self.driver.find_element(By.ID, 'android:id/button1').click()
        # if enter.is_enabled() == True:
        #     enter.click()
        self.driver.find_element(By.ID, 'cn.kmob.screenfingermovelock:id/patternTxt').click()
        window = self.driver.get_window_rect()
        print(window)
        width = window['width']
        height = window['height']
        x1 = int(width / 4)
        y1 = int(height / 6)
        x2 = x1 * 2
        x3 = x1 * 3
        y2 = y1 * 2
        y3 = y1 * 3
        action.press(x=x1, y=y1).move_to(x=x2, y=y1).move_to(x=x3, y=y1).move_to(x=x3, y=y2).move_to(x=x3,
                                                                                                     y=y3).wait(100).release().perform()
