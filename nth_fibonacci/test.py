import solution
import unittest


class nth_fibonacciTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, solution.nth_fibonacci(2))

    def test_2(self):
        self.assertEqual(55, solution.nth_fibonacci(10))

    def test_3(self):
        self.assertEqual(8, solution.nth_fibonacci(6))


if __name__ == '__main__':
    unittest.main()
