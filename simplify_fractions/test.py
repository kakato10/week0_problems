import unittest
import solution


class SimplifyFractionsTest(unittest.TestCase):
    def test_simplifying_fraction1(self):
        self.assertEqual((1, 3), solution.simplify_fraction((3, 9)))

    def test_simplifying_fraction2(self):
        self.assertEqual((0, 3), solution.simplify_fraction((0, 3)))

    def test_simplifying_fraction3(self):
        self.assertEqual((1, 2), solution.simplify_fraction((2, 4)))

    def test_simplifying_fraction4(self):
        self.assertEqual((2, 7), solution.simplify_fraction((2, 7)))

    def test_simplifying_fraction5(self):
        self.assertEqual((1, 1), solution.simplify_fraction((3, 3)))

if __name__ == '__main__':
    unittest.main()
