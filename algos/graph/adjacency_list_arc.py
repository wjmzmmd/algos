__author__ = 'qin xue'


class AdjacencyListArc(object):
    def __init__(self, value=-1):
        self.next_arc = None
        self.value = value

    def set_next_arc(self, arc):
        self.next_arc = arc

    def get_next_arc(self):
        return self.next_arc

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
