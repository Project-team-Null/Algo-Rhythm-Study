from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline


def dijkstra(graph, start, n, mid1, mid2):
    heap = [(0, start)]
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    while heap:
        cur_dis, node = heapq.heappop(heap)
        if cur_dis > distance[node]:
            continue
        for next_node, w in graph[node].items():
            temp = cur_dis + w
            if temp < distance[next_node]:
                distance[next_node] = temp
                heapq.heappush(heap, (temp, next_node))
    return distance[mid1], distance[mid2]


if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = {i: defaultdict(lambda: float('inf')) for i in range(1, n + 1)}
    for _ in range(e):
        frm, to, w = map(int, input().split())
        graph[frm][to] = min(graph[frm][to], w)
        graph[to][frm] = min(graph[to][frm], w)
    mid1, mid2 = map(int, input().split())
    one2m1, one2m2 = dijkstra(graph, 1, n, mid1, mid2)
    n2m1, n2m2 = dijkstra(graph, n, n, mid1, mid2)
    _, m2m = dijkstra(graph, mid1, n, mid1, mid2)
    ans = min(one2m1 + n2m2, one2m2 + n2m1) + m2m
    print(-1 if ans == float('inf') else ans)
