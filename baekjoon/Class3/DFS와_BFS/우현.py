from collections import deque

def bfs(root, arr, n):
    queue = deque([root])
    visited = [0 for _ in range(n + 1)]
    visited[root] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, n + 1):
            if not visited[i] and arr[node][i]:
                visited[i] = 1
                queue += [i]
    
def dfs(root, arr, n):
    queue = deque([root])
    visited = [0 for _ in range(n + 1)]
    visited[0] = 1
    while queue:
        node = queue.pop()
        if visited[node]: continue
        visited[node] = 1
        print(node, end=' ')
        for i in range(n):
            if not visited[n - i] and arr[node][n - i]:
                queue += [n - i] 

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        from_node, to_node = map(int, input().split())
        arr[from_node][to_node] = 1
        arr[to_node][from_node] = 1
    dfs(v, arr, n)
    print()
    bfs(v, arr, n)
