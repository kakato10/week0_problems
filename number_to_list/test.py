import unittest
import solution


class number_to_listTest(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 2, 3], solution.number_to_list(123))

    def test2(self):
        self.assertEqual([1, 4, 2, 5, 7], solution.number_to_list(14257))

    def test3(self):
        self.assertEqual([9, 0, 1, 3, 5, 0], solution.number_to_list(901350))


if __name__ == '__main__':
    unittest.main()
