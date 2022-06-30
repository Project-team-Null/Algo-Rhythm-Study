import sys

read = sys.stdin.readline

if __name__ == "__main__":
    n = int(read())
    lst = [0] + list(map(int, read().split()))
    m = int(read())

    dp = [[0 for _ in range(n + 2)] for __ in range(n + 2)]

    for idx in range(1, n - 1):
        dp[idx][idx] = 1
        if lst[idx] == lst[idx + 1]:
            dp[idx][idx + 1] = 1
        if lst[idx] == lst[idx + 2]:
            dp[idx][idx + 2] = 1
    dp[n - 1][n - 1] = 1
    dp[n][n] = 1
    if lst[n - 1] == lst[n]:
        dp[n - 1][n] = 1

    for distance in range(3, n):
        for idx in range(1, n - distance + 1):
            if dp[idx + 1][idx + distance - 1] and lst[idx] == lst[idx + distance]:
                dp[idx][idx + distance] = 1

    for _ in range(m):
        s, e = map(int, read().split())
        print(dp[s][e])
