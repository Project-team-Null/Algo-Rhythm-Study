from sys import stdin
import heapq

def dijk(graph, start, n):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (dist[start], start))
    visited = set()
    while len(heap) != 0:
        cost, cur = heapq.heappop(heap)
        if cur in visited: continue
        visited.add(cur)
        for key in graph[cur].keys():
            temp = cost + graph[cur][key]
            if temp < dist[key]:
                dist[key] = temp
                heapq.heappush(heap, (dist[key], key))
    return dist


if __name__ == '__main__':
    read = stdin.readline
    n, e = map(int, read().rstrip().split())
    graph = [{} for _ in range(n+1)]
    for _ in range(e):
        frm, to, weight = map(int, read().rstrip().split())
        graph[frm][to] = weight
        graph[to][frm] = weight
    v1, v2 = map(int, read().rstrip().split())
    
    ref = dijk(graph, 1, n)
    tmp1 = dijk(graph, v1, n)[v2]
    tmp2 = dijk(graph, v2, n)[n]
    tmp3 = dijk(graph, v1, n)[n]
    ans = tmp1 + min(ref[v1] + tmp2, ref[v2] + tmp3)
    print(-1) if ans == float('inf') else print(ans)