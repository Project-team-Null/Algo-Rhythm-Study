from sys import stdin
from collections import defaultdict


def bellmanford(graph, n):
    dist = [1000000000] * (n + 1)
    for i in range(n):
        for j in range(1, n + 1):
            for next_node, weight in graph[j]:
                temp = dist[j] + weight
                if temp < dist[next_node]:
                    if i == n - 1:
                        return "YES"
                    dist[next_node] = temp
    return "NO"


if __name__ == "__main__":
    read = stdin.readline
    tc = int(read())
    for _ in range(tc):
        n, m, w = map(int, read().split())
        graph = defaultdict(list)
        for __ in range(m):
            s, e, t = map(int, read().split())
            graph[s].append((e, t))
            graph[e].append((s, t))
        for __ in range(w):
            s, e, t = map(int, read().split())
            graph[s].append((e, -t))
        print(bellmanford(graph, n))
