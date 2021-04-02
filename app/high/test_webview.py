from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView:
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '10',
            # 'deviceName': 'emulator-5554',
            'deviceName': 'Q5S5T19424004010',
            'browserName': 'Chrome',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
            # 'chromedriverExecutable':'xxxxx'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        """
        打开百度
        报错是因为访问百度会出现一个弹窗 是否允许获取位置权限>invalid argument: invalid locator
        """
        self.driver.get('https://m.baidu.com')
        # print(self.driver.find_element(MobileBy.ID, 'com.android.chrome:id/text').is_displayed())
        path = (MobileBy.ID, 'com.android.chrome:id/text')
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(path))
        print(self.driver.find_element(*path).text)
        self.driver.find_element(By.ID, 'index-kw').click()
        self.driver.find_element(By.ID, 'index-kw').send_keys('appium')
        self.driver.find_element(By.ID, 'index-bn').click()
