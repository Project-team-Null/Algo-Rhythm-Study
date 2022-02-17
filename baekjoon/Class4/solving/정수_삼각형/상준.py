from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    dp = [0] * (n+1)
    dp[0] = int(read().rstrip())
    for _ in range(n-1):
        temp = list(map(int, read().rstrip().split()))
        for i in range(len(temp)-1, -1, -1):
            if i == len(temp)-1: dp[i] = dp[i-1] + temp[i]
            elif i == 0: dp[i] = dp[i] + temp[i]
            else:
                dp[i] = temp[i] + max(dp[i-1], dp[i])
    print(max(dp))