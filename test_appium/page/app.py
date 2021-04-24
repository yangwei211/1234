"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:14 下午'
"""
# app.py  app相关的操作，启动，关闭，重启
from appium import webdriver

from test_appium.page.main_page import MainPage


class App:

    def start(self):
        # 启动app
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["settings[waitForIdleTimeout]"] = 0
        # caps['dontStopAppOnReset'] = True
        caps["noReset"] = "true"
        caps['skipDeviceInitialization'] = True
        # 客户端与服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待,更智能，中间任何时间等到某个元素都停止查找，继续往后执行，
        # 每次调用find_element的时候都会激活这种等待方式
        self.driver.implicitly_wait(5)
        return self

    def restart(self):
        # self.driver.
        pass

    def stop(self):
        pass

    def goto_main(self):
        # 入口
        return MainPage(self.driver)
