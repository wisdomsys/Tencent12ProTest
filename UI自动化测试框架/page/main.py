from selenium.webdriver.common.by import By

from UI自动化测试框架.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        self.steps('../page/main.yaml')

    def goto_windows(self):
        self.find(By.ID, 'com.xueqiu.android:id/post_status').click()
        self.find(By.ID, 'com.xueqiu.android:id/home_search').click()
        # self.find(By.ID, 'com.xueqiu.android:id/iv_close').click() # 弹窗关闭
