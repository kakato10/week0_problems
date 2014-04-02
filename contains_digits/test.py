import unittest
import solution


class contains_digitsTest(unittest.TestCase):

    def test_contains_digits1(self):
        self.assertEqual(True, solution.contains_digits(432, [3, 2]))

    def test_contains_digits2(self):
        self.assertEqual(False, solution.contains_digits(8213, [2, 4]))

    def test_contains_digits3(self):
        self.assertEqual(False, solution.contains_digits(82743, [9, 1]))

    def test_contains_digits4(self):
        self.assertEqual(True, solution.contains_digits(9213, []))


if __name__ == '__main__':
    unittest.main()
