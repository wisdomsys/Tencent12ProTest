from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self):
        # send alibaba
        # click
        # ...
        self.find(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.find(By.XPATH, '//*[@text="阿里巴巴"]').click()
        self.find(By.XPATH,
                  '//*[contains(@resource-id,"stock_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()

    def is_choose(self):
        ele = self.finds(By.XPATH,
                         '//*[contains(@resource-id,"stock_item_container")]//*[@text="阿里巴巴"]/../..//*[@text="已添加"]')
        return len(ele) > 0
