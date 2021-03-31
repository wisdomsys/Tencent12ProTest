from appium import webdriver
from selenium.webdriver.common.by import By


class TestSnowXpath:
    def setup(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'Q5S5T19424004010',
                        'appPackage': 'com.xueqiu.android', 'appActivity': '.view.WelcomeActivityAlias',
                        'noReset': True, 'skipDeviceInitialization': True, 'unicodeKeyboard': True,
                        'resetKeyboard': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_get_current(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/title_text" and @text="股票"]').click()
        # self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/stockCode' and @text=09988]")
        path = "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"
        # path = "//*[@text='09988']"
        current_price = self.driver.find_element(By.XPATH,path).text
        print(f'打印一下当前09988股票的价格是：{current_price}')
        assert float(current_price) > 200
