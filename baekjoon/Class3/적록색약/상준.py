from sys import stdin
from collections import deque
import copy

def bfs(board, n):
    ret = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque()
    visited = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                ret += 1
                que.append((i, j))
                ref = board[i][j]
                while len(que) != 0:
                    y, x = que.pop()
                    if (y, x) not in visited:
                        visited.add((y, x))
                        for k in range(4):
                            ny = y + dy[k]
                            nx = x + dx[k]
                            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == ref:
                                que.append((ny, nx))
    return ret

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    board1 = [list(read().rstrip()) for _ in range(n)]
    board2 = copy.deepcopy(board1)
    for i in range(n):
        for j in range(n):
            if board2[i][j] == 'G':
                board2[i][j] = 'R'
    
    print(bfs(board1, n), bfs(board2, n))