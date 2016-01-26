#!/usr/bin/python3.4
#-*-coding:utf-8-*

import random
from panelHandler import*
from scoreCounter import*
from enum import Enum

class Model(PanelHandler):
    def __init__(self, nbLines, nbCol, nbColors):
        super(self.__class__, self).__init__(nbLines, nbCol)
        self.nbColors = nbColors
        self.counter = ScoreCounter()
        self.init_panel()

    def init_panel(self):
        for line in range(self.nbLines):
            for col in range(self.nbCol):
                cellVal = random.randint(0, self.nbColors - 1)
                self.jewelsPanel[line][col] = cellVal

    def request_jewel_move(self, currLine, currCol, futureLine, futureCol):
        self.notify_freeze_views()
        self.counter.init_counter()
        self.swap_cells(currLine, currCol, futureLine, futureCol)
        originCells = [(currLine, currCol), (futureLine, futureCol)]
        deletedLines, originCells = delete_connex_lines(originCells)
        self.counter.add_lines(deletedLines)
        if deletedLines == []:
            self.swap_cells(currLine, currCol, futureLine, futureCol)
        while originCells != []:
            deletedLines, originCells = delete_connex_lines(originCells)
            self.counter.add_lines(deletedLines)
        self.score += self.counter.get_score()
        self.notify_unfreeze_views()

    def delete_connex_lines(self, originCells):
        linesToDelete = get_lines_to_delete(originCells)
        if linesToDelete == []:
            return linesToDelete, []
        self.delete_cells(linesToDelete)
        self.delete_cells_view(linesToDelete)
        #TODO add to the deleted lines
        #TODO ask view to translate and create
        self.translate_cells_view(linesToDelete)
        newOrigin = self.get_new_origins(linesToDelete)
        return linesToDelete, newOrigin

    def get_lines_to_delete(self, originPointsList):
        linesToDelete = []
        for originPoint in originPointList:
            pointLine = originPoint[0]
            pointCol = originPoint[1]
            currentLine = self.get_max_deletable_line(pointLine, pointCol)
            if not(currentLine is None):
                linesToDelete.append(currentLine)
        return linesToDelete

    def get_max_deletable_line(self, pointLine, pointCol):
        lOrigLine = self.get_line_orig(pointLine, pointCol)
        lEndLine = self.get_line_end(pointLine, pointCol)
        lLength = lEndLine - lOrigLine

        cOrigCol = self.get_col_orig(pointLine, pointCol)
        cEndCol = self.get_col_end(pointLine, pointCol)
        cLength = cEndCol - cOrigCol
        if cLength >= lLength and lLength >= 3:
            return LineCol.Line, lOrigLine, pointCol, lLength
        elif cLength >= 3:
            return LineCol.Col, pointLine, cOrigCol, cLength

    def __str__(self):
        return str(jewelsPanel)

class LineCol(Enum):
    Line = 0
    Col = 1
