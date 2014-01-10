# coding:utf8


import numpy as np
import sequence as sq
from dist import *
from itertools import izip
import sys

def iPrint(seq, theta, y, l):
    ret = []
    for ss, yy in izip(seq, y):
        ins = ss.subs(yy, len=l)
        inf = zip(yy, ins)
        print inf[0][1]
        ret.append(inf)
    print theta

def getSeqs(fn):
    s = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            if '>' in line:
                continue
            s.append(line.strip())
    return [sq.sequence(l) for l in s]

def getTheta(l, source=None):
    if source is not None:
        # read from file
        t = [] #shape (l+1)*4
        with open(source, 'r') as f:
            for line in f.readlines():
                t.append(line.strip().split())
        t = np.array(t, dtype='float')
        return t
    t = np.random.rand(l+1, 4)
    for line in t:
        line /= sum(line)
    return t

def update_theta(ss, yy, l):
    t = np.empty((l+1, 4))
    t.fill(0)
    base = dict(zip(('A','C','G','T'),range(4)))
    count = dict(zip(('A','C','G','T'),[0]*4))
    for s, y in izip(ss, yy):
        mask = [0]*len(s)
        for p in y:
            mask[p:p+l] = [1]*l
        flag, index = 0, 0
        for b, m in izip(s, mask):
            if m == 1:
                t[index + 1][base[b]] += 1
                index = (index + 1) % l
                flag = 1 if not flag else flag
                continue
            if m == 0:
                t[m][base[b]] += 1
                flag = 0 if flag else flag
                continue
    # post process
    for line in t:
        line /= sum(line)
    return t

def main(**kwargs):
    fn = kwargs.get('f',None)
    l = int(kwargs.get('len', 10))
    rounds = int(kwargs.get('t', 1000))
    num = int(kwargs.get('n', 0))
    seqs = getSeqs(fn)
    theta = getTheta(l)
    for r in xrange(rounds):
        # get y
        y = []
        for seq in seqs:
            # get c
            clist = range(int(len(seq)/l))
            priorC = prior_cy(clist, n=len(seq), l=l)
            if not num:
                c = P_c_Y(clist, s=seq, t=theta, l=l, p=priorC)
                c = c.draw()
            else:
                c = num
            # get y
            yy = np.empty(c + 1)
            yy.fill(-1)
            yy[-1] = len(seq)
            for k in reversed(range(1,c+1)):
                rg = range((k-1)*l, int(yy[k])-l)
                if not rg:
                    # terminate
                    yy = yy[k:]
                    break
                if len(rg) == 1:
                    yy[k-1] = rg[0]
                    yy = yy[k-1:]
                    break
                yy_k = p_y_k(rg, s=seq, t=theta, l=l, c=c, k=k-1)
                yy[k-1] = yy_k.draw()
            yy =[int(n) for n in yy[:-1]]
            y.append(yy[:])
        # update theta
        theta = update_theta(seqs, y, l)

    iPrint(seqs, theta, y, l)


if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {}
    for a in args:
        n, v = a.split('=')
        kwargs[n] = v
    main(**kwargs)
