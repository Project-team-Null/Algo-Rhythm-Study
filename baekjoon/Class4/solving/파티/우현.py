from collections import defaultdict
import heapq
from sys import stdin
input = stdin.readline


def dijkstra(graph, n, k):
    heap = []
    distance = [float('inf')] * (n + 1)
    distance[k] = 0
    heapq.heappush(heap, (0, k))
    while heap:
        dist, current = heapq.heappop(heap)
        if dist > distance[current]:
            continue
        for next_node, w in graph[current].items():
            temp = distance[current] + w
            if temp < distance[next_node]:
                distance[next_node] = temp
                heapq.heappush(heap, (temp, next_node))
    return distance


def aStar(graph, n, frm, to):  # heuristic = 0
    heap = []
    heapq.heappush(heap, (0, frm))
    visited = [float('inf')] * (n + 1)
    visited[frm] = 0
    while heap:
        dist, current = heapq.heappop(heap)
        if dist > visited[current]:
            continue
        if current == to:
            return dist
        for next_node, w in graph[current].items():
            temp = dist + w
            if visited[next_node] > temp:
                visited[next_node] = temp
                heapq.heappush(heap, (temp, next_node))


# def floydWarshall(graph, n):
#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             if graph[i][k] != float('inf'):
#                 for j in range(1, n + 1):
#                     if i == j:
#                         graph[i][j] = 0
#                         continue
#                     temp = graph[i][k] + graph[k][j]
#                     if graph[i][j] > temp:
#                         graph[i][j] = temp
#     return


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    graph = [defaultdict(lambda: float('inf')) for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a][b] = w
    x_to_n = dijkstra(graph, n, x)
    max_cost = 0
    for i in range(1, n + 1):
        max_cost = max(max_cost, x_to_n[i] + aStar(graph, n, i, x))
    print(max_cost)
