if __name__ == '__main__':
    n, k = map(int, input().split())
    dp = [0] * 100002
    for i in range(n):
        dp[i] = n - i

    temp = n + 1
    if n % 2 == 0:
        dp[temp] = 1
        temp += 1

    for i in range(temp, 100001, 2):
        dp[i] = 1 + min(dp[i//2], dp[i-1])
        dp[i-1] = min(dp[i]+1, dp[i-1])
        dp[i+1] = dp[i] + 1

    print(dp[k])
