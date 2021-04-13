from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHunger:
    def setup_class(self):
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

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        print('这是setup')

    def teardown(self):
        # 返回
        # self.driver.find_element()
        pass

    def test_hunger_add_coin(self):
        """
        打开饿了么
        进入我的页面
        点击超级吃货卡
        点击全部任务
        获取所有逛逛任务
        浏览每个逛逛任务，并打印任务名称
        完成
        """
        self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="我的"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '(//XCUIElementTypeOther[@name="a2ogi.14291182.Chihuoka.1"])[1]').click()
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # 滑动
        # self.driver.execute_script("mobile:dragFromToForDuration",
        #                            {"duration": 1, "element": None, "fromX": 1000, "fromY": 650, "toX": 100,
        #                             "toY": 100})
        self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="查看全部任务"]').click()

        # self.driver.switch_to.context(self.driver.contexts[-1])
        ele = '//XCUIElementTypeOther[@name="做任务赚吃货豆"]/XCUIElementTypeOther[8]/XCUIElementTypeOther'
        task_list = self.driver.find_elements(MobileBy.XPATH, ele)
        num = len(task_list)
        # 因为饿了么会自动更新任务列表，所以不需要每个使用for循环+1的方法
        # 任务存在去浏览和去完成两个状态，所有需要判断哪种元素存在
        go_to_read = '//*[@name="去浏览"]'
        go_to_doing = '//*[@name="去完成"]'
        go_read = self.driver.find_element(MobileBy.XPATH, go_to_read)
        go_doing = self.driver.find_element(MobileBy.XPATH, go_to_doing)
        # title = (MobileBy.XPATH, f'{go_to_read}/../../XCUIElementTypeOther[2]')
        while True:
            # try:
            #     if go_read:
            #         go_read.click()
            #         print(self.driver.find_element(MobileBy.XPATH, f'{go_to_read}/../../XCUIElementTypeOther[2]'))
            #     elif go_doing:
            #         go_doing.click()
            #         print(self.driver.find_element(MobileBy.XPATH, f'{go_to_doing}/../../XCUIElementTypeOther[2]'))
            #     else:
            #         print('任务已经完成')
            #         break
            # except Exception as e:
            #     print(e)
            if go_read:
                go_read.click()
                # print(self.driver.find_element(MobileBy.XPATH, f'{go_to_read}/../../XCUIElementTypeOther[2]'))
            elif go_doing:
                go_doing.click()
                # print(self.driver.find_element(MobileBy.XPATH, f'{go_to_doing}/../../XCUIElementTypeOther[2]'))
            else:
                print('任务已经完成')
                break
            sleep(17)
            print(self.driver.get_window_size())
            # TouchAction(self.driver).press(el=None, x=20, y=200).move_to(el=None, x=0,
            #                                                              y=200).release().perform()
            back = self.driver.find_element(MobileBy.XPATH, '//*[@name="返回"]')
            # back = self.driver.find_element(MobileBy.XPATH, '//XCUIElementTypeButton[@name="返回"]')
            back_two = self.driver.find_element(MobileBy.XPATH, '//*[@name="任务完成点击返回"]')
            self.driver.switch_to.context(self.driver.contexts[-1])
            if back:
                back.click()
            else:
                back_two.click()

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
