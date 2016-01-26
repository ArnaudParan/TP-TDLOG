#!/usr/bin/python3.4
#-*-coding:utf-8-*

from model import*
import unittest

class model_testCase(unittest.TestCase):
    def setUp(self):
        self.linesNb = 10
        self.colNb = 20
        self.nbColors = 7
        self.model = Model(self.linesNb, self.colNb, self.nbColors)
        self.init_panel()

    def init_panel(self):
        self.lOrigCol = 1
        self.cOrigLine = 2
        self.lLength = 5
        self.cLength = 3
        self.lEndCol = self.lOrigCol + self.lLength
        self.cEndLine = self.cOrigLine + self.cLength
        self.init_line(self.lOrigCol, self.lEndCol, self.cOrigLine, self.cEndLine)
        self.init_col(self.lOrigCol, self.lEndCol, self.cOrigLine, self.cEndLine)

    def init_line(self, lOrigCol, lEndCol, cOrigLine, cEndLine):
        panel = self.model.jewelsPanel
        for col in range(lOrigCol, lEndCol):
            panel[cOrigLine][col] = 0
        panel[cOrigLine][lOrigCol - 1] = 1
        panel[cEndLine][lOrigCol] = 1

    def init_col(self, lOrigCol, lEndCol, cOrigLine, cEndLine):
        panel = self.model.jewelsPanel
        for line in range(cOrigLine, cEndLine):
            panel[line][lOrigCol] = 0
        panel[cOrigLine - 1][lOrigCol] = 1
        panel[cOrigLine][lEndCol] = 1

    def test_get_max_deletable_line(self):
        expectedLine = LineCol.Col, self.cOrigLine, self.lOrigCol, self.lLength
        actualLine = self.model.get_max_deletable_line(self.cOrigLine, self.lOrigCol)
        self.assertEqual(actualLine, expectedLine)

if __name__ == "__main__" :
    unittest.main()
