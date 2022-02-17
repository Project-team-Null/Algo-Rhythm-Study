import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline


def solution(nodes, start, v):
    dist = [float('inf')] * (v + 1)

    def dijkstra(start):
        que = [(0, start)]
        dist[start] = 0
        while que:
            cur_w, cur = heapq.heappop(que)
            if dist[cur] >= cur_w:  # 방문한적 있는지
                for frm_w, frm in nodes[cur]:
                    if frm_w + cur_w < dist[frm]:
                        dist[frm] = frm_w + cur_w
                        heapq.heappush(que, (frm_w + cur_w, frm))
    dijkstra(start)
    return list(map(lambda x: x if x != float('inf') else "INF", dist[1:]))


if __name__ == "__main__":
    nodes = defaultdict(list)
    V, E = map(int, input().split())
    start = int(input())
    for i in range(E):
        u, v, w = map(int, input().split())
        nodes[u].append((w, v))
    print(*solution(nodes, start, V), sep='\n')
