from appium import webdriver

desire_cap = {
    "platformName": "android",
    "deviceName": "AEUSCQB6YXAIDQGY",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    'noReset': True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_cap)
driver.implicitly_wait(10)
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
    ".ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
    ".FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget"
    ".RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.LinearLayout/android"
    ".widget.TextView")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
    ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
    ".RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView"
    "/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el4.click()
