from sys import stdin
import heapq

def dijk(graph, start, v):
    dist = [float('inf')] * (v+1)
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
    v, e = map(int, read().rstrip().split())
    graph = [{} for _ in range(v+1)]
    start = int(read().rstrip())
    for _ in range(e):
        frm, to, weight = map(int, read().rstrip().split())
        graph[frm][to] = min(graph[frm].get(to, float('inf')), weight)
    
    ans = dijk(graph, start, v)
    for i in range(1, v+1):
        print('INF') if ans[i] == float('inf') else print(ans[i])