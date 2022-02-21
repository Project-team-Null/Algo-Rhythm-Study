from sys import stdin
from collections import deque

def bfs(board, n, m):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    que = deque([(0, 0, 1, False)])
    visited_b = set()
    visited_a = set()
    while len(que) != 0:
        y, x, dist, broke = que.popleft()
        if y == n - 1 and x == m - 1: return dist
        if not broke:
            if (y, x) in visited_b: continue
            visited_b.add((y, x))
        else:
            if (y, x) in visited_b or (y, x) in visited_a): continue
            visited_a.add((y, x))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == '0':
                    que.append((ny, nx, dist + 1, broke))
                elif board[ny][nx] == '1' and not broke:
                    que.append((ny, nx, dist + 1, not broke))
    return -1


if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    board = [list(read().rstrip()) for _ in range(n)]
    print(bfs(board, n, m))