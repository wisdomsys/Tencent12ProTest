from appium.webdriver.common.mobileby import MobileBy

from test_app.page.address_list import AddressList


# 主函数入口
from test_app.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        # 消息
        pass

    def goto_address_list(self):
        # 通讯录
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressList(self._driver)

    def goto_workbench(self):
        # 工作台
        pass

    def goto_profile(self):
        # 我的
        pass
