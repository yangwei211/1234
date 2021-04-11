"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:05 下午'
"""
import pytest


@pytest.fixture()
def login():
    print("这是企业微信的登录")
