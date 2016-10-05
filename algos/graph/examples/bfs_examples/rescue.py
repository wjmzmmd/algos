from functools import reduce

__author__ = 'qin xue'


def bfs_recur(si, sj, x, m, n):
    queue = [[si, sj, 0]]  # the start location is angel's friend's current location and time cost is 0
    index = -1
    ret_list = []
    while index < len(queue) - 1:
        index += 1
        curr = queue[index]
        ci = curr[0]
        cj = curr[1]
        cnt = curr[2]
        if x[ci][cj] == 'a':
            print('cnt:', cnt)
            ret_list.append(cnt)
            continue
        if judge_available_move(ci - 1, cj, queue, x, m, n):  # up
            add_to_queue(ci - 1, cj, queue, cnt)
        if judge_available_move(ci, cj + 1, queue, x, m, n):  # right
            add_to_queue(ci, cj + 1, queue, cnt)
        if judge_available_move(ci + 1, cj, queue, x, m, n):  # down
            add_to_queue(ci + 1, cj, queue, cnt)
        if judge_available_move(ci, cj - 1, queue, x, m, n):  # left
            add_to_queue(ci, cj - 1, queue, cnt)
    if ret_list:
        print(min(ret_list))
    else:
        print('Poor ANGEL has to stay in the prison all his life.')


def judge_available_move(i, j, queue, x, m, n):
    return 0 <= i <= m - 1 and 0 <= j <= n - 1 and x[i][j] != '#'


def add_to_queue(i, j, queue, cnt):
    if x[i][j] == 'x':
        cnt += 2
    elif x[i][j] == '.':
        cnt += 1
    elif x[i][j] == 'a':
        cnt += 1
    if not reduce(lambda a, b: a or b, map(deal_queue, queue, [[i, j, cnt]] * len(queue))):
        queue.append([i, j, cnt])


def deal_queue(x, y):
    if x[0] == y[0] and x[1] == y[1]:
        if x[2] <= y[2]:
            return True
    return False


if __name__ == '__main__':
    x = [['#', '.', '#', '#', '#', '#', '#', '.'],
         ['#', '.', 'a', '#', '.', '.', 'r', '.'],
         ['#', '.', '.', '#', 'x', '.', '.', '.'],
         ['.', '.', '#', '.', '.', '#', '.', '#'],
         ['#', '.', '.', '.', '#', '#', '.', '.'],
         ['.', '#', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]
    # bfs_recur(1, 6, x, 7, 8)
    x = [['#', '.', '#', '#', '#', '#', '#', '.'],
         ['#', 'a', '1', '#', 'x', 'r', '.', '.'],
         ['#', '.', 'x', '#', 'x', 'x', '.', '.'],
         ['.', '.', '#', '#', '#', '#', '.', '#'],
         ['#', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '#', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]
    bfs_recur(1, 5, x, 7, 8)
