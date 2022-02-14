import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(tree, n):
    dist = {}
    max_value = [0, 0]

    def dfs(start):
        nonlocal max_value
        for node, wei in tree[start]:
            if node not in dist:
                dist[node] = wei + dist[start]
                if dist[node] > max_value[1]:
                    max_value = [node, dist[node]]
                dfs(node)

    dist[1] = 0
    dfs(1)
    v = max_value[0]

    dist.clear()
    max_value = [0, 0]

    dist[v] = 0
    dfs(v)

    return max_value[1]


if __name__ == '__main__':
    n = int(input())
    tree = {}
    for i in range(1, n + 1):
        arr = list(map(int, input().split()))
        tree[arr[0]] = []
        for j in range(1, len(arr) - 2, 2):
            tree[arr[0]].append((arr[j], arr[j + 1],))
    print(solution(tree, n))
