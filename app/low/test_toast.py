from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10',
            'deviceName': 'Q5S5T19424004010',
            'appPackage': 'com.touchboarder.android.api.demos',
            'appActivity': 'com.example.android.apis.view.PopupMenu1',
            'noReset': True,
            'automationName': 'uiautomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'MAKE A POPUP!').click()
        # ACCESSIBILITY_ID  对应的content-desc

        self.driver.find_element(MobileBy.XPATH, '//*[@text="MAKE A POPUP!"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()

        # print(self.driver.page_source)
        # 方法一
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)

        # 方法二
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked")]').text)
