
import sys
from collections import defaultdict

input = sys.stdin.readline


def solution(computers):

    visited = set([1])

    def dfs(start):
        # if start in visited:
        #     return
        for computer in computers[start]:
            if computer not in visited:
                visited.add(computer)
                dfs(computer)

    dfs(1)
    return len(visited) - 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    computers = defaultdict(list)

    for _ in range(m):
        start, end = map(int, input().split())
        computers[start].append(end)
        computers[end].append(start)

    print(solution(computers))
