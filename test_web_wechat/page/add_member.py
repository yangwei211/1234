import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_wechat.page.base_page import BasePage
from test_web_wechat.page.contact import ContactPage


class AddMemberPage(BasePage):

    def add_member(self):
        self.driver.find_element(By.ID, "username").send_keys("皮城女警22")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("0010")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13100001111")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        time.sleep(20)
        # 页面的return 分成两个部分
        # 1. 其他页面的 实例
        # 2. 用例所需要的断言
        # 注意： 不要写成 ContactPage
        # 快捷导入  alt + 回车
        return ContactPage(self.driver)

    def add_xxx(self):

        # 调用本身的实例
        # AddMemberPage()
        return self

