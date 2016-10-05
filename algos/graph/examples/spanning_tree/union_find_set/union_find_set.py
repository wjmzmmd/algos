__author__ = 'qin xue'


def find(x, parent):
    s = x
    while parent[s] >= 0:
        s = parent[s]
    while s != x:
        tmp = parent[x]
        parent[x] = s
        x = tmp
    return s


def union(r1, r2, parent):
    s1 = find(r1, parent)
    s2 = find(r2, parent)
    if s1 == s2:  # the same set, then return
        return False
    tmp = parent[s1] + parent[s2]
    if parent[s1] > parent[s2]:
        parent[s1] = s2
        parent[s2] = tmp
    else:
        parent[s2] = s1
        parent[s1] = tmp
    return True
