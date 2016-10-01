__author__ = 'qin xue'
"""
find and print the longest sub-sequence for list x, y
"""


def lcs_length(x, y, c, b):
    m = len(x)
    n = len(y)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # left up
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2  # up
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3  # left


def search_sub_sequence(x, b, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 1:
        print(x[i - 1])
        search_sub_sequence(x, b, i - 1, j - 1)
    elif b[i][j] == 2:
        search_sub_sequence(x, b, i, j - 1)
    elif b[i][j] == 3:
        search_sub_sequence(x, b, i - 1, j)


if __name__ == '__main__':
    x = 'abcsss'
    y = 'sdfiqe'
    print(x)
    print(y)
    m = len(x)
    n = len(y)
    c = [([0] * (n + 1)) for i in range(m + 1)]
    b = [([0] * (n + 1)) for i in range(m + 1)]
    # print(c)
    lcs_length(x, y, c, b)
    print(c)
    print(b)
    search_sub_sequence(x, b, m, n)
