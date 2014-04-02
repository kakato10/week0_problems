import unittest
import solution
import os


class SumIntegersFromFileTest(unittest.TestCase):
    def setUp(self):
        solution.get_me_some_integers(5, "some_integers.txt")

    def test_sum_integers(self):
        sum_integers = 0
        filename = "some_integers.txt"
        file = open(filename, 'r')
        content = file.read()
        file.close()
        for element in content:
            if element != ' ':
                sum_integers = sum_integers + int(element)
        self.assertEqual(sum_integers, solution.main(filename))

    def tearDown(self):
        os.remove("some_integers.txt")

if __name__ == '__main__':
    unittest.main()
