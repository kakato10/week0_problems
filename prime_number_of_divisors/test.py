import unittest
import solution


class prime_number_of_divisorsTest(unittest.TestCase):
    def test_prime_number_of_divisors1(self):
        self.assertEqual(False, solution.prime_number_of_divisors(1))

    def test_prime_number_of_divisors2(self):
        self.assertEqual(True, solution.prime_number_of_divisors(4))

    def test_prime_number_of_divisors3(self):
        self.assertEqual(False, solution.prime_number_of_divisors(8))

    def test_prime_number_of_divisors4(self):
        self.assertEqual(False, solution.prime_number_of_divisors(10))


if __name__ == '__main__':
    unittest.main()
