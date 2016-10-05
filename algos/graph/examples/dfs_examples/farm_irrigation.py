__author__ = 'qin xue'


def dfs_recur(i, j, x, m, n):
    print(i, j)
    tmp = x[i][j]
    if judge_is_available(i, j, i - 1, j, x, m, n):  # move up
        x[i][j] = '*'
        dfs_recur(i - 1, j, x, m, n)
        x[i][j] = tmp
    if judge_is_available(i, j, i, j + 1, x, m, n):  # move right
        x[i][j] = '*'
        dfs_recur(i, j + 1, x, m, n)
        x[i][j] = tmp
    if judge_is_available(i, j, i + 1, j, x, m, n):  # move down
        x[i][j] = '*'
        dfs_recur(i + 1, j, x, m, n)
        x[i][j] = tmp
    if judge_is_available(i, j, i, j - 1, x, m, n):  # move left
        x[i][j] = '*'
        dfs_recur(i, j - 1, x, m, n)
        x[i][j] = tmp
    x[i][j] = '*'


def judge_is_available(ci, cj, si, sj, x, m, n):
    if not (0 <= si <= m - 1 and 0 <= sj <= n - 1):
        return False
    if x[ci][cj] == 'A':  # if current square is 'A'
        return is_match_up(ci, cj, si, sj, x) or is_match_left(ci, cj, si, sj, x)
    if x[ci][cj] == 'B':  # 'B;
        return is_match_up(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x)
    if x[ci][cj] == 'C':  # 'C'
        return is_match_down(ci, cj, si, sj, x) or is_match_left(ci, cj, si, sj, x)
    if x[ci][cj] == 'D':  # 'D'
        return is_match_right(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj, x)
    if x[ci][cj] == 'E':  # 'E'
        return is_match_up(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj, x)
    if x[ci][cj] == 'F':  # 'F'
        return is_match_left(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x)
    if x[ci][cj] == 'G':  # 'G'
        return is_match_left(ci, cj, si, sj, x) or is_match_up(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x)
    if x[ci][cj] == 'H':  # 'H'
        return is_match_left(ci, cj, si, sj, x) or is_match_up(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj, x)
    if x[ci][cj] == 'I':  # 'I'
        return is_match_left(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj, x)
    if x[ci][cj] == 'J':  # 'J'
        return is_match_up(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj, x)
    if x[ci][cj] == 'K':  # 'K'
        return is_match_up(ci, cj, si, sj, x) or is_match_right(ci, cj, si, sj, x) or is_match_down(ci, cj, si, sj,
                                                                                                    x) or is_match_left(
            ci, cj, si, sj, x)
    return False


def is_match_up(ci, cj, si, sj, x):
    if ci - 1 == si and cj == sj:  # up
        if x[si][sj] in ('C', 'D', 'E', 'H', 'I', 'J', 'K'):
            return True
    return False


def is_match_left(ci, cj, si, sj, x):
    if ci == si and cj - 1 == sj:  # left
        if x[si][sj] in ('B', 'D', 'F', 'G', 'I', 'J', 'K'):
            return True
    return False


def is_match_right(ci, cj, si, sj, x):
    if ci == si and cj + 1 == sj:  # right
        if x[si][sj] in ('A', 'C', 'F', 'G', 'H', 'I', 'K'):
            return True
    return False


def is_match_down(ci, cj, si, sj, x):
    if ci + 1 == si and cj == sj:  # down
        if x[si][sj] in ('A', 'B', 'E', 'G', 'H', 'J', 'K'):
            return True
    return False


def search(x, m, n):
    count = 0
    for i in range(m):
        for j in range(n):
            if x[i][j] != '*':  # if meet not visited field
                count += 1
                dfs_recur(i, j, x, m, n)
    print(count)


if __name__ == '__main__':
    x = [['A', 'D', 'C'],
         ['F', 'J', 'K'],
         ['I', 'H', 'E']]
    # search(x, 3, 3)
    x = [['D', 'K'],
         ['H', 'F']]
    # search(x, 2, 2)
    x = [['A', 'D', 'C'],
         ['F', 'J', 'K'],
         ['I', 'H', 'E']]
    search(x, 3, 3)
