from sys import stdin
import heapq

def dijk(graph, i, n):
    dist = [float('inf')] * (n+1)
    dist[i] = 0
    heap = []
    heapq.heappush(heap, (dist[i], i))
    visited = set()
    while len(heap) != 0:
        cost, cur = heapq.heappop(heap)
        if cur not in visited:
            visited.add(cur)
            for key in graph[cur].keys():
                temp = cost + graph[cur][key]
                if temp < dist[key]:
                    dist[key] = temp
                    heapq.heappush(heap, (dist[key], key))
    return dist


if __name__ == '__main__':
    read = stdin.readline
    n, m, x =map(int, read().rstrip().split())
    graph = [{} for _ in range(n+1)]
    for _ in range(m):
        frm, to, weight = map(int, read().rstrip().split())
        graph[frm][to] = weight
    
    ans = 0
    dist_x = dijk(graph, x, n)
    for i in range(1, n+1):
        ans = max(ans, dijk(graph, i, n)[x] + dist_x[i])
    print(ans)