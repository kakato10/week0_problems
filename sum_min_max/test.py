import unittest
import solution


class sum_min_maxTest(unittest.TestCase):
    def test_sum_min_max1(self):
        self.assertEqual(10, solution.sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))

    def test_sum_min_max2(self):
        self.assertEqual(90, solution.sum_of_min_and_max([-10, 5, 10, 100]))

    def test_sum_min_max3(self):
        self.assertEqual(2, solution.sum_of_min_and_max([1]))


if __name__ == '__main__':
    unittest.main()
