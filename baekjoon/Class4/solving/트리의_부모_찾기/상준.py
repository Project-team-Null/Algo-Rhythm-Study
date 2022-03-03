from sys import stdin
from collections import deque

def bfs(tree):
    visited = set()
    ret = {}
    que = deque([1])
    while len(que) != 0:
        cur = que.popleft()
        visited.add(cur)
        for child in tree[cur]:
            if child in visited: continue
            ret[child] = cur
            que.append(child)
    return ret


if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        frm, to = map(int, read().split())
        tree[frm].append(to)
        tree[to].append(frm)
    
    ans = bfs(tree)
    for i in range(2, n+1):
        print(ans[i])