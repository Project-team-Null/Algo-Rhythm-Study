from sys import stdin
from collections import deque

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        frm, to = map(int, read().rstrip().split())
        graph[frm].append(to)
        graph[to].append(frm)
    
    visited = set()
    ans = 0
    for i in range(1, n+1):
        if i not in visited:
            ans += 1
            que = deque([i])
            while len(que) != 0:
                cur = que.pop()
                if cur not in visited:
                    visited.add(cur)
                    for child in graph[cur]:
                        if child not in visited: que.append(child)
    print(ans)