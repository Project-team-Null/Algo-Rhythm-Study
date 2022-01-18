if __name__ == '__main__':
    n, k = map(int, input().split())
    dp = [0] * 100002
    for i in range(n-1, -1, -1):
        dp[i] = dp[i+1] + 1

    if n%2 == 0:
        dp[n+1] = 1
        for i in range(n+2, 100001, 2):
            dp[i] = 1 + min(dp[i//2], dp[i-1])
            dp[i-1] = min(dp[i]+1, dp[i-1])
            dp[i+1] = dp[i] + 1
    else:
        for i in range(n+1, 100001, 2):
            dp[i] = 1 + min(dp[i//2], dp[i-1])
            dp[i-1] = min(dp[i]+1, dp[i-1])
            dp[i+1] = dp[i] + 1

    print(dp[k])