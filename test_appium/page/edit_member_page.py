"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
# from test_appium.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class EditMemberPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../"
                                 "android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//"
                                 "android.widget.EditText").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from test_appium.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
