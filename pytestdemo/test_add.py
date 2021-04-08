"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 8:47 下午'
"""
import pytest

from Calculator import Calculator


class TestCal:

    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000]
    ], ids=['int1', 'float', 'bignum', 'zeronum'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    def test_add1(self):
        # calc = Calculator()
        assert 0.2 == self.calc.add(0.1, 0.1)

    def test_add2(self):
        # calc = Calculator()
        assert 2000 == self.calc.add(1000, 1000)

    def test_add2(self):
        # calc = Calculator()
        assert 1000 == self.calc.add(0, 1000)
