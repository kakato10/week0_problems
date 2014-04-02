import unittest
import solution


class count_wordsTest(unittest.TestCase):
    def test_counting_words1(self):
        self.assertEqual({"apple": 2, "banana": 1, "pie": 1}, solution.count_words(["apple", "banana", "apple", "pie"]))

    def test_counting_words2(self):
        self.assertEqual({"python": 3, "ruby": 1}, solution.count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    unittest.main()
