from sys import stdin
import heapq

def dijk(graph, start, n):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()
    while len(heap) != 0:
        cost, cur = heapq.heappop(heap)
        if cur in visited: continue
        visited.add(cur)
        for next, c in graph[cur]:
            temp = cost + c
            if temp < dist[next]:
                dist[next] = temp
                heapq.heappush(heap, (temp, next))
    return dist


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    m = int(read().rstrip())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        frm, to, cost = map(int, read().rstrip().split())
        graph[frm].append((to, cost))
    start, end = map(int, read().rstrip().split())
    print(dijk(graph, start, n)[end])