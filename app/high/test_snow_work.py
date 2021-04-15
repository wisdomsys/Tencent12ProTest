from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestSnowWork:
    def setup_class(self):
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'')

    def teardown_class(self):
        print('teardown')
        self.driver.quit()

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown  ')
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('search_key,search_result', [('alibaba', '阿里巴巴'), ('jd', '京东')])
    def test_work(self, search_key, search_result):
        """
        使用录制功能完成上面的功能,搜索jd xiaomi alibaba
        进行简单的重构，使用pytest框架
        可以加入参数化，实现多条搜索搜索功能的测试用例
        合理使用set_class,setup,加快执行速度
        添加数据验证，assert
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(search_key)
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{search_result}']").click()
        ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{search_result}']/../..//*[@text='加自选']")
        if len(ele) > 0:
            ele[0].click()
            # self.driver.find_element(MobileBy.XPATH, f"//*[@text='{search_result}']/../..//*[@text='加自选']").click()
        else:
            print('已经加自选')
