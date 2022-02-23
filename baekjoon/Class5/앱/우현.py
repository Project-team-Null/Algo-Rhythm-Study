from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    byte = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    sum_cost = sum(cost)
    dp = [0] * (sum_cost + 1)
    maxi = 0
    for i in range(n):
        b = byte[i]
        c = cost[i]
        for j in range(sum_cost, c - 1, -1):
            dp[j] = max(dp[j], dp[j - c] + b)
    for i in range(sum_cost + 1):
        if dp[i] >= m:
            print(i)
            break
