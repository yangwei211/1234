"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
# from test_appium.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../"
                  "android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/..//"
                  "android.widget.EditText").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from test_appium.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
