from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestHunger:
    def setup_class(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Q5S5T19424004010",
            "appPackage": 'me.ele',
            "appActivity": 'me.ele.Launcher',
            # 'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        self.driver.find_element(MobileBy.ID, 'me.ele:id/img_4').click()

    def teardown(self):
        pass

    def logout(self):
        self.driver.find_element(MobileBy.ID, 'me.ele:id/iv_setting').click()
        self.driver.find_element(MobileBy.ID, 'me.ele:id/logout').click()

    def goto_login(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="me.ele:id/id_magex_mistview"]/android.widget.ImageView').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="密码登录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"用户名")]').send_keys(user)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="密码"]').send_keys(pwd)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="登录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="同意"]').click()

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
        length = self.driver.find_elements(MobileBy.XPATH, '//*[@resource-id="me.ele:id/id_magex_mistview"]')
        if len(length) < 5:
            self.goto_login()
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, '(//*[@resource-id="me.ele:id/id_magex_mistview"])[2]').click()
        # 因为找不到查看全部任务的元素，所以得滑动屏幕
        sleep(3)
        action = TouchAction(self.driver)
        action.press(x=850, y=1600).wait(200).move_to(x=850, y=1200).release().perform()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="查看全部任务"]').click()
        all_list = ['去浏览', '去完成']
        goto_browser = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{all_list[0]}"]')
        goto_doing = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{all_list[1]}"]')
        ele_list = (MobileBy.XPATH, '(//*[@class="android.widget.ListView"])[2]/android.view.View')
        scroll1 = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new ' \
                  f'UiSelector(' \
                  f').text("{all_list[0]}").instance(0));'
        scroll2 = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new ' \
                  f'UiSelector(' \
                  f').text("{all_list[1]}").instance(0));'
        while True:
            if goto_browser > 0:
                self.driver.find_element_by_android_uiautomator(scroll1).click()
                sleep(17)
                self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"返回")]').click()
            elif goto_doing > 0:
                self.driver.find_element_by_android_uiautomator(scroll2).click()
                sleep(17)
                self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"返回")]').click()
            print('该账号任务均完成，切换账号')
            break
        print('没有任务')
        return True
