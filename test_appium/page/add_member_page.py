"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
# from test_appium.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from test_appium.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        # return True
