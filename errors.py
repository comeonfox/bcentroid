# -*- coding: utf8 -*-
"""
    Several Exceptions are defined here.
"""


class NotSeqError(Exception):
    def __init__(self, value="Sequence provided is not a DNA sequence"):
        self.value = value

    def __str__(self):
        return self.value

if __name__ == '__main__':
    raise NotSeqError()
