from sys import stdin

def bellmanford(graph, n):
    dist = [1000000] * (n+1)
    for i in range(n):
        for j in range(1, n+1):
            for next, c in graph[j]:
                temp = dist[j] + c
                if temp < dist[next]:
                    if i == n-1: return True
                    dist[next] = temp
    return False


if __name__ == '__main__':
    read = stdin.readline
    tc = int(read().rstrip())
    for _ in range(tc):
        n, m, w = map(int, read().rstrip().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            s, e, t = map(int, read().rstrip().split())
            graph[s].append((e, t))
            graph[e].append((s, t))
        for _ in range(w):
            s, e, t = map(int, read().rstrip().split())
            graph[s].append((e, -t))
        
        print('YES' if bellmanford(graph, n) else 'NO')