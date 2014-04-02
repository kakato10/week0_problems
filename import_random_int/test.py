import solution
import unittest
import os


class ImportRandomIntTest(unittest.TestCase):
    def test_importing_random_int(self):
        numbers = []
        for i in range(1, 101):
            numbers.append(i)
        solution.main(5, 'my_numbers.txt')
        file = open('my_numbers.txt', 'r')
        content = file.read()
        content = content.split('\n')
        numbers_from_file = list(content)
        int_numbers = []
        for element in content:
            if element != '':
                int_numbers.append(int(element))
        for element in int_numbers:
            self.assertTrue(element in numbers)
        file.close()

    def tearDown(self):
        os.remove('my_numbers.txt')

if __name__ == '__main__':
    unittest.main()
