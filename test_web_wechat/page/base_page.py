import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """
    # 没有参数传入， 会取默认None ,如果有参数传入,会取传入的参数
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，每一次调用find 方法，就会轮询查找元素是否存在
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver
