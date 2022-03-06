from sys import stdin
from collections import deque

def bfs(graph, n):
    ret = []
    for i in range(1, n+1):
        que = deque([(i, 0)])
        visited = set()
        ans = 0
        while len(que) != 0:
            user, step = que.popleft()
            if user not in visited:
                visited.add(user)
                ans += step
                for child in graph[user]:
                    que.append((child, step+1))
        ret.append(ans)
    return ret


if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    graph = [set() for _ in range(n+1)]
    for _ in range(m):
        frm, to = map(int, read().rstrip().split())
        graph[frm].add(to)
        graph[to].add(frm)
    
    ans = bfs(graph, n)
    temp = float("inf")
    idx = -1
    for i in range(n):
        if ans[i] < temp:
            temp = ans[i]
            idx = i+1
    print(idx)