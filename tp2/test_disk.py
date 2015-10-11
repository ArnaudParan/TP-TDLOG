#!/usr/bin/python3.4
#-*-coding:utf-8-*

from disk import*
import math
import unittest

class disk_testCase(unittest.TestCase) :
    def setUp(self):
        self.radius = 10.
        xCenter = 1.
        yCenter = 2.
        self.cent = Point(xCenter, yCenter)
        self.testDisk = Disk(self.radius, xCenter, yCenter)

        transx = 5.
        transy = 9.
        self.translationVect = Point(transx, transy)

    def test_init(self):
        diskRadius = self.testDisk.radius
        diskCent = self.testDisk.cent

        self.assertEqual(diskRadius, self.radius)
        self.assertEqual(diskCent, self.cent)

    def test_init_neg_radius_exception(self):
        with self.assertRaises(Exception):
            Disk(-1., 0., 0.)

    def test_perimeter(self):
        expectedPerim = 2 * math.pi * self.radius
        diskPerim = self.testDisk.perimeter()

        self.assertEqual(diskPerim, expectedPerim)

    def test_iadd(self):
        self.testDisk += self.translationVect
        expectedCenter =  self.cent + self.translationVect

        self.assertEqual(self.testDisk.cent, expectedCenter)

    def test_add(self):
        testTranslated = self.testDisk + self.translationVect
        expectedCenter =  self.cent + self.translationVect

        self.assertEqual(testTranslated.cent, expectedCenter)

    def test_translate(self):
        self.testDisk.translate(self.translationVect)
        expectedCenter =  self.cent + self.translationVect

        self.assertEqual(self.testDisk.cent, expectedCenter)

    def test_collision_point(self):
        innerPoint = self.cent
        borderPoint = self.cent + Point(self.radius, 0.)
        outerPoint = self.cent + Point(self.radius, self.radius)
        innerCollision = self.testDisk.collision_point(innerPoint)
        borderCollision = self.testDisk.collision_point(borderPoint)
        outerCollision = self.testDisk.collision_point(outerPoint)

        self.assertTrue(innerCollision)
        self.assertTrue(borderCollision)
        self.assertFalse(outerCollision)

    def test_eq(self):
        xCent = self.cent.absc
        yCent = self.cent.ord
        eqDisk = Disk(self.radius, xCent, yCent)
        ieqDisk = Disk(self.radius, xCent + 2., yCent)
        self.assertEqual(self.testDisk, eqDisk)
        self.assertNotEqual(self.testDisk, ieqDisk)

if __name__ == "__main__" :
    unittest.main()
