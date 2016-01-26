#!/usr/bin/python3

class BinaryHeap:
    def __init__(self):
        self.tabVals = []

    def insert(self, elem):
        priority = elem[0]
        self.tabVals.append(elem)
        idElem = len(self.tabVals) - 1
        idParent = int(idElem / 2)
        parent = self.tabVals[idParent]
        while idElem != 0 and elem > parent:
            swap(self.tabVals, idElem, idParent)
            idElem = idParent
            idParent = int(idElem / 2)
            parent = self.tabVals[idParent]

def heap_from_file(fileHandler):
    heap = BinaryHeap()
    line = fileHandler.popLine()
    while line is not None:
        heap.insert(line)
        line = fileHandler.popLine()
    return heap

def swap(tab, id1, id2):
    tmp1 = tab[id1]
    tab[id1] = tab[id2]
    tab[id2] = tmp1
