from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline


def dijkstra(graph, frm, to, n):
    heap = []
    distance = [float('inf')] * (n + 1)
    distance[frm] = 0
    heapq.heappush(heap, (0, frm))
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distance[node]:
            continue
        for next_node, w in graph[node].items():
            temp = cost + w
            if temp < distance[next_node]:
                distance[next_node] = temp
                heapq.heappush(heap, (temp, next_node))
    return distance[to]


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for _ in range(m):
        frm, to, w = map(int, input().split())
        graph[frm][to] = min(graph[frm][to], w)
    frm, to = map(int, input().split())
    print(dijkstra(graph, frm, to, n))
