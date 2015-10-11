#!/usr/bin/python3.4
#-*-coding:utf-8-*

from point import*

def MIN(left, right):
    return left if (left < right) else right

def MAX(left, right):
    return left if (left > right) else right

def pointlist_circumscribed_box(pointList):
    if len(pointList) < 1:
        raise Exception('Empty list in box definition')
    xmax = pointList[0].absc
    xmin = pointList[0].absc
    ymax = pointList[0].ord
    ymin = pointList[0].ord
    for point in pointList:
        xmax = MAX(xmax, point.absc)
        xmin = MIN(xmin, point.absc)
        ymax = MAX(ymax, point.ord)
        ymin = MIN(ymin, point.ord)
    return Box(xmin, xmax, ymin, ymax)

class Box:
    def __init__(self, xmin, xmax, ymin, ymax):
        if xmin > xmax or ymin > ymax:
            raise Exception('Wrong box definition')
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


    def translate(self, transVect):
        xtrans = transVect.absc
        ytrans = transVect.ord
        self.xmin += xtrans
        self.xmax += xtrans
        self.ymin += ytrans
        self.ymax += ytrans

    def __eq__(self, testedEqual):
        xeq = self.xmin == testedEqual.xmin
        xeq = xeq and self.xmax == testedEqual.xmax
        yeq = self.ymin == testedEqual.ymin
        yeq = yeq and self.ymax == testedEqual.ymax
        return xeq and yeq

    def collision(self, testedPoint):
        xpoint = testedPoint.absc
        ypoint = testedPoint.ord
        xcollision = self.xmin <= xpoint and xpoint <= self.xmax
        ycollision = self.ymin <= ypoint and ypoint <= self.ymax
        return xcollision and ycollision

    def __iadd__(self, transVect):
        self.translate(transVect)
        return self

    def __add__(self, transVect):
        translated = copy.copy(self)
        translated.translate(transVect)
        return translated
