from sys import stdin
from collections import deque
from collections import defaultdict


def bfs(tree, n):
    queue = deque([1])
    lst = [0] * (n + 1)
    lst[1] = 1
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if lst[i] == 0:
                lst[i] = node
                queue.append(i)
    return lst[2:]


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    tree = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, read().split())
        tree[a].append(b)
        tree[b].append(a)
    for i in bfs(tree, n):
        print(i)
