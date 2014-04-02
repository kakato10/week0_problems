import unittest
import solution


class biggest_differenceTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(-3, solution.biggest_difference([0, 1, 2, 3]))

    def test2(self):
        self.assertEqual(-21, solution.biggest_difference([22, 1, 11, 20, 13]))

    def test3(self):
        self.assertEqual(-99, solution.biggest_difference(range(100)))


if __name__ == '__main__':
    unittest.main()
