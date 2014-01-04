# **coding:utf8**

import errors as E
from itertools import izip


class sequence(str):
    base = ('A', 'C', 'G', 'T')

    def __new__(cls, seq):
        seq = seq.upper()
        for l in seq:
            if l not in cls.base:
                raise E.NotSeqError()
        return str.__new__(cls, seq)

    def subs(self, locs, **kwargs):
        l = int(kwargs.get('len', 1))
        subl = [self[loc:loc + l] for loc in locs]
        return subl

    def _ind(i, j):
        return 1 if i == j else 0

    def likelihood(self, locs, l, theta, prior):
        """
            compute the likelihood of the sequence.
            Parameters:
                - `locs`: motif starting points.
                - `l`: motif length
                - `theta`: motif and background compositions. 2d-arr, (l+1)*4
                - `prior`: prior distribution of locs
            Return:
                likelihood of the sequence.
        """
        assert len(theta(0)) == l + 1, "motif length and theta not match"
        mask = [0] * len(self)
        for loc in locs:
            mask[loc:loc + l] = [1] * l
        seq = izip(self, mask)
        base = dict(zip(self.base, [0, 1, 2, 3]))
        mult = 1.0
        # (m, s) = ('A', 0)
        flag, index = (0, 0)
        for m, s in seq:
            if s == 1:
                index += 1
                mult *= theta[index][base[m]]
                index %= l
                # bkgrd -> motif
                if flag == 0:
                    flag = 1
                continue
            if s == 0:
                mult *= theta[s][base[m]]
                # motif -> bkgrd
                if flag == 1:
                    flag = 0
                continue

    def forwardsum(self, locs, l, theta, prior):
        pass

    def backwardsum(self, locs, l, theta, prior):
        pass
