#!/usr/bin/python3.4
#-*-coding:utf-8-*

from polygon import*

class Triangle(Polygon):
    def __init__(self, point1, point2, point3):
        super(self.__class__, self).__init__([point1, point2, point3])

    def __str__(self):
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]
        return 'Triangle({} ,{}, {})'.format(str(p1), str(p2), str(p3))
