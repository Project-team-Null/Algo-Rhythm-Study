from sys import stdin
from collections import deque
from queue import PriorityQueue

def bfs(space, pos):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    que = deque([(pos[0], pos[1], 0)])
    visited = set()
    pq = PriorityQueue()
    ans = 0
    size = 2
    eat_count = 0
    while True:
        while len(que) != 0:
            y, x, time = que.popleft()
            if (y, x) not in visited:
                visited.add((y, x))
                if 0 < space[y][x] < size:
                    pq.put((time, y, x))
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<n and 0<=nx<n and space[ny][nx] <= size:
                        que.append((ny, nx, time+1))
        if pq.empty(): break
        time, y, x = pq.get()
        while not pq.empty():
            pq.get()
        space[y][x] = 0
        ans += time
        if eat_count + 1 == size:
            size += 1
            eat_count = 0
        else: eat_count += 1
        visited.clear()
        que.append((y, x, 0))
    return ans


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    space = [list(map(int, read().rstrip().split())) for _ in range(n)]
    pos = None
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                pos = (i, j)
                space[i][j] = 0
    
    print(bfs(space, pos))