# -*- coding:utf-8 -*-
'''
    Generating matrix of random numbers.
'''

import sys
import random
import numpy

class randMat(object):
    def __init__(self):
        self.empty = True
        self.matrix = []
        self.x = 0
        self.y = 0
        self.min = 0
        self.max = 10000

    def shape(self):
        return (self.x, self.y)

    def gen(self, *args):
        (self.x, self.y) = ([int(n) for n in args])
        ret = []
        for j in xrange(self.y):
            row = []
            for i in xrange(self.x):
                row.append(random.randint(self.min, self.max))
            ret.append(row)
        self.matrix = ret
        self.empty = False

    def dump(self, seperator=''):
        for row in self.matrix:
            print seperator.join([str(x) for x in row])

    def extract(self):
        return self.matrix
