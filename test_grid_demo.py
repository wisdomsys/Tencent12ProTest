from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities


class TestGrid:
    def test_grid(self):
        selenium_grid_url = 'http://127.0.0.1:4444/wd/hub'
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1, 5):
            driver = Remote(command_executor=selenium_grid_url, desired_capabilities=capability)
            driver.get('https://www.baidu.com')
