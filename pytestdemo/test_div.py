"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:26 下午'
"""


class TestDiv:
    def test_div(self, connectDb, initcalc_class, get_div_datas):
        try:
            assert get_div_datas[2] == initcalc_class.div(get_div_datas[0], get_div_datas[1])
        except ZeroDivisionError:
            print("除数为0")
