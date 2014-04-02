import unittest
import os


class ConcatFilesTest(unittest.TestCase):
    def setUp(self):
        file1 = open("some_text1.txt", 'w')
        file1.write("okay")
        file1.close()
        file2 = open("some_text2.txt", 'w')
        file2.write("new")
        file2.close()
        file3 = open('some_text3.txt', 'w')
        file3.write("awesome")
        file3.close()

    def test_concat_two_files(self):
        os.system("python3 ./concat_files/solution.py some_text1.txt some_text2.txt")
        file = open("MEGATRON.txt", 'r')
        content = file.read()
        content_to_check = 'okay\nnew'
        file.close()
        self.assertEqual(content_to_check, content)

    def test_concat_three_files_into_existing_file(self):
        os.system("python3 ./concat_files/solution.py some_text1.txt some_text2.txt")
        os.system("python3 ./concat_files/solution.py some_text3.txt some_text1.txt some_text2.txt")
        file = open("MEGATRON.txt", 'r')
        content = file.read()
        content_to_check = 'okay\nnew\nawesome\nokay\nnew'
        file.close()
        self.assertEqual(content_to_check, content)

    def test_add_one_file_content_to_existing_file(self):
        os.system("python3 ./concat_files/solution.py some_text1.txt some_text2.txt")
        os.system("python3 ./concat_files/solution.py some_text3.txt")
        file = open("MEGATRON.txt", 'r')
        content = file.read()
        file.close()
        content_to_check = 'okay\nnew\nawesome'
        self.assertEqual(content_to_check, content)

    def tearDown(self):
        os.remove('some_text1.txt')
        os.remove('some_text3.txt')
        os.remove('some_text2.txt')
        os.remove("MEGATRON.txt")

if __name__ == '__main__':
    unittest.main()
