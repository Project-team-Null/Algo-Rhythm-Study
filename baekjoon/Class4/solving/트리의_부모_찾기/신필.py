
from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def solution(nodes):

    def level_search(root):
        parent = [0] * (n + 1)
        parent[root] = 1
        que = deque([1])
        while que:
            p = que.popleft()
            for c in nodes[p]:
                if parent[c] == 0:
                    parent[c] = p
                    que.append(c)
        return parent

    return level_search(1)[2:]


if __name__ == "__main__":
    n = int(input())
    nodes = defaultdict(list)
    for _ in range(n - 1):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    print(*solution(nodes), sep='\n')
