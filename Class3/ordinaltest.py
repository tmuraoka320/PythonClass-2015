import unittest
import ordinal

class Ordinaltest(unittest.TestCase):

	def test_first(self):
		self.assertEqual("1st", ordinal.Ordinal(1))

	def test_second(self):
		self.assertEqual("2nd", ordinal.Ordinal(2))
	
	def test_third(self):
		self.assertEqual("3rd", ordinal.Ordinal(3))

if __name__ == "__main__":
	unittest.main()