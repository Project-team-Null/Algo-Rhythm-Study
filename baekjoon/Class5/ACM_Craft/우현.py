from collections import defaultdict
from collections import deque
from sys import stdin
input = stdin.readline


def solution():
    n, k = map(int, input().split())
    cost_origin = [0] + list(map(int, input().split()))
    cost_dp = [0] * (n + 1)
    check = [0] * (n + 1)
    tree = defaultdict(list)

    for i in range(k):
        x, y = map(int, input().split())
        tree[x].append(y)
        check[y] += 1

    queue = deque()
    for i in range(1, n + 1):
        if check[i] == 0:
            cost_dp[i] = cost_origin[i]
            queue.append(i)

    while queue:
        node = queue.popleft()
        for next_node in tree[node]:
            check[next_node] -= 1
            cost_dp[next_node] = max(
                cost_dp[next_node], cost_dp[node] + cost_origin[next_node])
            if check[next_node] == 0:
                queue.append(next_node)

    w = int(input())
    return cost_dp[w]


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        print(solution())
