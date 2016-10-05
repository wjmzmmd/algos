__author__ = 'qin xue'


class AdjacencyList(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, i):
        return self.nodes[i]

    def get_node_size(self):
        return len(self.nodes)
