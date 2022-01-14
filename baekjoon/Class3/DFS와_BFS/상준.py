from queue import Queue

def dfs(graph, n, v):
    for i in range(n+1):
        graph[i].sort(reverse=True)

    stack = [v]
    visited = set()
    ans = []
    while (len(stack) != 0):
        cur = stack.pop()
        if cur not in visited:
            ans.append(cur)
            visited.add(cur)
            for child in graph[cur]:
                stack.append(child)
    return ans

def bfs(graph, n, v):
    for i in range(n+1):
        graph[i].sort()

    que = Queue()
    que.put(v)
    visited = set()
    ans = []
    while(que.qsize() != 0):
        cur = que.get()
        if cur not in visited:
            ans.append(cur)
            visited.add(cur)
            for child in graph[cur]:
                que.put(child)
    return ans

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [ [] for _ in range(n + 1) ]
    for _ in range(m):
        frm, to = map(int, input().split())
        graph[frm].append(to)
        graph[to].append(frm)

    print(" ".join(map(str, dfs(graph, n, v))))
    print(" ".join(map(str, bfs(graph, n, v))))