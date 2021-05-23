import json

import requests

from service.api.base_api import BaseApi


class WeWork(BaseApi):
    # 可以不用加的，只是为了声明类型，python也开始支持类型了，是python3的一个技巧
    token: str = None

    def get_token(self):
        # r = requests.get(
        #     "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     params={
        #         "corpid": "wwd6da61649bd66fea",
        #         "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
        #     }
        # )

        # 具体的api对象通过这样的设计，可以实现数据化，为以后的自动生成垫定了一个好的基础
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params": {
                "corpid": "wwd6da61649bd66fea",
                "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
            }
        }
        r = self.request(data)

        assert r.status_code == 200
        self.token = r.json()['access_token']
