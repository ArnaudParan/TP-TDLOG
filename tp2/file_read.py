#!/usr/bin/python3.4
#-*-coding:utf-8-*

from os import chdir

from polygon import*
from disk import*
from triangle import*

def read_collision_file(file):
    line  = file.readline()
    objects = []
    while line != '':
        currentObject = string_to_shape(line)
        objects.append(currentObject)
        line = file.readline()

    nbObjects = len(objects)
    for objId in range(nbObjects - 1):
        currentObject
        point = objects[nbObjects - 1]
        if currentObject.collision(point):
            print(str(point) + ' est dans ' + str(currentObject))

#the description has to be SHAPE_NAME num1 ...
def string_to_shape(stringDescription):
    splittedLine = stringDescription.split()

    if splittedLine[0] == 'DISK':
        return createDisk(splittedLine)

    elif splittedLine[0] == 'POLYGON':
        return createPolygon(splittedLine)

    elif splittedLine[0] == 'TRIANGLE':
        return createTriangle(splittedLine)

def createDisk(splittedLine):
    radius = float(splittedLine[1])
    xCent = float(splittedLine[2])
    yCent = float(splittedLine[3])
    return Disk(radius, xCent, yCent)

def createPolygon(splittedLine):
    nbWords = len(splittedLine)
    points = []
    for pointId in range(nbWords // 2):
        xPoint = float(splittedLine[2 * pointId + 1])
        yPoint = float(splittedLine[2 * pointId + 2])
        points.append(Point(xPoint, yPoint))
    return Polygon(points)

def createTriangle(splittedLine):
    x1 = float(splittedLine[1])
    y1 = float(splittedLine[2])
    x2 = float(splittedLine[3])
    y2 = float(splittedLine[4])
    x3 = float(splittedLine[5])
    y3 = float(splittedLine[6])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    return Triangle(p1, p2, p3)

def createPoint(splittedLine):
    x1 = float(splittedLine[1])
    y1 = float(splittedLine[2])
    return Point(x1, y1)
