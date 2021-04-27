import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    logging.basicConfig(level=logging.INFO)
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

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
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

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 'send' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len > 0' == action:
                    ele = self.finds(step['by'], step['locator'])
                    print('长度是：', len(ele))
                    return len(ele) > 0
