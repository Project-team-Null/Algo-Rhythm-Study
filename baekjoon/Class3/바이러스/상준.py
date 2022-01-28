from sys import stdin
from collections import deque

def bfs(graph):
    que = deque([1])
    visited = set()
    ans = 0
    while len(que) != 0:
        cur = que.pop()
        if cur not in visited:
            visited.add(cur)
            ans += 1
            for child in graph[cur]:
                que.append(child)
    return ans


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    graph = [[] for _ in range(n+1)]
    m = int(read().rstrip())
    for _ in range(m):
        frm, to = map(int, read().rstrip().split())
        graph[frm].append(to)
        graph[to].append(frm)
    
    print(bfs(graph)-1)