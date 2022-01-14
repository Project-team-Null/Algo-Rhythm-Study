if __name__ == '__main__':
    n = int(input())
    dp = [-1, 0, 1, 1] + [0] * (n - 3)
    for i in range(4, n+1):
        comp = [dp[i-1]]
        if i%3 == 0: comp.append(dp[i//3])
        if i%2 == 0: comp.append(dp[i//2])
        dp[i] = 1 + min(comp)
    print(dp[n])
