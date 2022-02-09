from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, k = map(int, read().rstrip().split())
    objs = []
    for _ in range(n):
        objs.append(tuple(map(int, read().rstrip().split())))
    
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w, v = objs[i-1]
        for j in range(1, k+1):
            if w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])