# 完善邀请信息页面
from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        name_element = self.find(MobileBy.XPATH, '//*[@text="姓名　"]/../android.widget.EditText')
        name_element.send_keys('霍格沃茨4')
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH,
                  '//*[@text="性别"]/..//*[contains(@class,"TextView") and @text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_mobile(self):
        phone = self.find(MobileBy.XPATH, '//*[contains(@text,"手机　")]/..//*[contains(@text,"手机号")]')
        phone.send_keys('13121571613')
        return self

    def click_save(self):
        # 局部导入
        from test_app.page.member_invite_menu import MemberInviteMenu
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                         '0)).scrollIntoView(new UiSelector().text("保存").instance(0));')
        self.find(MobileBy.ID, 'com.tencent.wework:id/ac9').click()

        return MemberInviteMenu(self._driver)
