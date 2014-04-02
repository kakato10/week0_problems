import unittest
import solution


class contains_digitTest(unittest.TestCase):
    def test_contains_digit1(self):
        self.assertEqual(False, solution.contains_digit(341, 2))

    def test_contains_digit2(self):
        self.assertEqual(True, solution.contains_digit(1239, 2))

    def test_contains_digit3(self):
        self.assertEqual(True, solution.contains_digit(103333332, 3))


if __name__ == '__main__':
    unittest.main()
