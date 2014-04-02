import unittest
import solution


class increasing_seqTest(unittest.TestCase):

    def test_increasing_seq1(self):
        self.assertTrue(solution.is_increasing([1, 2, 3, 4, 5]))

    def test_increasing_seq2(self):
        self.assertTrue(solution.is_increasing([3]))

    def test_increasing_seq3(self):
        self.assertTrue(not solution.is_increasing([3, 1, 4, 79]))

    def test_increasing_seq4(self):
        self.assertTrue(not solution.is_increasing([2, 2, 2, 2]))

if __name__ == '__main__':
    unittest.main()
