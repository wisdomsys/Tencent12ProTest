from appium import webdriver


class TestWebView:
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '10',
            # 'deviceName': 'emulator-5554',
            'deviceName': 'Q5S5T19424004010',
            'browserName': 'Browser',
            'noReset': True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview(self):
        self.driver.get('https://m.baidu.com')


