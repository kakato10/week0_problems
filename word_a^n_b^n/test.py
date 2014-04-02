import unittest
import solution


class IsAnBnTest(unittest.TestCase):
    def test_is_an_bn1(self):
        self.assertTrue(solution.is_an_bn(""))

    def test_is_an_bn2(self):
        self.assertTrue(not solution.is_an_bn("rado"))

    def test_is_an_bn3(self):
        self.assertTrue(not solution.is_an_bn("aaabb"))

    def test_is_an_bn4(self):
        self.assertTrue(solution.is_an_bn("aaabbb"))

    def test_is_an_bn5(self):
        self.assertTrue(not solution.is_an_bn("aabbaabb"))

    def test_is_an_bn6(self):
        self.assertTrue(not solution.is_an_bn("aaabbbb"))

    def test_is_an_bn7(self):
        self.assertTrue(solution.is_an_bn("aaaaabbbbb"))

    def test_is_an_bn8(self):
        self.assertTrue(not solution.is_an_bn("abab"))


if __name__ == '__main__':
    unittest.main()
