__author__ = 'qin xue'


class Queue(object):
    def __init__(self):
        self.q = []

    def add(self, x):
        self.q.append(x)

    def pop(self):
        self.q.pop()
