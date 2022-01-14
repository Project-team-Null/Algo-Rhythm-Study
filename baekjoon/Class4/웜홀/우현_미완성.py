from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    tc = int(read())
    for _ in range(tc):
        n, m, w = map(int, read().split())
        graph = {}
        for i in range(n + 1):
            graph[i] = []
        for __ in range(m):
            s, e, t = map(int, read().split())
            graph[s].append((e, t))
            graph[e].append((s, t))
        for __ in range(w):
            s, e, t = map(int, read().split())
            graph[s].append((e, -t))
        print(graph)