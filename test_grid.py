from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote


class TestGrid:
    def test_grid(self):
        hub_url = 'http://169.254.18.197:4444/wd/hub'
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1, 5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get('https://www.baidu.com')
