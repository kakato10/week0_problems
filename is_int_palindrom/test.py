import solution
import unittest


class is_int_palindromTest(unittest.TestCase):

    def test_for_palindroms1(self):
        self.assertEqual(True, solution.is_int_palindrom(10001))

    def test_for_palindrom2(self):
        self.assertEqual(False, solution.is_int_palindrom(21))

    def test_for_palindroms3(self):
        self.assertEqual(True, solution.is_int_palindrom(4))

    def test_for_palindroms4(self):
        self.assertEqual(False, solution.is_int_palindrom(123451))

if __name__ == '__main__':
    unittest.main()
