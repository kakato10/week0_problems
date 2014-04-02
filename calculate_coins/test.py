import unittest
import solution


class calculate_coinsTest(unittest.TestCase):
    def test_calculate_coins1(self):
        self.assertEqual({1: 0, 2: 0, 5: 0, 10: 1, 20: 1, 50: 0, 100: 24}, solution.calculate_coins(24.3))

    def test_calculate_coins2(self):
        self.assertEqual({1: 0, 2: 1, 5: 1, 10: 0, 20: 0, 50: 1, 100: 0}, solution.calculate_coins(0.57))

    def test_calculate_coins3(self):
        self.assertEqual({1: 1, 2: 1, 5: 1, 10: 1, 20: 1, 50: 0, 100: 5}, solution.calculate_coins(5.38))

    def test_calculate_coins4(self):
        self.assertEqual({1: 0, 2: 2, 5: 1, 10: 0, 20: 2, 50: 1, 100: 9}, solution.calculate_coins(9.99))

    def test_calculate_coins5(self):
        self.assertEqual({1: 1, 2: 0, 5: 0, 10: 1, 20: 0, 50: 0, 100: 2}, solution.calculate_coins(2.11))


if __name__ == '__main__':
    unittest.main()
