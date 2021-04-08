"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 9:09 下午'
"""
import pytest


@pytest.mark.parametrize('key,result', [
    ['appium', 200], ['selenium', 200], ['requests', 200], ['docker', 300]
], ids=['a', 'b', 'c', 'd'])
def test_interface(key, result):
    url = f"http://ceshiren.com/key={key}"
    print(url, result)


@pytest.mark.parametrize('a,b', [
    [1, 1], [100, 100]
])
class TestDemo:
    def test_a(self, a, b):
        print(a, b)

    def test_b(self, a, b):
        print(a, b)


# a : int,string,float
# b:  1, 2, 3

# 笛卡尔积
@pytest.mark.parametrize('c', ['x', 'y', 'z'])
@pytest.mark.parametrize('b', [1, 2, 3])
@pytest.mark.parametrize('a,d', [['int', 'a'], ['string', 'b'], ['float', 'c']])
def test_ab(a, d, b, c):
    print(a, b, c, d)
