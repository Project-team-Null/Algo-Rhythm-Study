from sys import stdin
from collections import deque
from collections import defaultdict


def solution(tree, n, root):
    queue = deque([root])
    cost = [-1] * (n + 1)
    cost[root] = 0
    ret = [root, 0]
    while queue:
        node = queue.popleft()
        for i, w in tree[node]:
            if cost[i] == -1:
                cost[i] = cost[node] + w
                queue.append(i)
                if ret[1] < cost[i]:
                    ret = [i, cost[i]]
    return ret


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    tree = defaultdict(list)
    for _ in range(n - 1):
        a, b, w = map(int, read().split())
        tree[a].append((b, w))
        tree[b].append((a, w))
    leaf, _ = solution(tree, n, 1)
    print(solution(tree, n, leaf)[1])
