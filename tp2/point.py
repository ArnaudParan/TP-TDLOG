#!/usr/bin/python3.4
#-*-coding:utf-8-*

class Point:
    def __init__(self, absc, ord):
        self.absc = absc
        self.ord = ord

    def __neg__(self):
        neg = self
        neg.absc = -neg.absc
        neg.ord = -neg.ord
        return neg

    def __sub__(self, substracted):
        diff = self
        diff.absc -= substracted.absc
        diff.ord -= substracted.ord
        return diff

    def __iadd__(self, translationVectt):
        self.translate(translationVectt)
        return self

    def __add__(self, translationVectt):
        sum = self
        sum.translate(translationVectt)
        return sum

    def translate(self, transVect):
        self.absc += transVect.absc
        self.ord += transVect.ord

    def norm(self):
        return ((self.absc ** 2) + (self.ord ** 2)) ** 0.5

    def __str__(self):
        return "({}, {})".format(self.absc, self.ord)

	def __eq__(self, testedEqual):
		print("passed")
		return (self.absc == testedEqual.absc) and (self.ord == testedEqual.ord)
