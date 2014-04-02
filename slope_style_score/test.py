import unittest
import solution


class SlopeStyleTest(unittest.TestCase):
    """docstring for SlopeStyleTest"""
    def test_slope_style1(self):
        self.assertEqual("%.2f" % round(50), solution.slope_style_score([10, 40, 50, 60, 100]))

    def test_slope_style_two_highest_scores(self):
        self.assertEqual("%.2f" % round(80), solution.slope_style_score([10, 60, 80, 100, 100]))

    def test_slope_style_two_loweset_scores(self):
        self.assertEqual("%.2f" % round(60), solution.slope_style_score([30, 30, 80, 70, 100]))

    def test_slope_style_two_highest_and_lowest_scores(self):
        self.assertEqual("%.2f" % round(70), solution.slope_style_score([50, 50, 60, 100, 100]))


if __name__ == '__main__':
    unittest.main()
