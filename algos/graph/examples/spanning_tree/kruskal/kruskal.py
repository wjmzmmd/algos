import sys
from functools import reduce

from algos.graph.examples.spanning_tree.union_find_set.union_find_set import union

__author__ = 'qin xue'

"""
time consumption: O(log2(m) + 2m*log2(n) + n)
"""

MAX_INT = sys.maxsize


def kruskal(sorted_arcs, n):
    parent = [-1] * n
    index = -1
    selected_arcs = []
    while index < len(sorted_arcs) - 1:
        index += 1
        if union(sorted_arcs[index][0], sorted_arcs[index][1], parent):
            selected_arcs.append(sorted_arcs[index])
    print(selected_arcs)
    print(sum(map(lambda x: x[2], selected_arcs)))


def get_matrix_sorted_arcs(x, n):
    sorted_arcs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[i][j] < MAX_INT:
                sorted_arcs.append((i, j, x[i][j]))
    sorted_arcs.sort(key=lambda x: x[2])
    print(sorted_arcs)
    return sorted_arcs


def get_link_sorted_arcs(x):
    pass


if __name__ == '__main__':
    x = [[0, 28, MAX_INT, MAX_INT, MAX_INT, 10, MAX_INT],
         [28, 0, 16, MAX_INT, MAX_INT, MAX_INT, 14],
         [MAX_INT, 16, 0, 12, MAX_INT, MAX_INT, MAX_INT],
         [MAX_INT, MAX_INT, 12, 0, 22, MAX_INT, 18],
         [MAX_INT, MAX_INT, MAX_INT, 22, 0, 25, 24],
         [10, MAX_INT, MAX_INT, MAX_INT, 25, 0, MAX_INT],
         [MAX_INT, 14, MAX_INT, 18, 24, MAX_INT, 0]]
    sorted_arcs = get_matrix_sorted_arcs(x, len(x))
    kruskal(sorted_arcs, len(x))
