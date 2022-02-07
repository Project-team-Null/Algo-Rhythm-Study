from sys import stdin
from collections import deque

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    graph = [list(map(int, read().rstrip().split())) for _ in range(n)]
    
    is_path = [[0]*n for _ in range(n)]
    que = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: que.append(j)
        while len(que) != 0:
            cur = que.popleft()
            if not is_path[i][cur]:
                is_path[i][cur] = 1
                for j in range(n):
                    if graph[cur][j] == 1: que.append(j)
    
    for i in range(n):
        print(" ".join(str(ans) for ans in is_path[i]))