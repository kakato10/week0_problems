import unittest
import solution


class what_is_my_signTest(unittest.TestCase):
	def test_what_is_my_sign1(self):
		self.assertEqual("Aries", solution.what_is_my_sign(24,3))

	def test_what_is_my_sign2(self):
		self.assertEqual('Cancer', solution.what_is_my_sign(22,7))

	def test_what_is_my_sign3(self):
		self.assertEqual('Virgo', solution.what_is_my_sign(15,9))

	def test_what_is_my_sign4(self):
		self.assertEqual('Sagittarius', solution.what_is_my_sign(1,12))

	def test_what_is_my_sign5(self):
		self.assertEqual('Capricorn', solution.what_is_my_sign(31,12))

if __name__ == '__main__':
	unittest.main()