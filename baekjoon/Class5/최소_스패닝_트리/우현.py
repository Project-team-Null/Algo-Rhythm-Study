from sys import stdin
import heapq


def mst_prim(v, graph):
    start_node = 1
    weight_list = [float('inf')] * (v + 1)
    heap = [(0, start_node)]
    weight_list[start_node] = 0
    visited = set()
    while heap:
        w, cur_node = heapq.heappop(heap)
        visited.add(cur_node)
        if w > weight_list[cur_node]:
            continue
        for next_node, next_w in graph[cur_node].items():
            if next_w < weight_list[next_node] and next_node not in visited:
                weight_list[next_node] = next_w
                heapq.heappush(heap, (next_w, next_node))
    return sum(weight_list[1:])


if __name__ == "__main__":
    read = stdin.readline
    v, e = map(int, read().split())
    graph = [dict() for _ in range(v + 1)]
    for _ in range(e):
        frm, to, w = map(int, read().split())
        graph[frm][to] = min(graph[frm].get(to, float('inf')), w)
        graph[to][frm] = graph[frm][to]

    print(mst_prim(v, graph))
