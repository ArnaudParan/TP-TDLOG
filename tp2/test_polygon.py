#!/usr/bin/python3.4
#-*-coding:utf-8-*

from polygon import*
import unittest

class polygon_testCase(unittest.TestCase):
    def setUp(self):
        p1 = Point(0., 0.)
        p2 = Point(2., 0.)
        p3 = Point(0., 1.)
        p4 = Point(3., 3.)
        p5 = Point(1., 1.)
        self.pointList = [p1, p2, p3, p4, p5]
        self.poly = Polygon(self.pointList)

    def test_eq(self):
        eqPoly = copy.copy(self.poly)
        ieqPoly = Polygon([Point(1., 1.), Point(0., 0.)])
        self.assertEqual(eqPoly, self.poly)
        self.assertNotEqual(ieqPoly, self.poly)

    def test_perimeter(self):
        perimeter = 1.
        testPoly = Polygon([Point(0.,0.), Point(0., perimeter / 2.)])
        self.assertEqual(testPoly.perimeter(), perimeter)

    def test_translate(self):
        transVect = Point(1., 2.)
        for point in self.pointList:
            point += transVect
        translated = Polygon(self.pointList)
        self.assertEqual(translated, self.poly)

if __name__ == "__main__" :
    unittest.main()
