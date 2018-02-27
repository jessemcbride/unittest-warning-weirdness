import unittest
import warnings

from secondary import d, e, f


class TestSecondary(unittest.TestCase):

    def test_d(self):
        with warnings.catch_warnings(record=True) as warning_list:
            d()

            self.assertTrue(len(warning_list), 1)

    def test_e(self):
        with warnings.catch_warnings(record=True) as warning_list:
            e()

            self.assertTrue(len(warning_list), 1)

    def test_f(self):
        with warnings.catch_warnings(record=True) as warning_list:
            f()

            self.assertTrue(len(warning_list), 1)

    def test_all_three(self):
        with warnings.catch_warnings(record=True) as warning_list:
            d()
            e()
            f()

            self.assertTrue(len(warning_list), 3)
