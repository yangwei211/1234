"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:02 下午'
"""
import pytest

from pytestdemo.Calculator import Calculator


@pytest.fixture()
def connectDb():
    # 相当于setup
    print('连接数据库操作')
    # return "database datas"
    yield "搜索结果"  # 返回后面的结果，yield 相当于return
    # 相当于 teardown操作
    print("断开连接数据库")


@pytest.fixture()
def login():
    print("login")
    usernmae = "hogwarts"
    password = "123"
    return usernmae, password


@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc
    # teardown
    print("teardown")


@pytest.fixture(params=[[0.1, 0, False], [2, 2, 2], [10, 1, 10]],
                ids=['zero', 'int', 'int1'])
def get_div_datas(request):
    return request.param
