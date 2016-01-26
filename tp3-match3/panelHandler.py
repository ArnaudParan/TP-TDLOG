#!/usr/bin/python3.4
#-*-coding:utf-8-*

class PanelHandler:
    def __init__(self, nbLines, nbCol,):
        self.nbLines = nbLines
        self.nbCol = nbCol
        self.jewelsPanel = []
        self.init_game_panel();
    
    def init_game_panel(self):
        for line in range(self.nbLines):
            currentLine = []
            for col in range(self.nbCol):
                currentLine.append(0)
            self.jewelsPanel.append(currentLine)

    def get_line_orig(self, pointLine, pointCol):
        if pointCol == 0:
            return pointCol
        previousVal = self.jewelsPanel[pointLine][pointCol - 1]
        currentVal = self.jewelsPanel[pointLine][pointCol]
        if previousVal != currentVal:
            return pointCol
        else:
            return self.get_line_orig(pointLine, pointCol - 1)

    def get_line_end(self, pointLine, pointCol):
        if pointCol == self.nbCol:
            return pointCol
        futureVal = self.jewelsPanel[pointLine][pointCol + 1]
        currentVal = self.jewelsPanel[pointLine][pointCol]
        if futureVal != currentVal:
            return pointCol
        else:
            return self.get_line_end(pointLine, pointCol + 1)

    def get_col_orig(self, pointLine, pointCol):
        if pointLine == 0:
            return pointLine
        previousVal = self.jewelsPanel[pointLine - 1][pointCol]
        currentVal = self.jewelsPanel[pointLine][pointCol]
        if previousVal != currentVal:
            return pointLine
        else:
            return self.get_col_orig(pointLine - 1, pointCol)

    def get_col_end(self, pointLine, pointCol):
        if pointLine == self.nbLines:
            return pointLine
        futureVal = self.jewelsPanel[pointLine + 1][pointCol]
        currentVal = self.jewelsPanel[pointLine][pointCol]
        if futureVal != currentVal:
            return pointLine
        else:
            return self.get_col_end(pointLine + 1, pointCol)

    def swap_cells(self, currLine, currCol, futureLine, futureCol):
        self.swap_panel_cells(currLine, currCol, futureLine, futureCol)
        self.notify_permute(currLine, currCol, futureLine, futureCol)

    def swap_panel_cells(self, currLine, currCol, futureLine, futureCol):
        currJewel = self.jewelsPanel[currLine][currCol]
        futureJewel = self.jewelsPanel[futureLine][futureCol]
        self.jewelsPanel[currLine][currCol] = futureJewel
        self.jewelsPanel[futureLine][futureCol] = currJewel

    def __str__(self):
        stringPanel = ''
        for line in range(self.nbLines):
            for col in range(self.nbCol):
                stringPanel += str(self.jewelsPanel[line][col]) + ' '
            stringPanel += '\n'
        return stringPanel
