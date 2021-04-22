"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:02 下午'
"""
from typing import List
import pytest
from Calculator import Calculator


@pytest.fixture(scope='session')
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
    yield calc  # return 记录上一次的执行结果，下次调用的时候，直接执行后面的动作
    # teardown
    print("teardown")


@pytest.fixture(params=[[0.1, 0, False], [2, 2, 2], [10, 1, 10]],
                ids=['zero', 'int', 'int1'])
def get_div_datas(request):
    return request.param


def pytest_collection_modifyitems(session, config, items: List):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'foo' in item.name:
            item.add_marker(pytest.mark.foo)
        elif 'last' in item.name:
            item.add_marker(pytest.mark.last)
