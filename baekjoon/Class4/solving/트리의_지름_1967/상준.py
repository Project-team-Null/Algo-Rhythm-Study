from sys import stdin

def dfs(graph, start, rad):
    node = 0
    stk = [(start, 0)]
    visited = set()
    while len(stk) != 0:
        cur, dist = stk.pop()
        if cur not in visited:
            visited.add(cur)
            if dist > rad:
                rad = dist
                node = cur
            for next in graph[cur].keys():
                stk.append((next, graph[cur][next] + dist))
    return node, rad


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    graph = [{} for _ in range(n+1)]
    for _ in range(n-1):
        parent, child, weight = map(int, read().rstrip().split())
        graph[parent][child] = weight
        graph[child][parent] = weight
    
    node, rad = dfs(graph, 1, 0)
    print(dfs(graph, node, rad)[1])