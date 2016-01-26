#!/usr/bin/python3.4
#-*-coding:utf-8-*

import unittest
from scoreCounter import*

class ScoreCounter_testCase(unittest.TestCase):
    def setUp(self):
        self.counter = ScoreCounter()

if __name__ == "__main__" :
    unittest.main()
