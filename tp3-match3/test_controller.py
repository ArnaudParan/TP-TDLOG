#!/usr/bin/python3.4
#-*-coding:utf-8-*

from controller import*
import unittest

class controller_testCase(unittest.TestCase):
    def setUp(self):
        self.nbX = 10
        self.nbY = 20
        self.controller = Controller(None, self.nbX, self.nbY)

    def test_is_in_game(self):
        inX = 0
        inY = 0
        outX = self.nbX + 1
        outY = 0
        inIsin = self.controller.is_in_game_table(inX, inY)
        outIsin = self.controller.is_in_game_table(outX, outY)

        self.assertTrue(inIsin)
        self.assertFalse(outIsin)

    def test_are_permutable(self):
        startX = 0
        startY = 0
        permX = 1
        permY = 0
        npermX = 1
        npermY = 1
        permIsPermutable = self.controller.are_permutable(
                startX,
                startY,
                permX,
                permY)
        npermIsPermutable = self.controller.are_permutable(
                startX,
                startY,
                npermX,
                npermY)

        self.assertTrue(permIsPermutable)
        self.assertFalse(npermIsPermutable)

if __name__ == "__main__" :
    unittest.main()
