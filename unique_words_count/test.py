import unittest
import solution


class unique_words_countTest(unittest.TestCase):
    def test_unique_words_count1(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_unique_words_count2(self):
        self.assertEqual(2, solution.unique_words_count(["python", "python", "python", "ruby"]))

    def test_unique_words_count3(self):
        self.assertEqual(1, solution.unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()
