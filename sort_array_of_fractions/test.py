import unittest
import solution


class SortFractionsTest(unittest.TestCase):

    def test_sorting_fractions1(self):
        self.assertEqual([(1, 2), (2, 3)], solution.sort_fractions([(2, 3), (1, 2)]))

    def test_sorting_fractions2(self):
        self.assertEqual([(1, 3), (1, 2), (2, 3)],\
            solution.sort_fractions([(2, 3), (1, 2), (1, 3)]))

    def test_sorting_fractions3(self):
        self.assertEqual([(0, 3), (1, 2), (5, 3), (10, 2)],\
            solution.sort_fractions([(1, 2), (5, 3), (0, 3), (10, 2)]))


if __name__ == '__main__':
    unittest.main()
