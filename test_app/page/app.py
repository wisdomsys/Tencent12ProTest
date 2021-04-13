from appium import webdriver
import yaml

from test_app.page.base_page import BasePage
from test_app.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = yaml.safe_load(open('../datas/configuration.yaml'))['caps']
            print(caps)
            desired_caps = {
                'platformName': caps['platformName'],
                'platformVersion': caps['platformVersion'],
                'deviceName': caps['deviceName'],
                'appPackage': caps['appPackage'],
                'appActivity': caps['appActivity'],
                'noReset': caps['noReset'],
                'skipDeviceInitialization': caps['skipDeviceInitialization'],
                'unicodeKeyboard': caps['unicodeKeyboard'],
                'resetKeyboard': caps['resetKeyboard'],
                'skipServerInstallation': caps['skipServerInstallation']
            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
