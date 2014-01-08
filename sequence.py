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

    def likelihood(self, locs, l, theta, prior, **kwargs):
        """
            compute the likelihood of the sequence.
            Parameters:
                - `locs`: motif starting points.
                - `l`: motif length
                - `theta`: motif and background compositions. 2d-arr, (l+1)*4
                - `prior`: prior distribution of locs
                - `kwargs`: i, j for slicing the sequence.
            Return:
                likelihood of the sequence.
        """
        assert len(theta(0)) == l + 1, "motif length and theta not match"
        (i, j) = (int(kwargs.get('i')), int(kwargs.get('j'))) if kwargs \
            else (None, None)
        mask = [0] * len(self)
        for loc in locs:
            mask[loc:loc + l] = [1] * l
        seq = izip(self, mask) if (i, j) is (None, None) \
            else izip(self[i:j], mask)

        base = dict(zip(self.base, [0, 1, 2, 3]))
        mult = 1.0
        # (m, s) = ('A', 0)
        flag, index = (0, 0)
        for m, s in seq:
            if s == 1:
                mult *= theta[index + 1][base[m]]
                index = (index + 1) % l
                # bkgrd -> motif
                flag = 1 if not flag else flag
                continue
            if s == 0:
                mult *= theta[s][base[m]]
                # motif -> bkgrd
                flag = 0 if flag else flag
                continue
        return mult

    def fbsum(self, c, l, theta, prior, ii, jj):
        """
        Description:
            compute forward sum and backward sum.
        Parameters:
            ---
            c: length of locs.
            prior: prior distribution of Y. all possible values can be
                   extracted easily from this distribution.
            ii and jj are index to slide the sequence. when computing
            forward sum, `ii=0` and `jj<len(sequence)`; when computing
            backward sum, `ii<len(sequence)` and `jj=len(sequence)`.
        """
        assert c == len(locs)
        # Init.
        if c == 0:
            return 1
        for c in xrange(1,len(self)/l+1):
            if jj < c*l:
                return 0
        # FIXME:prior should be properly designed to make this work.
        tmp = [self.likelihood(v, l, theta, prior, i=ii, j=jj)
               for v in prior]
        numerator = sum(tmp)
        denominator = 1.0
        for s in self[ii:jj]:
            denominator *= theta[0][s]
        return 1.0 * numerator / denominator

    def fwdsum(self, c, j, theta, l):
        base = dict(zip(self.base, xrange(0,4)))
        def lamda(j, theta, l):
            ret = 1.0
            for pos in xrange(j, j+l):
                try:
                    ret *= float(theta[pos + 1 - j][base[self[pos]]]) / float(theta[0][base[self[pos]]])
                except IndexError:
                    print "%d %d %d" % (j, pos + 1 - j, base[self[pos]])
                    raise
            return ret


        if c == 0:
            return 1
        if j < c * l:
            return 0
        return self.fwdsum(c, j-1, theta, l) + self.fwdsum(c-1,j-l,theta, l) * \
                lamda(j-l+1, theta, l)
