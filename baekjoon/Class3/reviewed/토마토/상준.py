from sys import stdin
from collections import deque

def bfs(board, start, cnt, m, n, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    for pos in start:
        que.append((pos[0], pos[1], cnt))
    max_cnt = 0
    while len(que) != 0:
        (y, x, c) = que.popleft()
        if (y, x) not in visited:
            visited.add((y,x))
            max_cnt = c
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<m and board[ny][nx] != -1:
                    que.append((ny, nx, c+1))
    return max_cnt


if __name__ == '__main__':
    read = stdin.readline
    m, n = map(int, read().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, read().split())))
    
    start = []
    tom_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                start.append((i, j))
            if board[i][j] != -1:
                tom_cnt += 1
    
    visited = set()
    ans = bfs(board, start, 0, m, n, visited)
    if tom_cnt != len(visited): ans = -1
    print(ans)