from sys import stdin
from collections import deque

if __name__ == '__main__':
    read = stdin.readline
    m, n, h = map(int, read().rstrip().split())
    board = []
    for i in range(h):
        board.append([list(map(int, read().strip().split())) for _ in range(n)])

    que = deque()
    tom = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    que.append((i,j,k,0))
                if board[i][j][k] != -1:
                    tom += 1
    
    dz, dy, dx = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    cnt = 0
    while len(que) != 0:
        z, y, x, c = que.popleft()
        if board[z][y][x] == 1:
            cnt = c
            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and board[nz][ny][nx] == 0:
                    board[nz][ny][nx] = 1
                    que.append((nz, ny, nx, c+1))
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    print(-1)
                    exit(0)
    print(cnt)
    