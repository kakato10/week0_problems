import unittest
import solution


class count_vowelsTest(unittest.TestCase):
    def test_count_vowels1(self):
        self.assertEqual(2, solution.count_vowels("Python"))

    def test_count_vowels2(self):
        self.assertEqual(8, solution.count_vowels("Theistareykjarbunga"))

    def test_count_vowels3(self):
        self.assertEqual(0, solution.count_vowels("grrrrgh!"))

    def test_count_vowels4(self):
        self.assertEqual(22, solution.count_vowels\
            ("Github is the second best thing that happend\
                to programmers, after the keyboard!"))

    def test_count_vowels5(self):
        self.assertEqual(8, solution.count_vowels("A nice day to code!"))


if __name__ == '__main__':
    unittest.main()
