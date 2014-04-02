import unittest
import solution


class MemberFibonacciListTest(unittest.TestCase):

    def test_for_member1(self):
        self.assertTrue(not solution.member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

    def test_for_member2(self):
        self.assertTrue(solution.member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))

    def test_for_member3(self):
        self.assertTrue(solution.member_of_nth_fib_lists([7, 11],\
            [2], [7, 11, 2, 2, 7, 11, 2]))

    def test_for_member4(self):
        self.assertTrue(not solution.member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    unittest.main()
