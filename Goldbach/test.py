import unittest
import solution


class GoldbachTest(unittest.TestCase):
    def test_goldbach1(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)],\
        solution.goldbach(100))

    def test_goldbach2(self):
        self.assertEqual([(3, 7), (5, 5)], solution.goldbach(10))

    def test_goldbach3(self):
        self.assertEqual([(3, 5)], solution.goldbach(8))

    def test_goldach4(self):
        self.assertEqual([(3, 3)], solution.goldbach(6))

    def test_goldbach5(self):
        self.assertEqual([(2, 2)], solution.goldbach(4))


if __name__ == '__main__':
    unittest.main()
