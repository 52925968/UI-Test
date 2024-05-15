from appium.options.android import UiAutomator2Options
from selenium import webdriver

from base_page import BasePage


class App(BasePage):

    # 启动app
    def start(self):
        # _package = "com.pinsmedical.pinslife"
        # _activity = "com.pinsmedical.pinslife.component.home.MainActivity"

        _package = "com.pinsmedical.s505_android"
        _activity = "com.pinsmedical.s505_android.component.MainActivity"
        # print ('_driver=',self._driver)
        if self._driver is None:
            desir_cap = {
                "appPackage": _package,
                "appActivity": _activity,
                "platformName": "Android",
                "platformVersion": "10",
                "dontStopAppOnReset": True,
                "deviceName": "1c4508bf",  # 设备名称
                "automationName": "uiautomator2",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            options = UiAutomator2Options().load_capabilities(desir_cap)   #appium-python-client 版本较高 需要导入UIAutomator2Options
            self._driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", options=options)
            self._driver.implicitly_wait(5)  # 隐式等待5s

        else:
            self._driver.start_activity(_package, _activity)
        # return self


    def quit(self):
        self._driver.quit()


if __name__ == "__main__":
    app = App()
    app.start()

