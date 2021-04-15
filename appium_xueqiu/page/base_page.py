import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
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

    def finds(self, locator, value):
        if isinstance(locator, tuple):
            elements = self._driver.find_element(*locator)
        else:
            elements = self._driver.find_element(locator, value)
        return elements

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # if isinstance(locator, tuple):
            #     element = self._driver.find_element(*locator)
            # else:
            #     element = self._driver.find_element(locator, value)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹窗
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
            raise e

    def find_get_text(self, locator, value: str = None):
        element: WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator,
                                                                                  tuple) else self._driver.find_element(
                locator, value).text
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹窗
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
            raise e
