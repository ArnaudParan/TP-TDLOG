#!/usr/bin/python3.4
#-*-coding:utf-8-*

from disk import*
import math
import unittest

class disk_testCase(unittest.TestCase) :
	def test_init(self):
		radius = 10.
		xCenter = 1.
		yCenter = 2.
		testDisk = Disk(radius, xCenter, yCenter)
		self.assertEqual(testDisk.radius, radius)
		self.assertEqual(testDisk.xCenter, xCenter)
		self.assertEqual(testDisk.yCenter, yCenter)

if __name__ == "__main__" :
	unittest.main()
