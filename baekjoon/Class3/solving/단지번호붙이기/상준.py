from sys import stdin
from collections import deque

def bfs(board, pos):
    ret = 0
    dy = [1, -1 ,0, 0]
    dx = [0, 0, 1, -1]

    que = deque([pos])
    while len(que) != 0:
        y, x = que.popleft()
        if board[y][x] == '1':
            board[y][x] = '0'
            ret += 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '1':
                    que.append((ny, nx))
    return ret



if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    board = [list(read().rstrip()) for _ in range(n)]
    
    ans = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':
                ans.append(bfs(board, (i, j)))
    ans.sort()

    print(len(ans))
    for a in ans:
        print(a)