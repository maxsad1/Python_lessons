import unittest
from func import sum_


# 2 + 2 = 4
# 1230139048019759814598275728974589 + 59823745982745897298345798237459827345
# -2 + 2 = 0
# 5 + 0 = 5
# 2.5 + 1.5 = 4.0
# 2.5 + 1 = 3.5

class TestSum(unittest.TestCase):
    """docstring for TestSum"""

    def startup(self):
        """Приготовления перед выполнением теста"""
        ...

    def teardown(self):
        """Приборка после выполнения теста"""
        ...

    def test1(self):
        """2 + 2 = 4"""
        res = sum_(2, 2)
        self.assertEqual(res, 4)

    def test2(self):
        """1230139048019759814598275728974589 +
        59823745982745897298345798237459827345
        """
        a = 1230139048019759814598275728974589
        b = 59823745982745897298345798237459827345
        expected = a + b
        res = sum_(a, b)
        self.assertEqual(res, expected)

    def test3(self):
        """2.5 + 1.5 = 4.0"""
        res = sum_(2.5, 1.5)
        self.assertEqual(res, 4.0)

    def test4(self):
        """-2 + 2 = 0"""
        res = sum_(-2, 2)
        self.assertEqual(res, 0)

    def test5(self):
        """2.534 + 1.523 = 4.057"""
        res = sum_(2.534, 1.523)
        self.assertEqual(res, 4.057)
