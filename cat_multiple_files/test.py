import unittest
import solution
import os


class CatCommandTest(unittest.TestCase):
    def setUp(self):
        filename1 = 'some_text.txt'
        file = open(filename1, 'w')
        content = 'This is just a little bit of text.'
        file.write("".join(content))
        file.close()

        filename2 = 'and_some_more_text.txt'
        content2 = 'Are you ready to rock?'
        file2 = open(filename2, 'w')
        file2.write("".join(content2))
        file2.close()

    def test_cat_command(self):
        name1 = "some_text.txt"
        name2 = 'and_some_more_text.txt'
        self.assertEqual("This is just a little bit of text.\n\nAre you ready to rock?", solution.main(name1, name2))

    def tearDown(self):
        os.remove('some_text.txt')
        os.remove('and_some_more_text.txt')

if __name__ == '__main__':
    unittest.main()
