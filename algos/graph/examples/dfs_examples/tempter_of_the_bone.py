__author__ = 'qin xue'

"""

"""


def dfs_recur(i, j, cnt, di, dj, t, si, sj, x, m, n):
    print(i, j, cnt)
    if i == di and j == dj and cnt == t:
        print('YES')
        return True
    temp = (t - cnt) - abs(i - di) - abs(j - dj)
    if temp < 0 or temp % 2 != 0:  # temp is negative or not even, then pruning
        return False
    if judge_is_available(i - 1, j, x, m, n):  # move up
        x[i - 1][j] = 'X'
        if dfs_recur(i - 1, j, cnt + 1, di, dj, t, si, sj, x, m, n):
            return True
        x[i - 1][j] = '.'
    if judge_is_available(i, j + 1, x, m, n):  # move right
        x[i][j + 1] = 'X'
        if dfs_recur(i, j + 1, cnt + 1, di, dj, t, si, sj, x, m, n):
            return True
        x[i][j + 1] = '.'
    if judge_is_available(i + 1, j, x, m, n):  # move down
        x[i + 1][j] = 'X'
        if dfs_recur(i + 1, j, cnt + 1, di, dj, t, si, sj, x, m, n):
            return True
        x[i + 1][j] = '.'
    if judge_is_available(i, j - 1, x, m, n):  # move left
        x[i][j - 1] = 'X'
        if dfs_recur(i, j - 1, cnt + 1, di, dj, t, si, sj, x, m, n):
            return True
        x[i][j - 1] = '.'
    if i == si and j == sj:
        print('NO')
    return False


def judge_is_available(i, j, x, m, n):
    return 0 <= i <= m - 1 and 0 <= j <= n - 1 and (x[i][j] == '.' or x[i][j] == 'D')


if __name__ == '__main__':
    x = [['S', '.', '.', '.'],
         ['.', 'X', '.', 'X'],
         ['.', '.', '.', 'D']]
    dfs_recur(0, 0, 0, 2, 3, 5, 0, 0, x, 3, 4)
