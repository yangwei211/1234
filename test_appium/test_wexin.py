"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/22 8:59 下午'
"""

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException


class TestWX:
    def setup_class(self):
        # 生成测试数据的第三方库
        self.faker = Faker('zh-CN')
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

    def setup(self):
        # 初始化，首页的启动
        self.driver.launch_app()

    def teardown(self):
        # 首页的关闭
        self.driver.close_app()

    def teardown_class(self):
        # 资源消毁，消毁driver
        self.driver.quit()

    def test_daka(self):
        # 测试用例
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 强制等待
        # sleep(5)
        # uiautomator的定位方式，android 原生的定位方式，滚动查找某个 文字
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        # self.driver.update_settings({'waitForIdleTimeout':0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def swipe_find(self, text, num=3):
        # num : 默认查找次数
        # 进入滑动查找，改变隐式等待时长，提高查找速度
        self.driver.implicitly_wait(1)

        # 滑动查找，通过外部传递的num次数，决定查找次数
        for i in range(0, num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                # 滑动一页，继续查找
                size = self.driver.get_window_size()
                # self.driver.get_window_rect()
                width = size['width']
                height = size['height']
                # 'width', 'height'
                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 完成滑动操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")

    @pytest.mark.parametrize('a', [
        'aa', 'bb'
    ])
    def test_addcontact(self, a):
        # faker
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.swipe_find('添加成员').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../"
                                 "android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(
            phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
