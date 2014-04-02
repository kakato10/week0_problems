import unittest
import solution


class decreasing_seqTest(unittest.TestCase):

    def test_decreasing_seq1(self):
        self.assertTrue(not solution.is_decreasing([1, 2, 3, 4, 5]))

    def test_decreasing_seq2(self):
        self.assertTrue(solution.is_decreasing([3]))

    def test_decreasing_seq3(self):
        self.assertTrue(not solution.is_decreasing([3, 1, 4, 79]))

    def test_decreasing_seq4(self):
        self.assertTrue(not solution.is_decreasing([2, 2, 2, 2]))

    def test_decreasing_seq5(self):
        self.assertTrue(solution.is_decreasing([89, 5, 4, 3, 2, 1, 0]))


if __name__ == '__main__':
    unittest.main()
