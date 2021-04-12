"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 4:16 下午'
"""
import pytest


# @pytest.mark.second
def test_foo():
    assert True


# @pytest.mark.last
def test_last():
    print("last")


# @pytest.mark.first
def test_bar():
    assert True
