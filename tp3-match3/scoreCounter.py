#!/usr/bin/python3.4
#-*-coding:utf-8-*

class ScoreCounter:
    def __init__(self):
        self.score = 0
        self.linesNb = 0

    def init_counter(self):
        self.score = 0
        self.linesNb = 0

    def get_score(self):
        return self.score

    def add_lines(self, deletedLines):
        for line in deletedLines:
            length = line[3]
            self.linesNb += 1
            self.score += length + 4 * self.linesNb
