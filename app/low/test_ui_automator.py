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

    def test_my_info(self):
        """
        用例
            打开【雪球】app
            点击我的，进入到个人信息页面
            输入用户名，密码
            点击登录
        """
        # self.driver.find_element_by_android_uiautomator(
        # 'new UiSelector().resourceId("com.xueqiu.android:id/tab_icon")[4]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout['
                                 '5]/android.widget.ImageView').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('12345')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('12345')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

        # 多属性定位
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("xxx").text("我的").className("xxx")')

        # 父子关系定位 childSelector
        son = 'resourceId("xxxx").childSelector(text("xxx"))'

        # 兄弟定位 formParent
        brother = "resourceId('').formParent(text('xxx'))"

        # 实现滚动查找元素
        # 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("").instance(0));'

    def test_scroll_find_element(self):
        # self.driver.find_element(By.XPATH,'//*[@text="推荐"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("allSBnow").'
                                                        'instance(0));')


        # path = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("babygirl").instance(0));'
        # self.driver.find_element_by_android_uiautomator(path)


# ‘new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(“查找的元素文本”).instance(0));’