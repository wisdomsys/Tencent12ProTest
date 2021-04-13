# 邀请成员
from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base_page import BasePage


class MemberInviteMenu(BasePage):

    def member_by_manul(self):
        # 手动添加成员
        # 局部导入
        from test_app.page.contact_add import ContactAdd
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        return ContactAdd(self._driver)

    def get_toast(self):
        # self.find(MobileBy.XPATH, '//*[@text="添加成功"]')
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
