#!/usr/bin/env python
#
#  Copyright (c) 2011, Sean Reifschneider, tummy.com, ltd.
#  All Rights Reserved.

def movingaverage(data, sample_size):
	'''Return the moving averages of the data, with a window size of
	`sample_size`.  `sample_size` must be an integer greater than 0.'''
	if sample_size < 1:
		raise ValueError('Sample_size must be 1 or larger')

	return [ sum(data[x - sample_size:x]) / sample_size
			for x in range(sample_size, len(data) + 1) ]


if __name__ == '__main__':
	import unittest

	class TestMovingAverage(unittest.TestCase):
		def test_Basic(self):
			with self.assertRaises(ValueError):
				movingaverage([1,2,3], 0)
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 1)), [1,2,3,4,5,6])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 2)), [1,2,3,4,5])
			self.assertEqual(list(movingaverage(map(float, [1,2,3,4,5,6]), 2)),
					[1.5,2.5,3.5,4.5,5.5])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 3)), [2,3,4,5])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 4)), [2,3,4])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 5)), [3,4])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 6)), [3])
			self.assertEqual(list(movingaverage([1,2,3,4,5,6], 7)), [])

	suite = unittest.TestLoader().loadTestsFromTestCase(TestMovingAverage)
	unittest.TextTestRunner(verbosity = 2).run(suite)
