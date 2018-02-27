import unittest
import warnings

from main import a, b, c


class TestMain(unittest.TestCase):

    def test_a(self):
        with warnings.catch_warnings(record=True) as warning_list:
            a()

            self.assertTrue(len(warning_list), 1)

    def test_b(self):
        with warnings.catch_warnings(record=True) as warning_list:
            b()

            self.assertTrue(len(warning_list), 1)

    def test_c(self):
        with warnings.catch_warnings(record=True) as warning_list:
            c()

            self.assertTrue(len(warning_list), 1)

    def test_all_three(self):
        with warnings.catch_warnings(record=True) as warning_list:
            a()
            b()
            c()

            self.assertTrue(len(warning_list), 3)
