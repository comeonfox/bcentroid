# **coding:utf8**

import errors as E


class sequence(str):
    base = ('A', 'C', 'G', 'T')

    def __new__(cls, seq):
        seq = seq.upper()
        for l in seq:
            if l not in cls.base:
                raise E.NotSeqError()
        return str.__new__(cls, seq)

    def subs(self, locs, **kwargs):
        l = int(kwargs.get('l', 1))
        subl = [self[loc:loc + l] for loc in locs]
        return subl

    def likelihood(self, locs, l, theta, prior):
        """
            compute the likelihood of the sequence.
            Parameters:
                - `locs`: motif starting points.
                - `l`: motif length
                - `theta`: motif and background compositions.
                - `prior`: prior distribution of locs
            Return:
                likelihood of the sequence.
        """
        assert len(theta(0)) == l + 1, "motif length and theta not match"
        pass

    def forwardsum(self, locs, l, theta, prior):
        pass

    def backwardsum(self, locs, l, theta, prior):
        pass
