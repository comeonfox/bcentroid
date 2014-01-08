class dist(object):
    """
        A distribution class.
    """
    def __init__(self, values, **kwargs):
        self.values = values
        probs = self.prob(**kargs) if kwargs else self.prob()
        self.table = dict(zip(self.values, probs))

    def prob(self, **kwargs):
        # should be implemented by subclasses
        pass

    def __iter__(self):
        for n in self.table.keys():
            yield n

    def lookup(self, value):
        return self.table.get(value, 0)


class uniform(dist):
    def prob(self):
        return [1.0 / len(self.values) for v in self.values]


def PcY(sequence, theta, l, priorC):
    n = len(sequence)
    for c in priorC:
        numerator = sequence.fbsum(c,
