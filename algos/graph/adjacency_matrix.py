__author__ = 'qin xue'


class AdjacencyMatrix(object):
    def __init__(self, m, n):
        self.x = [([-1] * n) for i in range(m)]
