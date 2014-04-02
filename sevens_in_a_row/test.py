import unittest
import solution

class sevens_in_a_rowTest(unittest.TestCase):
	def test_sevens_in_a_row1(self):
		self.assertEqual(True, solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
	
	def test_sevens_in_a_row2(self):
		self.assertEqual(False, solution.sevens_in_a_row([1,7,1,7,7], 4))
		
	def test_sevens_in_a_row3(self):
		self.assertEqual(True, solution.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
		
	def test_sevens_in_a_row4(self):
		self.assertEqual(True, solution.sevens_in_a_row([7,2,1,6,2], 1))
		
	def test_sevens_in_a_row5(self):
		self.assertEqual(True, solution.sevens_in_a_row([7,7,7,3,7,7,7,7,7], 4))

if __name__ == '__main__':
	unittest.main()
		