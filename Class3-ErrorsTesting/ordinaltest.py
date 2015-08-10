import unittest
import ordinal

class Ordinaltest(unittest.TestCase):

	def test_first(self):
		self.assertEqual("11th", ordinal.Ordinal(11))

	def test_second(self):
		self.assertEqual("12th", ordinal.Ordinal(12))
	
	def test_third(self):
		self.assertEqual("13th", ordinal.Ordinal(13))

if __name__ == "__main__":
	unittest.main()