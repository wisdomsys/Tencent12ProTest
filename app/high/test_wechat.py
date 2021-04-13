from time import sleep

import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver


# 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(
# "保存").instance(0));'
class TestWechat:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10',
            'deviceName': 'Q5S5T19424004010',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': True,
            'skipDeviceInitialization': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'skipServerInstallation': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        print('teardown')
        self.driver.quit()

    def test_add_contact(self):
        print('添加联系人')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        name_element = self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/../android.widget.EditText')
        name_element.send_keys('霍格沃茨2')
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        phone = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机　")]/..//*[contains(@text,"手机号")]')
        phone.send_keys('13121571611')
        # 滑动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).scrollIntoView(new UiSelector().text("保存").instance(0));')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ac9').click()
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')
