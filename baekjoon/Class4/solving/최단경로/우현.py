from sys import stdin
from collections import defaultdict
import heapq


def dijkstra(board, v, k):
    heap = []
    distance = [float('inf')] * (v + 1)
    distance[k] = 0
    heapq.heappush(heap, (0, k))
    while heap:
        dist, current = heapq.heappop(heap)
        if dist > distance[current]:
            continue
        for next_node, w in board[current].items():
            temp = distance[current] + w
            if temp < distance[next_node]:
                distance[next_node] = temp
                heapq.heappush(heap, (temp, next_node))
    return distance[1:]


if __name__ == "__main__":
    read = stdin.readline
    v, e = map(int, read().split())
    k = int(read())
    board = defaultdict(lambda: defaultdict(lambda: 11))
    for _ in range(e):
        n_from, n_to, w = map(int, read().split())
        board[n_from][n_to] = min(board[n_from][n_to], w)
    for i in dijkstra(board, v, k):
        if i == float('inf'):
            print("INF")
        else:
            print(i)
