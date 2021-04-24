"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:18 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from test_appium.page.add_member_page import AddMemberPage
from test_appium.page.base_page import BasePage


class ContactListPage(BasePage):

    def goto_addmember(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)
