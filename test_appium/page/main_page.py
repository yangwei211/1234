"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:16 下午'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.contactlist_page import ContactListPage


class MainPage(BasePage):
    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click 通讯录
        self.find(*self.contact_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)
