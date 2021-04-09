from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHunger:
    def setup(self):
        desired_caps = {
            "platformName": "iOS",
            "platformVersion": "14.3",
            "udid": "03831fa0c5b0f0646098e4e816e5d08e20f5a9d0",
            "bundleId": "me.ele.ios.eleme",
            "deviceName": "Joseph_beer",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "N5ZB83XTH3"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_hunger_add_coin(self):
        """
        打开饿了么
        进入我的页面
        点击超级吃货卡
        点击全部任务
        获取所有逛逛任务
        浏览每个逛逛任务
        完成
        """
        self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="我的"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '(//XCUIElementTypeOther[@name="a2ogi.14291182.Chihuoka.1"])[1]').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 滑动

        # self.driver.execute_script("mobile:dragFromToForDuration",
        #                            {"duration": 1, "element": None, "fromX": 1000, "fromY": 650, "toX": 100,
        #                             "toY": 100})
        self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="查看全部任务"]').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        # ele = '//XCUIElementTypeStaticText[@name="去浏览" or @name="去完成"]'
        ele = '//XCUIElementTypeOther[@name="做任务赚吃货豆"]/XCUIElementTypeOther[8]/XCUIElementTypeOther'
        task_list = self.driver.find_elements(MobileBy.XPATH, ele)
        num = len(task_list)
        print('num是', num)
        # 因为饿了么会自动更新任务列表，所以不需要每个使用for循环+1的方法
        # 任务数剩余比较少的时候 ，会变成去完成
        go_read = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="去浏览"]')
        go_doing = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="去完成"]')
        for i in task_list:
            # if self.driver.find_element(*go_read):
            #     self.driver.find_element(*go_read).click()
            # elif self.driver.find_element(*go_doing):
            self.driver.find_element(*go_doing).click()
            sleep(17)
            local = (MobileBy.XPATH, '//*[@name="返回"]')
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(local))
            self.driver.find_element(*local).click()



        # for i in task_list:
        #     j += 1
        #     self.driver.find_element(MobileBy.XPATH, f'(//XCUIElementTypeStaticText[@name="去浏览"])[{j}]').click()
        #     sleep(17)
        #     self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="返回"]').click()

        # if j > 5:
        #     self.driver.execute_script("mobile:dragFromToForDuration",
        #                                {"duration": 1, "element": None, "fromX": 1000, "fromY": 650, "toX": 100,
        #                                 "toY": 100})
        #     self.driver.find_element(MobileBy.XPATH, f'(//XCUIElementTypeStaticText[@name="去浏览"])[{j}]').click()
        #     sleep(20)
        #     self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="返回"]').click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, f'(//XCUIElementTypeStaticText[@name="去浏览"])[{j}]').click()
        #     sleep(20)
        #     self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="返回"]').click()
