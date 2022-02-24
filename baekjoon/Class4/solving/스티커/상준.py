from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        n = int(read().rstrip())
        sticker = [[0] + list(map(int, read().rstrip().split())) for _ in range(2)]
        dp = [[0]*(n+1) for _ in range(2)]
        dp[0][1], dp[1][1] = sticker[0][1], sticker[1][1]
        for i in range(2, n+1):
            dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
        print(max(dp[0][n], dp[1][n]))