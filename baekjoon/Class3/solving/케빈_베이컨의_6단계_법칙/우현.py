from collections import deque
from collections import defaultdict


def bfs(graph, i):
    queue = deque([i])
    visited = set([i])
    length = len(queue)
    depth = 1
    cost = 0
    while length:
        for _ in range(length):
            node = queue.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
                    cost += depth
        depth += 1
        length = len(queue)
    return cost


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cost = [0] * n
    for i in range(n):
        cost[i] = bfs(graph, i + 1)

    print(cost.index(min(cost)) + 1)
