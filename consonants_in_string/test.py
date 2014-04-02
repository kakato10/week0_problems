import unittest
import solution

class consonantsTest(unittest.TestCase):
	"""docstring for consonantsTest"""
	def test_consonants_1(self):
		self.assertEqual(8, solution.count_consonants('lqlqlqlq!....'))
	def test_consonants_2(self):
		self.assertEqual(4, solution.count_consonants('lialialialia!....'))
	def test_consonants_3(self):
		self.assertEqual(44, solution.count_consonants('Github is the second best thing that happend to programmers, after the keyboard!'))
	def test_consonants_4(self):
		self.assertEqual(12, solution.count_consonants('Where the fuck are you going!'))

if __name__ == '__main__':
	unittest.main()