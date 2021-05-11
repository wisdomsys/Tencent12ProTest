import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self._params['name'] = name
        print(name)
        self.steps('../data/search.yaml', 'search')

    def add(self, name):
        self._params['name'] = name
        self.steps('../data/search.yaml', 'add')

    def is_choose(self, name):
        self._params['name'] = name
        return self.steps('../data/search.yaml', 'is_choose')

    def reset(self, name):
        self._params['name'] = name
        return self.steps('../data/search.yaml', 'reset')

# ele = self.finds(By.XPATH,
# f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="已添加"]')
