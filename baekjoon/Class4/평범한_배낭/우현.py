from sys import stdin


def solution(lst, k):
    dp = [0] * (k + 1)
    for w, v in lst:
        for i in range(k, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    return dp[-1]


if __name__ == "__main__":
    read = stdin.readline
    n, k = map(int, read().split())
    lst = []
    dp = [0] * (k + 1)
    for i in range(n):
        w, v = map(int, read().split())
        if w <= k:
            lst.append((w, v))
    print(solution(lst, k))
