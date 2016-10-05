__author__ = 'qin xue'


def dfs_recur(i, j, x, m, n):
    print(i, j)
    x[i][j] = 'D'
    if judge_is_available(i - 1, j - 1, x, m, n):
        dfs_recur(i - 1, j - 1, x, m, n)
    if judge_is_available(i - 1, j, x, m, n):
        dfs_recur(i - 1, j, x, m, n)
    if judge_is_available(i - 1, j + 1, x, m, n):
        dfs_recur(i - 1, j + 1, x, m, n)
    if judge_is_available(i, j + 1, x, m, n):
        dfs_recur(i, j + 1, x, m, n)
    if judge_is_available(i + 1, j + 1, x, m, n):
        dfs_recur(i + 1, j + 1, x, m, n)
    if judge_is_available(i + 1, j, x, m, n):
        dfs_recur(i + 1, j, x, m, n)
    if judge_is_available(i + 1, j - 1, x, m, n):
        dfs_recur(i + 1, j - 1, x, m, n)
    if judge_is_available(i, j - 1, x, m, n):
        dfs_recur(i, j - 1, x, m, n)


def judge_is_available(i, j, x, m, n):
    return 0 <= i <= m - 1 and 0 <= j <= n - 1 and x[i][j] == '@'


def search(x, m, n):
    num = 0
    for i in range(m):
        for j in range(n):
            if x[i][j] == '@':
                num += 1
                dfs_recur(i, j, x, m, n)
    print(num)


if __name__ == '__main__':
    x = [['*', '@', '*', '@', '*'],
         ['*', '*', '@', '*', '*'],
         ['*', '@', '*', '@', '*']]
    # search(x, 3, 5)
    x = [['*', '*', '*', '*', '@'],
         ['*', '@', '@', '*', '@'],
         ['*', '@', '*', '*', '@'],
         ['@', '@', '@', '*', '@'],
         ['@', '@', '*', '*', '@']]
    search(x, 5, 5, )
