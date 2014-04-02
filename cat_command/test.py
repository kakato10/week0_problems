import unittest
import solution
import os


class CatCommandTest(unittest.TestCase):
    def setUp(self):
        filename = 'some_text.txt'
        file = open(filename, 'w')
        content = 'This is just a little bit of text.'
        file.write("".join(content))
        file.close()

    def test_cat_command(self):
        name = "some_text.txt"
        self.assertEqual("This is just a little bit of text.", solution.main(name))

    def tearDown(self):
        os.remove('some_text.txt')

if __name__ == '__main__':
    unittest.main()
