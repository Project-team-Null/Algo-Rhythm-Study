def solve(RGB, n):
    dp = [RGB[0]]
    for i in range(1, n):
        r_min = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
        g_min = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
        b_min = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])
        dp.append([r_min, g_min, b_min])

    return dp[n-1]
if __name__ == '__main__':
    n = int(input())
    RGB = []
    for _ in range(n):
        r, g, b = map(int, input().split())
        RGB.append([r, g, b])

    print(min(solve(RGB, n)))