import unittest
import solution


class list_to_numberTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(123, solution.list_to_number([1, 2, 3]))

    def test2(self):
        self.assertEqual(189321, solution.list_to_number([1, 8, 9, 3, 2, 1]))

    def test3(self):
        self.assertEqual(321, solution.list_to_number([0, 3, 2, 1]))

    def test4(self):
        self.assertEqual(900, solution.list_to_number([9, 0, 0]))


if __name__ == '__main__':
    unittest.main()
