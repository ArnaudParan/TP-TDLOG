#!/usr/bin/python3.4
#-*-coding:utf-8-*

import math
from point import*

class Disk:
    def __init__(self, radius, xCent, yCent):
        if radius <= 0:
            raise Exception('Negative radius in Disk')
        self.radius = radius
        self.cent = Point(xCent, yCent)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __iadd__(self, translationVect):
        self.translate(translationVect)
        return self

    def __add__(self, translationVect):
        sum = copy.copy(self)
        sum.translate(translationVect)
        return sum

    def translate(self, translationVect):
        center = self.cent
        center.translate(translationVect)

    def collision_point(self, point):
        gap = self.cent - point
        return (gap.norm() <= self.radius)

    def __eq__(self, testedEqual):
        return (self.radius == testedEqual.radius) and (self.cent == testedEqual.cent)

    def __str__(self):
        return 'Disk({}, {})'.format(self.radius, str(self.cent))
