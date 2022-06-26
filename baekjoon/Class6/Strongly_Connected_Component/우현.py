import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

if __name__ == "__main__":
    read = sys.stdin.readline
    v, e = map(int, read().split())

    graph = defaultdict(list)
    t_graph = defaultdict(list)

    for _ in range(e):
        frm, to = map(int, read().split())
        graph[frm].append(to)
        t_graph[to].append(frm)

    for i in range(1, v + 1):
        graph[i].sort()

    visited = set()
    finish_map = dict()
    order_map = dict()
    scc = []
    connections = []
    order = 0

    def dfs(node, finish_check):
        visited.add(node)
        f_graph = graph
        if not finish_check:
            f_graph = t_graph
            scc.append(node)
        for next_node in f_graph[node]:
            if next_node not in visited:
                dfs(next_node, finish_check)
        if finish_check:
            global order
            finish_map[node] = order
            order_map[order] = node
            order += 1

    for node in range(1, v + 1):
        if node not in visited:
            dfs(node, True)

    for i in range(1, v + 1):
        t_graph[i].sort(key=lambda x: -finish_map[x])

    visited.clear()
    cnt = 0

    for node, _ in sorted(finish_map.items(), key=lambda x: -x[1]):
        if node not in visited:
            dfs(node, False)
            connections.append(sorted(scc))
            cnt += 1
            scc = []

    print(cnt)
    for lst in sorted(connections):
        print(" ".join(str(x) for x in lst), -1)
