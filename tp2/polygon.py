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
            perimeter += self.edge_length(edgeId)
        return perimeter

    def edge_length(self, edgeId):
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
        return edge.norm()

    def translate(self, transVect):
        for point in self.points:
            point += transVect
        self.boundingBox += transVect

    def collision(self, collisionPoint):
        boxCollision = self.boundingBox.collision(collisionPoint)
        if not boxCollision:
            return False
