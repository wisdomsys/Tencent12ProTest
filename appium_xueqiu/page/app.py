import yaml
from appium import webdriver

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        desi_read = yaml.safe_load(open('../../UI自动化测试框架/page/configuration.yaml'))['caps']
        if self._driver is None:
            caps = dict()
            caps['platformName'] = desi_read['platformName']
            caps['platformVersion'] = desi_read['platformVersion']
            caps['deviceName'] = desi_read['deviceName']
            caps['appPackage'] = desi_read['appPackage']
            caps['appActivity'] = desi_read['appActivity']
            caps['noReset'] = desi_read['noReset']
            caps['udid'] = 'emulator-5554'
            # 初始化driver
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)
