import unittest
# import random
from main import turn, user_input


class TestTurn(unittest.TestCase):
    """docstring for TestTurn"unittest.TestCase"""

    def test_last(self):
        sticks = 1
        comp_takes = turn(sticks)
        self.assertEqual(comp_takes, 1)

    def test_zero(self):
        sticks = 0
        self.assertRaises(ValueError, turn, sticks)

    def test_negative(self):
        sticks = -5
        self.assertRaises(ValueError, turn, sticks)

    def test_two(self):
        sticks = 2
        comp_takes = turn(sticks)
        self.assertEqual(comp_takes, 1)

    def test_three(self):
        sticks = 3
        comp_takes = turn(sticks)
        self.assertEqual(comp_takes, 2)

    def test_right_result(self):
        sticks = range(4, 21)
        for s in sticks:
            comp_takes = turn(s)
            self.assertTrue(1 <= comp_takes <= 3)

    def test_win_condition(self):
        sticks_left = [21, 17, 13, 9, 5, 1]
        for sticks in range(2, 20):
            if sticks not in sticks_left:
                comp_takes = turn(sticks)
                self.assertTrue((sticks - comp_takes) in sticks_left)


def input_single(x):
    def input(p):
        return str(x)
    return input


def input_many(values):
    def input(p):
        for val in values:
            yield str(val)
    return input


class UserInput(unittest.TestCase):
    """docstring for Userunittest.TestCase"""

    def test_one(self):
        res = user_input(21, inp_func=input_single("1"))
        self.assertEqual(res, 1)

    def test_two(self):
        res = user_input(21, inp_func=input_single("2"))
        self.assertEqual(res, 2)

    def test_three(self):
        res = user_input(21, inp_func=input_single("3"))
        self.assertEqual(res, 3)
