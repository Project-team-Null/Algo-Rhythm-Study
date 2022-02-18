from collections import defaultdict


def floydWarshall(graph, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if j == k:
                    graph[j][k] = 0
                    continue
                temp = graph[j][i] + graph[i][k]
                if graph[j][k] > temp:
                    graph[j][k] = temp
    return


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a][b] = min(graph[a][b], w)
    floydWarshall(graph, n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j] if graph[i][j] != float('inf') else 0, end=' ')
        print()
