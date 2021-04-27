import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self.steps('../data/search1.yaml')

    def is_choose(self, name):
        return self.steps('../data/search2.yaml')

    def reset(self, reset):
        return self.steps('../data/search3.yaml')

# ele = self.finds(By.XPATH,
# f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="已添加"]')
