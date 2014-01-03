# -*- coding:utf-8 -*-
'''
    Generating matrix of random numbers.
'''

import random


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

    def gen(self, x, y):
        self.x, self.y = int(x), int(y)
        ret = []
        for j in xrange(self.y):
            ret.append([random.randint(self.min, self.max) for n in range(self.x)])
        self.matrix = ret
        self.empty = False

    def dump(self, seperator=''):
        for row in self.matrix:
            print seperator.join([str(x) for x in row])

    def extract(self):
        return self.matrix


class randSeqs(randMat):
    def __init__(self):
        super(randSeqs, self).__init__()
        self.base = ('A', 'C', 'G', 'T')

    def gen(self, *args):
        (self.x, self.y) = ([int(n) for n in args])
        ret = []
        for j in xrange(self.y):
            ret.append([random.choice(self.base) for n in range(self.x)])
        self.matrix = ret
        self.empty = False
