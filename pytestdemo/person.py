"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 9:32 下午'
"""


class Father:
    def make_computer(self):
        print("make")


class Person(Father):

    def get_name(self):
        return "hogwarts"

    def get_age(self):
        self.get_name()
        print("11")


print(Person().get_age())
Person().make_computer()
