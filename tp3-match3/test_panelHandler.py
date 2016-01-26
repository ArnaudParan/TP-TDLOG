#!/usr/bin/python3.4
#-*-coding:utf-8-*

from panelHandler import*
import unittest

class panel_testCase(unittest.TestCase):
    def setUp(self):
        self.linesNb = 10
        self.colNb = 20
        self.panel = PanelHandler(self.linesNb, self.colNb,)
        self.init_panel()

    def init_panel(self):
        self.lOrigCol = 1
        self.cOrigLine = 2
        self.lEndCol = self.lOrigCol + 5
        self.cEndLine = self.cOrigLine + 3
        self.valBorder = 1
        self.valInner = 0
        self.init_line(self.lOrigCol, self.lEndCol, self.cOrigLine, self.cEndLine)
        self.init_col(self.lOrigCol, self.lEndCol, self.cOrigLine, self.cEndLine)

    def init_line(self, lOrigCol, lEndCol, cOrigLine, cEndLine):
        panel = self.panel.jewelsPanel
        for col in range(lOrigCol, lEndCol):
            panel[cOrigLine][col] = self.valInner
        panel[cOrigLine][lOrigCol - 1] = self.valBorder
        panel[cEndLine][lOrigCol] = self.valBorder

    def init_col(self, lOrigCol, lEndCol, cOrigLine, cEndLine):
        panel = self.panel.jewelsPanel
        for line in range(cOrigLine, cEndLine):
            panel[line][lOrigCol] = self.valInner
        panel[cOrigLine - 1][lOrigCol] = self.valBorder
        panel[cOrigLine][lEndCol] = self.valBorder

    def test_init_game_panel(self):
        linesNb = len(self.panel.jewelsPanel)
        colNb = len(self.panel.jewelsPanel[0])
        self.assertEqual(linesNb, self.linesNb)
        self.assertEqual(colNb, self.colNb)

    def test_swap_panel_cells(self):
        lineSwapIn = self.cOrigLine
        colSwapIn = self.lOrigCol
        lineSwapBorder = lineSwapIn - 1
        colSwapBorder = colSwapIn
        self.panel.swap_panel_cells(lineSwapIn, colSwapIn, lineSwapBorder, colSwapBorder)

        innerCellAfter = self.panel.jewelsPanel[lineSwapIn][colSwapIn]
        innerCellBefore = self.valInner
        borderCellAfter = self.panel.jewelsPanel[lineSwapBorder][colSwapBorder]
        borderCellBefore = self.valBorder

        self.assertEqual(innerCellBefore, borderCellAfter)
        self.assertEqual(innerCellAfter, borderCellBefore)

    def test_get_line_orig(self):
        lineOrig = self.panel.get_line_orig(self.cOrigLine, self.lOrigCol)
        self.assertEqual(lineOrig, self.lOrigCol)

    def test_get_line_end(self):
        lineEnd = self.panel.get_line_end(self.cOrigLine, self.lOrigCol)
        self.assertEqual(lineEnd, self.lEndCol - 1)

    def test_get_col_orig(self):
        colOrig = self.panel.get_col_orig(self.cOrigLine, self.lOrigCol)
        self.assertEqual(colOrig, self.cOrigLine)

    def test_get_col_end(self):
        colEnd = self.panel.get_col_end(self.cOrigLine, self.lOrigCol)
        self.assertEqual(colEnd, self.cEndLine - 1)

if __name__ == "__main__" :
    unittest.main()
