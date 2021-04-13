from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base_page import BasePage
from test_app.page.member_invite_menu import MemberInviteMenu


# 通讯录
class AddressList(BasePage):
    def add_member(self):
        # 通讯录 -> 添加成员
        self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInviteMenu(self._driver)
