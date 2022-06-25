from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    p = [0] * (n + 2)
    for i in range(n):
        a, b = map(int, read().split())
        p[i] = a
        p[i + 1] = b

    for i in range(1, n):
        for j in range(1, n - i + 1):
            dp[j][j + i] = float('inf')
            for k in range(j, j + i):
                temp = p[j - 1] * p[k] * p[j + i] + dp[j][k] + dp[k + 1][j + i]
                dp[j][j + i] = min(dp[j][j + i], temp)

    print(dp[1][n])
