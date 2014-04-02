import unittest
import solution


class is_number_balancedTest(unittest.TestCase):

    def test_is_number_balanced1(self):
        self.assertEqual(True, solution.is_number_balanced(4352))

    def test_is_number_balanced2(self):
        self.assertEqual(False, solution.is_number_balanced(8213))

    def test_is_number_balanced3(self):
        self.assertEqual(False, solution.is_number_balanced(100))

    def test_is_number_balanced4(self):
        self.assertEqual(True, solution.is_number_balanced(2341))

    def test_is_number_balanced5(self):
        self.assertEqual(True, solution.is_number_balanced(3))


if __name__ == '__main__':
    unittest.main()
