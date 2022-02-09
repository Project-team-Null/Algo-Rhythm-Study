
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def solution(nodes, n):
    visited = set()
    cnt = 0

    def bfs(start):
        que = deque([start])
        while que:
            cur = que.popleft()
            for to in nodes[cur]:
                if to not in visited:
                    que.append(to)
                    visited.add(to)

    for node in range(1, n + 1):
        if node not in visited:
            visited.add(node)
            bfs(node)
            cnt += 1

    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    nodes = defaultdict(list)
    for _ in range(m):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    print(solution(nodes, n))
