import unittest
import solution


class sum_of_divisors_Test(unittest.TestCase):
    def test_sum_of_divisors1(self):
        self.assertEqual(15, solution.sum_of_divisors(8))

    def test_sum_of_divisors2(self):
        self.assertEqual(8, solution.sum_of_divisors(7))

    def test_sum_of_divisors3(self):
        self.assertEqual(1, solution.sum_of_divisors(1))

    def test_sum_of_divisors4(self):
        self.assertEqual(24, solution.sum_of_divisors(15))


if __name__ == '__main__':
    unittest.main()
