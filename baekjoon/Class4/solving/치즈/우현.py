from sys import stdin
from collections import deque
input = stdin.readline


def set_outside(board, n, m):
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    def neighbor(y, x):
        lst = []
        for i in range(4):
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
                lst.append((y + dy[i], x + dx[i]))
        return lst

    queue = deque([(0, 0)])
    visited = set((0, 0))
    while queue:
        y, x = queue.popleft()
        if board[y][x] == 0:
            board[y][x] = 2
        for next_y, next_x in neighbor(y, x):
            if board[next_y][next_x] != 1 and (next_y, next_x) not in visited:
                queue.append((next_y, next_x))
                visited.add((next_y, next_x))


def set_cheese(board, n, m):
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    def check(y, x):
        cnt = 0
        for i in range(4):
            temp_y = y + dy[i]
            temp_x = x + dx[i]
            if 0 <= temp_y < n and 0 <= temp_x < m and board[temp_y][temp_x] == 2:
                cnt += 1
        return cnt >= 2

    is_finished = True
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and check(y, x):
                board[y][x] = 0
                is_finished = False
    return is_finished


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    ans = 0
    set_outside(board, n, m)
    while not set_cheese(board, n, m):
        set_outside(board, n, m)
        ans += 1
    print(ans)
