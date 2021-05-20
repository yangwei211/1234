import json

import requests


class TestWeWork:
    # pytest识别是否是测试方法的时候，会排除带有初始化方法的类，所以不能加__init__
    # def __init__(self):
    #     self.token=""

    def setup_class(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": "wwd6da61649bd66fea",
                "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        self.token = r.json()['access_token']

    # def test_token(self):
    #     r = requests.get(
    #         "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #         params={
    #             "corpid": "wwd6da61649bd66fea",
    #             "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
    #         }
    #     )
    #     print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    #     assert r.status_code == 200
    #     print(r.json()['access_token'])

    def test_search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        # 新增标签
        #todo: 数据唯一性，1.提前清理数据（推荐） 2.使用时间戳代表唯一性
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name": "tag_group_052001",
                "tag": [
                    {
                        "name": "tag_052001",
                    }
                ]
            }
        )

        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 0

        # todo：代码冗余
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag_delete(self):
        r=requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": "etQKd-CgAAXKugrgAns8p1HiVSQZzFdA"
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 0
