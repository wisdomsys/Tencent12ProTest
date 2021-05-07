import json
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    _params = {}
    _black_list = [
        (By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.XPATH, '//*[@text="允许"]'),
        (By.XPATH, '//*[@text="确认"]'),
        (By.ID, 'com.xueqiu.android:id/tv_agree'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_num = 0
    _max_num = 3

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly_wait(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self,name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_get_text(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    @handle_black
    def steps(self, path, name):
        with open(path) as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 'send' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len > 0' == action:
                    ele = self.finds(step['by'], step['locator'])
                    return len(ele) > 0
