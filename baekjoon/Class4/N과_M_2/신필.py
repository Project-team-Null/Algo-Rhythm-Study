
from itertools import combinations


def solution(n, m):

    def dfs(arr):
        if len(arr) == m:
            print(*arr)
        else:
            for i in range(arr[-1]+1, n+1):
                if i not in arr:
                    dfs(arr + [i])

    for i in range(1, n - m + 2):
        dfs([i])


def solution2(n, m):
    for arr in combinations(range(1, n+1), m):
        print(*arr)


if __name__ == "__main__":
    n, m = map(int, input().split())
    solution2(n, m)
