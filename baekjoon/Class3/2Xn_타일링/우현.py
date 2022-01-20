from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    dp = [0] * (n + 4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    for i in range(5, n + 1):
        if i % 2 == 1:
            dp[i] = dp[i - 1] * 2 - 1
        else:
            dp[i] = dp[i - 2] * 5 - 3
    print(dp[n])
