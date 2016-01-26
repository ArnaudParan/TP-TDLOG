#!/usr/bin/python3.4
#-*-coding:utf-8-*

from model import*

class Controller:
    def __init__(self, model, nbX, nbY):
        self.model = model
        self.nbX = nbX
        self.nbY = nbY

    def request_move(self, currentX, currentY, futureX, futureY):
        currentInTable = is_in_game_table(currentX, currentY)
        futureInTable = is_in_game_table(futureX, futureY)
        currFuturePermutable = are_permutable(currentX, currentY, futureX, futureY)

    def is_in_game_table(self, pointX, pointY):
        xIsIn = (0 <= pointX) and (pointX < self.nbX)
        yIsIn = (0 <= pointY) and (pointY < self.nbY)
        return xIsIn and yIsIn

    def are_permutable(self, currentX, currentY, futureX, futureY):
        isTop = (futureX == currentX) and (futureY == currentY + 1)
        isBottom = (futureX == currentX) and (futureY == currentY - 1)
        isLeft = (futureX == currentX - 1) and (futureY == currentY)
        isRight = (futureX == currentX + 1) and (futureY == currentY)
        return isTop or isBottom or isLeft or isRight
