import solution
import unittest


class sum_digitsTest(unittest.TestCase):
    def test_sum_digits1(self):
        self.assertEqual(6, solution.sum_of_digits(123))

    def test_sum_digits2(self):
        self.assertEqual(8, solution.sum_of_digits(1223))

    def test_sum_digits3(self):
        self.assertEqual(10, solution.sum_of_digits(31123))


if __name__ == '__main__':
    unittest.main()
