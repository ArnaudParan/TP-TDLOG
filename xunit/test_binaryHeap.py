#!/usr/bin/python3

from binaryHeap import*
import unittest

class BinaryHeap_testCase(unittest.TestCase):
    def test_insert(self):
        increasingTab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        decreasingTab = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        mixedTab = [5, 2, 7, 1, 3, 6, 8, 0, 4, 9, 10]
        heap1 = heap_from_tab(increasingTab)
        heap2 = heap_from_tab(decreasingTab)
        heap3 = heap_from_tab(mixedTab)

        self.assertTrue(is_binary_heap(heap1))
        self.assertTrue(is_binary_heap(heap2))
        self.assertTrue(is_binary_heap(heap3))

    def test_heap_from_file(self):
        fileHandler = MockFileHandler()
        heap = heap_from_file(fileHandler)
        self.assertTrue(is_binary_heap(heap))
        self.assertEqual(heap.tabVals[0], [10, "message 10"])

class MockFileHandler:
    def __init__(self):
        self.lines = [[0, "message 0"],
                [1, "message 1"],
                [2, "message 2"],
                [3, "message 3"],
                [4, "message 4"],
                [5, "message 5"],
                [6, "message 6"],
                [7, "message 7"],
                [8, "message 8"],
                [9, "message 9"],
                [10, "message 10"]]
        self.lineId = 0

    def popLine(self):
        currentId = self.lineId
        if currentId >= len(self.lines):
            return None
        self.lineId += 1
        return self.lines[currentId]

def heap_from_tab(tab):
    heap = BinaryHeap()
    for elem in tab:
        heap.insert((elem, ""))

    return heap

def is_binary_heap(heap):
    tab = heap.tabVals
    bodyEnd = int(len(tab)/2 - 1)

    for i in range(bodyEnd):
        current = tab[i]
        leftSon = tab[2*i + 1]
        rightSon = tab[2*i + 2]
        if not(is_node_ok(current, leftSon, rightSon)):
            return False

    return True

def is_node_ok(current, leftSon, rightSon):
        if current < leftSon:
            return False
        if current < rightSon:
            return False
        else:
            return True

if __name__ == "__main__" :
    unittest.main()
