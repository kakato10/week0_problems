import unittest
import solution


class mealTest(unittest.TestCase):
	def test_for_spam(self):
		self.assertEqual("spam ", solution.prepare_meal(3))
	def test_for_eggs(self):
		self.assertEqual("eggs", solution.prepare_meal(5))
	def test_for_and(self):
		self.assertEqual("spam and eggs", solution.prepare_meal(15))
	def test_for_more_spam(self):
		self.assertEqual("spam spam spam ", solution.prepare_meal(27))
	def test_for_more_spam_plus_eggs(self):
		self.assertEqual("spam spam and eggs", solution.prepare_meal(45))
	def test_for_staying_hungry(self):
		self.assertEqual("", solution.prepare_meal(7))


if __name__ == '__main__':
	unittest.main()

	