#!/usr/bin/python3.4
#-*-coding:utf-8-*

from point import*
import math
import unittest

class point_testCase(unittest.TestCase) :
	def test_init(self) :
		absc = 10.
		ord = 20.
		testPoint = Point(absc, ord)

		self.assertEqual(testPoint.absc, absc)
		self.assertEqual(testPoint.ord, ord)

	def test_neg(self):
		absc = 10.
		ord = 20.
		testPoint = Point(absc, ord)
		negPoint = - testPoint

		self.assertEqual(negPoint.absc, -absc)
		self.assertEqual(negPoint.ord, -ord)
		self.assertEqual(testPoint.absc, absc)
		self.assertEqual(testPoint.ord, ord)

	def test_substract(self):
		abscM = 10.
		ordM = 20.
		abscS = 40.
		ordS = 30.

		minuend = Point(abscM, ordM)
		subtrahend = Point(abscS, ordS)
		diff = minuend - subtrahend

		self.assertEqual(diff.absc, abscM - abscS)
		self.assertEqual(diff.ord, ordM - ordS)
		self.assertEqual(minuend.absc, abscM)
		self.assertEqual(minuend.ord, ordM)

	def test_iadd(self):
		abscSummed = 10.
		ordSummed = 20.
		abscSummand = 40.
		ordSummand = 30.

		summed = Point(abscSummed, ordSummed)
		summand = Point(abscSummand, ordSummand)
		summed += summand

		self.assertEqual(summed.absc, abscSummed + abscSummand)
		self.assertEqual(summed.ord, ordSummed + ordSummand)

	def test_add(self):
		abscSummed = 10.
		ordSummed = 20.
		abscSummand = 40.
		ordSummand = 30.

		summed = Point(abscSummed, ordSummed)
		summand = Point(abscSummand, ordSummand)
		sum = summed + summand

		self.assertEqual(sum.absc, abscSummed + abscSummand)
		self.assertEqual(sum.ord, ordSummed + ordSummand)
		self.assertEqual(summed.absc, abscSummed)
		self.assertEqual(summed.ord, ordSummed)

	def test_translate(self):
		abscTranslated = 10.
		ordTranslated = 20.
		abscTranslation = 40.
		ordTranslation = 30.

		translated = Point(abscTranslated, ordTranslated)
		translation = Point(abscTranslation, ordTranslation)
		translated.translate(translation)

		self.assertEqual(translated.absc, abscTranslated + abscTranslation)
		self.assertEqual(translated.ord, ordTranslated + ordTranslation)

	def test_norm(self):
		absc = 1.
		ord = absc
		testPoint = Point(absc, ord)

		self.assertEqual(testPoint.norm(), absc * math.sqrt(2))

	def test_str(self):
		absc = 10.
		ord = 20.
		testPoint = Point(absc, ord)

		self.assertEqual(str(testPoint), "(" + str(absc) + ", " + str(ord) + ")")

	def test_eq(self):
		absc1 = 10.
		ord1 = 20.
		absc2 = 40.
		ord2 = 30.

		eqPoint1 = Point(absc1, ord1)
		eqPoint2 = Point(absc1, ord1)
		ineqPoint = Point(absc2, ord2)

		#self.assertEqual(eqPoint1, eqPoint2)
		self.assertEqual(eqPoint1, eqPoint2)
		self.assertFalse(eqPoint1 == ineqPoint)

if __name__ == "__main__" :
	unittest.main()
