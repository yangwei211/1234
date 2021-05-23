import json

import jsonpath as jsonpath
import requests

from service.api.wework_api import WeWork


class Tag(WeWork):
    def search(self):
        """

        :return:
        """
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {}
        }
        return self.request(data)

    def add(self, tag_list, group_name, **kwargs):
        if 'json' in kwargs:
            json_data=kwargs['json']
        else:
            json_data={
                'group_name': group_name,
                'tag': tag_list
            }
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": json_data
        }

        return self.request(data)

    # def add(self, json):
    #     # 可以借鉴 requests.request与requests.get .post 的封装思路
    #     data = {
    #         "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
    #         "method": "post",
    #         "params": {"access_token": self.token},
    #         "json": json
    #     }
    #
    #     return self.request(data)

    def delete(self, tag_id_list):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id_list
            }
        }
        return self.request(data)

    def clear(self):
        r = self.search()
        tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        # jsonpath.jsonpath(r.json(), "$..tag.id")
        r = self.delete(tag_id_list)
        return r
