import unittest
import solution


class PrimeFactorizationTest(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual([(2, 1), (5, 1)], solution.prime_factorization(10))
        self.assertEqual([(2, 1), (7, 1)], solution.prime_factorization(14))
        self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))
        self.assertEqual([(89, 1)], solution.prime_factorization(89))
        self.assertEqual([(2, 3), (5, 3)], solution.prime_factorization(1000))
        self.assertEqual([(2, 1), (3, 1), (5, 1)], solution.prime_factorization(30))
        self.assertEqual('Do not try to troll me', solution.prime_factorization(0))
        self.assertEqual('Do not try to troll me', solution.prime_factorization(1))

if __name__ == '__main__':
    unittest.main()
