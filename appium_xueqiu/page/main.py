from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find(By.XPATH, '(//*[@resource-id="com.xueqiu.android:id/tab_icon"])[2]').click()
        return Market(self._driver)
