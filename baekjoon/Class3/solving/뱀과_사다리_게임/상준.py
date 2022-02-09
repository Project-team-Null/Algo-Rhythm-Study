from sys import stdin
from collections import deque

def bfs(ladder, snake):
    que = deque([(1, 0)])
    visited = set()
    while len(que) != 0:
        cur, move = que.popleft()
        if cur == 100: return move
        if cur not in visited:
            visited.add(cur)
            for i in range(1, 7):
                if ladder.get(cur+i, 0) != 0: que.append((ladder[cur+i], move+1))
                elif snake.get(cur+i, 0) != 0: que.append((snake[cur+i], move+1))
                else: que.append((cur+i, move+1))


if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    ladder = snake = dict()
    for _ in range(n):
        x, y = map(int, read().rstrip().split())
        ladder[x] = y
    for _ in range(m):
        u, v = map(int, read().rstrip().split())
        ladder[u] = v
    
    print(bfs(ladder, snake))