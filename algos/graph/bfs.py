from algos.graph.adjacency_list import AdjacencyList
from algos.graph.adjacency_list_arc import AdjacencyListArc
from algos.graph.adjacency_list_node import AdjacencyListNode

__author__ = 'qin xue'


def bfs_list(start_spot, x):
    queue = [start_spot]
    index = -1
    while index < len(queue) - 1:
        index += 1
        curr = queue[index]
        # print(curr)
        arc = x.get_node(curr).get_next_arc()
        while arc:
            value = arc.get_value()
            if value not in queue:
                queue.append(value)
            arc = arc.get_next_arc()
    print(queue)


def bfs_matrix(start_spot, x, n):
    queue = [start_spot]
    index = -1
    while index < len(queue) - 1:
        index += 1
        curr = queue[index]
        # print(curr)
        for j in range(n):
            if x[curr][j] != -1 and j not in queue:
                queue.append(j)
    print(queue)


if __name__ == '__main__':
    # x = AdjacencyList()
    # node = AdjacencyListNode()
    # arc1 = AdjacencyListArc(1)
    # node.set_next_arc(arc1)
    # x.add_node(node)
    # arc2 = AdjacencyListArc()
    x = [[-1, 1, -1, 1, 1, -1, -1, -1, -1],
         [1, -1, 1, -1, 1, -1, -1, -1, -1],
         [-1, 1, -1, -1, -1, -1, 1, -1, -1],
         [1, -1, -1, -1, -1, 1, -1, -1, -1],
         [1, 1, -1, -1, -1, 1, -1, -1, -1],
         [-1, -1, -1, 1, 1, -1, -1, 1, -1],
         [-1, -1, 1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, 1, -1, -1, 1],
         [-1, -1, -1, -1, -1, -1, -1, 1, -1]]
    # bfs_matrix(0, x, 9)
    print('=====')
    x = AdjacencyList()
    node = AdjacencyListNode()  # 0
    arc1 = AdjacencyListArc(1)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(3)
    arc1.set_next_arc(arc2)
    arc3 = AdjacencyListArc(4)
    arc2.set_next_arc(arc3)
    node = AdjacencyListNode()  # 1
    arc1 = AdjacencyListArc(0)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(2)
    arc1.set_next_arc(arc2)
    arc3 = AdjacencyListArc(4)
    arc2.set_next_arc(arc3)
    node = AdjacencyListNode()  # 2
    arc1 = AdjacencyListArc(1)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(6)
    arc1.set_next_arc(arc2)
    node = AdjacencyListNode()  # 3
    arc1 = AdjacencyListArc(0)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(5)
    arc1.set_next_arc(arc2)
    node = AdjacencyListNode()  # 4
    arc1 = AdjacencyListArc(0)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(1)
    arc1.set_next_arc(arc2)
    arc3 = AdjacencyListArc(5)
    arc2.set_next_arc(arc3)
    node = AdjacencyListNode()  # 5
    arc1 = AdjacencyListArc(3)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(4)
    arc1.set_next_arc(arc2)
    arc3 = AdjacencyListArc(7)
    arc2.set_next_arc(arc3)
    node = AdjacencyListNode()  # 6
    arc1 = AdjacencyListArc(2)
    node.set_next_arc(arc1)
    x.add_node(node)
    node = AdjacencyListNode()  # 7
    arc1 = AdjacencyListArc(5)
    node.set_next_arc(arc1)
    x.add_node(node)
    arc2 = AdjacencyListArc(8)
    arc1.set_next_arc(arc2)
    node = AdjacencyListNode()  # 8
    arc1 = AdjacencyListArc(7)
    node.set_next_arc(arc1)
    x.add_node(node)
    bfs_list(0, x)
