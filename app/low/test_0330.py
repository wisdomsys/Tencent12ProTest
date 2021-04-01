import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'AEUSCQB6YXAIDQGY'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps['noReset'] = True
# desired_caps['dontStopAppOnReset'] = True
desired_caps['skipDeviceInitialization'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'com.xueqiu.android:id/home_search').click()
driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')

# driver.find_element_by_accessibility_id('xxx')
driver.back()
time.sleep(5)

driver.quit()
