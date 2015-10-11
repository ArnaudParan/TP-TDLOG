#!/usr/bin/python3.4
#-*-coding:utf-8-*

from point import*
from box import*

class Polygon:
    def __init__(self, pointList):
        self.points = pointList
        self.boundingBox = pointlist_circumscribed_box(self.points)

    def __eq__(self, testedEqual):
        return self.points == testedEqual.points

    def perimeter(self):
        perimeter = 0.
        pointsNb = len(self.points)
        for edgeId in range(pointsNb):
            edge = self.edge(edgeId)
            perimeter += edge.norm()
        return perimeter

    def edge(self, edgeId):
        pointsNb = len(self.points)
        if edgeId > pointsNb - 1:
            raise Exception('Edge out of bounds')
        if edgeId == pointsNb - 1:
            nextPoint = self.points[0]
            currentPoint = self.points[pointsNb - 1]
        else:
            nextPoint = self.points[edgeId + 1]
            currentPoint = self.points[edgeId]
        edge = nextPoint - currentPoint
        return edge

    def translate(self, transVect):
        for point in self.points:
            point += transVect
        self.boundingBox += transVect

    def collision(self, collisionPoint):
        boxCollision = self.boundingBox.collision(collisionPoint)
        if not boxCollision:
            return False
        #TODO do the collision inside the box

    def __str__(self):
        toString = 'Polygon('
        nbPoints = len(self.points)
        for pointId in range(nbPoints - 1):
            point = self.points[pointId]
            toString += str(point) + ', '
        point = self.points[nbPoints - 1]
        toString += str(point)
        toString += ')'
        return toString
