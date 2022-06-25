from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline


def dijkstra(graph, start, n):
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
    return distance


if __name__ == "__main__":
    n, b, s, r = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}
    rgraph = {i: {} for i in range(1, n + 1)}
    for _ in range(r):
        u, v, l = map(int, input().split())
        graph[u][v] = l
        rgraph[v][u] = l

    distance = dijkstra(graph, b + 1, n)
    rdistance = dijkstra(rgraph, b + 1, n)

    for i in range(b + 1):
        distance[i] += rdistance[i]

    d = sorted(distance[1:b + 1])

    del graph, rgraph, distance, rdistance

    dp = [0] + [float('inf')] * b
    for j in range(1, s + 1):
        new = [float('inf')] * j
        for i in range(j, b + 1):
            dsum = 0
            val = float('inf')
            for k in range(1, i // j + 1):
                dsum += d[i - k]
                val = min(val, dp[i - k] + dsum * (k - 1))
            new.append(val)
        dp = new
        print(dp)
    print(dp[b])
