from sys import stdin


def read(): return map(int, stdin.readline().split())


if __name__ == '__main__':
    n, m = read()
    dp = [[0] for _ in range(n + 1)]
    dp[0] = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] += list(read())

    for row in range(n + 1):
        for col in range(1, n + 1):
            dp[row][col] += dp[row][col - 1]
    for col in range(n + 1):
        for row in range(1, n + 1):
            dp[row][col] += dp[row - 1][col]

    for i in range(m):
        row1, col1, row2, col2 = read()
        print(dp[row2][col2] - dp[row2][col1 - 1] -
              dp[row1 - 1][col2] + dp[row1 - 1][col1 - 1])
