from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    a, b, c = map(int, read().rstrip().split())
    dp = [[0, 0] for _ in range(33)]
    dp[1] = [a % c, 1]
    for i in range(2, 33):
        dp[i][0] = dp[i-1][0]**2 % c
        dp[i][1] = dp[i-1][1] * 2
    
    ans = 1
    while True:
        for i in range(33):
            if dp[i][1] <= b: continue
            ans = (ans * dp[i-1][0]) % c
            b -= dp[i-1][1]
            break
        if b == 0: break
    print(ans)