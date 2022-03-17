from sys import stdin
from collections import deque

def bfs(cheese, n, m):
    dy = [-1, 1,  0, 0]
    dx = [ 0, 0, -1, 1]
    que = deque([(0,0)])
    visited = set()
    while len(que) != 0:
        y, x = que.popleft()
        if (y, x) in visited: continue
        visited.add((y, x))
        cheese[y][x] = -1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and (cheese[ny][nx] == 0 or cheese[ny][nx] == -1):
                que.append((ny, nx))


def is_melt(cheese, y, x):
    dy = [-1, 1,  0, 0]
    dx = [ 0, 0, -1, 1]
    cnt = 0
    for i in range(4):
        if cheese[y+dy[i]][x+dx[i]] == -1: cnt += 1
    return cnt


if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    cheese = [list(map(int, read().rstrip().split())) for _ in range(n)]
    ans = 0
    while True:
        ans += 1
        bfs(cheese, n, m)
        positions = []
        for i in range(1, n-1):
            for j in range(1, m-1):
                if cheese[i][j] == 1:
                    if is_melt(cheese, i, j) >= 2:
                        positions.append((i, j))
        if len(positions) == 0: break
        for y, x in positions:
            cheese[y][x] = -1
    print(ans-1)