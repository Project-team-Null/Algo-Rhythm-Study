def solve(R, G, B, n):
    dp = [[R[0], G[0], B[0]]]
    for i in range(1, n):
        r_min = min(R[i] + dp[i-1][1], R[i] + dp[i-1][2])
        g_min = min(G[i] + dp[i-1][0], G[i] + dp[i-1][2])
        b_min = min(B[i] + dp[i-1][0], B[i] + dp[i-1][1])
        dp.append([r_min, g_min, b_min])

    return dp[n-1]
if __name__ == '__main__':
    n = int(input())
    R, G, B = [], [], []
    for _ in range(n):
        r, g, b = map(int, input().split())
        R.append(r)
        G.append(g)
        B.append(b)

    print(min(solve(R, G, B, n)))