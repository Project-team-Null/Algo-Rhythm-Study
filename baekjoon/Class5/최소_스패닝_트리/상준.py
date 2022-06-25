from sys import stdin
from heapq import heappush, heappop

def prim(graph, v):
    visited = set([1])
    heap = []
    for next in graph[1]:
        heappush(heap, next)
    ans = 0
    
    while len(visited) != v:
        w, cur = heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        ans += w
        for next in graph[cur]:
            heappush(heap, next)
    
    return ans


if __name__ == '__main__':
    read = stdin.readline
    v, e = map(int, read().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        frm, to, w = map(int, read().split())
        graph[frm].append((w, to))
        graph[to].append((w, frm))
    
    print(prim(graph, v))