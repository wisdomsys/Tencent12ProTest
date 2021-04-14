from appium.webdriver.webdriver import WebDriver
import yaml
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _black_list = [(By.ID, 'com.xueqiu.android:id/iv_close')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)
            raise e

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if 'by' in step.keys():
                element = self.find(step['by'], step['locator'])
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    element.click()
