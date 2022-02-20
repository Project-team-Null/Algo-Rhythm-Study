from sys import stdin

def dfs(graph, start, r):
    node = 0
    visited = set()
    stk = [(start,0)]
    while len(stk) != 0:
        cur, dist = stk.pop()
        if cur not in visited:
            visited.add(cur)
            if dist > r:
                r = dist
                node = cur
            for next in graph[cur].keys():
                stk.append((next, dist+graph[cur][next]))
    return node, r


if __name__ == '__main__':
    read = stdin.readline
    v = int(read().rstrip())
    graph = [{} for _ in range(v+1)]
    for _ in range(v):
        info = list(map(int, read().rstrip().split()))[:-1]
        for i in range(1, len(info), 2):
            graph[info[0]][info[i]] = info[i+1]
    
    node, r = dfs(graph, 1, 0)
    print(dfs(graph, node, r)[1])