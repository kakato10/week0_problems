import unittest
import solution


class FibonacciListTest(unittest.TestCase):

    def test_fib_list1(self):
        self.assertEqual([1], solution.nth_fib_lists([1], [2], 1))

    def test_fib_list2(self):
        self.assertEqual([2], solution.nth_fib_lists([1], [2], 2))

    def test_fib_list3(self):
        self.assertEqual([1, 2, 1, 3],\
            solution.nth_fib_lists([1, 2], [1, 3], 3))

    def test_fib_list4(self):
        self.assertEqual([1, 2, 3, 1, 2, 3],\
            solution.nth_fib_lists([], [1, 2, 3], 4))

    def test_fib_list5(self):
        self.assertEqual([], solution.nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()
