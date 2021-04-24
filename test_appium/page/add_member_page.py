"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
# from test_appium.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class AddMemberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def addmember_bymenual(self):
        # click 手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from test_appium.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        # return True
