from sys import setrecursionlimit, stdin
setrecursionlimit(10000000)

visit1 = [0 for _ in range(10001)]
visit2 = [0 for _ in range(10001)]
fin = []

def transpose(graph, v):
    t_graph = [[] for _ in range(v+1)]
    for i in range(1, v+1):
        for j in graph[i]:
            t_graph[j].append(i)
    return t_graph


def dfs1(graph, i, v):
    visit1[i] = 1
    for j in graph[i]:
        if not visit1[j]:
            dfs1(graph, j, v)
    fin.append(i)


def dfs2(graph, i, v, temp):
    visit2[i] = 1
    temp.append(i)
    for j in graph[i]:
        if not visit2[j]:
            dfs2(graph, j, v, temp)


if __name__ == '__main__':
    read = stdin.readline
    v, e = map(int, read().split())
    graph = [[] for _ in range(v+1)]
    ans = []
    for _ in range(e):
        frm, to = map(int, read().split())
        graph[frm].append(to)
    
    for i in range(1, v+1):
        if not visit1[i]:
            dfs1(graph, i, v)

    t_graph = transpose(graph, v)
    
    for i in reversed(fin):
        if not visit2[i]:
            temp = []
            dfs2(t_graph, i, v, temp)
            ans.append(sorted(temp))
    
    ans.sort()
    print(len(ans))
    for a in ans:
        print(*a, -1)