# -*- coding:utf-8 -*-

def kmeans(elms, disFunc, k):
    pass

class cluster(set):
    def __init__(self, *args, **kwargs):
        self.centroid = None
        set.__init__(self, *args, **kwargs)

    @property
    def C(self):
        return self.centroid

    def setC(self, val):
        if val not in self:
            print "val has to be one of the set's elements"
        self.centroid = val
