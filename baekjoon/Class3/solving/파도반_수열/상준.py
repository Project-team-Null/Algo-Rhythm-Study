from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    dp = [0, 1, 1, 1, 2, 2] + [0]*95
    for i in range(6, 101):
        dp[i] = dp[i-1] + dp[i-5]

    for _ in range(t):
        n = int(read().rstrip())
        print(dp[n])