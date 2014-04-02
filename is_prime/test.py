import unittest
import solution


class is_primeTest(unittest.TestCase):
    def test_is_prime1(self):
        self.assertEqual(False, solution.is_prime(1))

    def test_is_prime2(self):
        self.assertEqual(True, solution.is_prime(7))

    def test_is_prime3(self):
        self.assertEqual(False, solution.is_prime(1000))

    def test_is_prime4(self):
        self.assertEqual(True, solution.is_prime(2))

    def test_is_prime5(self):
        self.assertEqual(False, solution.is_prime(4))

    def test_is_prime6(self):
        self.assertEqual(False, solution.is_prime(0))


if __name__ == '__main__':
    unittest.main()
