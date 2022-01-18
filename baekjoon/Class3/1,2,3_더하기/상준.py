def solve(n):
    dp = [1, 2, 4]
    for i in range(3, n):
        temp = dp[i-1] + dp[i-2] + dp[i-3]
        dp.append(temp)
    return dp[n-1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))