from algos.graph.adjacency_list import AdjacencyList
from algos.graph.adjacency_list_arc import AdjacencyListArc
from algos.graph.adjacency_list_node import AdjacencyListNode

__author__ = 'qin xue'

"""
深度遍历算法，应用栈
"""


def dfs_matrix(x):
    """

    :param x:
    :return:
    """
    n = len(x)
    visited = [-1] * n
    q = [0]
    curr_i = 0
    visited[0] = 1
    while True:
        curr_j = 0
        while curr_j < n:
            if visited[curr_j] == -1 and x[curr_i][curr_j] != -1:
                if q[len(q) - 1] != curr_i:
                    q.append(curr_i)
                q.append(curr_j)
                visited[curr_j] = 1
                curr_i = curr_j
                curr_j = 0
                continue
            curr_j += 1
        if not q:
            break
        print(q)  # 如果在这条路上没有再新的节点了
        curr_i = q.pop()
    print(visited)


def dfs_list(x):
    visited = [-1] * len(x)
    q = [0]
    curr = 0
    visited[0] = 1
    arc = x.get_node(0).get_next_arc()
    while True:
        while arc:
            curr = arc.get_value()
            if visited[curr] == -1:
                q.append(curr)
                visited[curr] = 1
                arc = x.get_node(curr).get_next_arc()
                continue
            arc = arc.get_next_arc()
        if not q:
            break
        print(q)


def dfs_matrix_recur(x, visited, i):
    print(i)
    visited[i] = 1
    n = len(x)
    for j in range(n):
        if x[i][j] != -1 and visited[j] == -1:
            dfs_matrix_recur(x, visited, j)


def dfs_list_recur(x, visited, i):
    print(i)
    visited[i] = 1
    arc = x.get_node(i).get_next_arc()
    while arc:
        j = arc.get_value()
        if visited[j] == -1:
            dfs_list_recur(x, visited, j)
        arc = arc.get_next_arc()


if __name__ == '__main__':
    x = [[-1, 1, -1, 1, 1, -1, -1, -1, -1],
         [1, -1, 1, -1, 1, -1, -1, -1, -1],
         [-1, 1, -1, -1, -1, -1, 1, -1, -1],
         [1, -1, -1, -1, -1, 1, -1, -1, -1],
         [1, 1, -1, -1, -1, 1, -1, -1, -1],
         [-1, -1, -1, 1, 1, -1, -1, 1, -1],
         [-1, -1, 1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, 1, -1, -1, 1],
         [-1, -1, -1, -1, -1, -1, -1, 1, -1]]
    # dfs_matrix(x)
    dfs_matrix_recur(x, [-1] * len(x), 0)
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
    # dfs_list_recur(x, [-1] * x.get_node_size(), 0)
