#!/usr/bin/python3.4
#-*-coding:utf-8-*

from box import*
import unittest

class box_testCase(unittest.TestCase):
    def setUp(self):
        self.xmin = 0.
        self.xmax = 1.
        self.ymin = 0.
        self.ymax = 1.
        self.box = Box(self.xmin, self.xmax, self.ymin, self.ymax)

    def test_init_exception(self):
        with self.assertRaises(Exception):
            Box(4, 3, 1, 2)
        with self.assertRaises(Exception):
            Box(3, 4, 2, 1)

    def test_translate(self):
        xtrans = 2.
        ytrans = 3.
        transVect = Point(xtrans, ytrans )
        self.box.translate(transVect)
        transV1 = self.xmin + xtrans
        transV2 = self.xmax + xtrans
        transV3 = self.ymin + ytrans
        transV4 = self.ymax + ytrans
        translatedBox = Box(transV1, transV2, transV3, transV4)
        self.assertEqual(self.box, translatedBox)

    def test_eq(self):
        eqBox = Box(self.xmin, self.xmax, self.ymin, self.ymax)
        self.xmin += 1.
        ieqBox = Box(self.xmin, self.xmax, self.ymin, self.ymax)
        self.assertEqual(self.box, eqBox)
        self.assertNotEqual(self.box, ieqBox)

    def test_collision_point(self):
        xmid = (self.xmax + self.xmin) / 2.
        ymid = (self.ymax + self.ymin) / 2.

        pointIn = Point(xmid, ymid)
        pointBorder = Point(self.xmax, self.ymin)
        pointOut = Point(self.xmax + 1., self.ymin)

        collisionIn = self.box.collision(pointIn)
        collisionBorder = self.box.collision(pointBorder)
        collisionOut = self.box.collision(pointOut)

        self.assertTrue(collisionIn)
        self.assertTrue(collisionBorder)
        self.assertFalse(collisionOut)

    def test_MIN(self):
        self.assertEqual(MIN(2, 3), 2)

    def test_MAX(self):
        self.assertEqual(MAX(2, 3), 3)

    def test_pointlist_circumscribed_box(self):
        point1 = Point(self.xmin, self.ymin)
        point2 = Point(self.xmax, self.ymax)
        list = [point1, point2]
        self.assertEqual(pointlist_circumscribed_box(list), self.box)

if __name__ == "__main__" :
    unittest.main()
