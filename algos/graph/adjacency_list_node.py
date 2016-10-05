__author__ = 'qin xue'


class AdjacencyListNode(object):
    def __init__(self):
        self.next_arc = None

    def set_next_arc(self, arc):
        self.next_arc = arc

    def get_next_arc(self):
        return self.next_arc
