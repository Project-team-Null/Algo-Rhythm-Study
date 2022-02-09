from sys import stdin
from collections import deque


def bfs(board, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def neighbor(y, x):
        lst = []
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0 <= px < m and 0 <= py < n:
                lst.append((py, px))
        return lst

    queue = deque([(0, 0, board[0][0])])
    visited = set([(0, 0, board[0][0])])
    length = 1
    depth = 1

    while length:
        for _ in range(length):
            cur_y, cur_x, cnt = queue.popleft()
            if cur_y == n - 1 and cur_x == m - 1:
                return depth
            for y, x in neighbor(cur_y, cur_x):
                block = board[y][x] + cnt
                if (y, x, cnt) not in visited and block <= 1:
                    visited.add((y, x, block))
                    queue.append((y, x, block))
        depth += 1
        length = len(queue)
    return -1


if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        temp = read()
        for j in range(m):
            board[i][j] = int(temp[j])
    print(bfs(board, n, m))
