from sys import stdin
from collections import deque

def bfs(root, tree, n):
    queue = deque([root])
    visited = [-1] * (n + 1)
    visited[root] = 0
    ret = [root, 0]
    while queue:
        node = queue.popleft()
        for (i, j) in tree[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + j
                queue += [i]
                if ret[1] < visited[i]:
                    ret = [i, visited[i]]
    return ret


if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    
    tree = {}
    for _ in range(n):
        read_arr = list(map(int, read().split()))
        key = read_arr[0]
        tree[key] = []
        idx = 1
        while read_arr[idx] != -1:
            tree[key].append((read_arr[idx], read_arr[idx + 1]))
            idx += 2
    
    node, dist = bfs(1, tree, n)
    node, dist = bfs(node, tree, n)
    print(dist)