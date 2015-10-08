#!/usr/bin/python3.4
#-*-coding:utf-8-*

import math
from point import*

class Disk:
    def __init__(self, radius, xCent, yCent):
        self.radius = radius
        self.cent = Point(xCent, yCent)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __iadd__(self, translationVect):
        self.translate(translationVect)

    def __add__(self, translationVect):
        sum = self
        sum.translate(translationVect)
        return sum

    def translate(self, translationVect):
        center = self.cent
        center.translate(translationVect)

    def collision_point(self, point):
        gap = self.cent - point
	return gap.norm() <= self.radius
