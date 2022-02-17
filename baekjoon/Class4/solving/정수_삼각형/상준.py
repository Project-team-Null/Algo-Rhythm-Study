from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    dp = [0] * (n+2)
    for _ in range(n):
        temp = list(map(int, read().rstrip().split()))
        for i in range(len(temp)-1, -1, -1):
            dp[i+1] = temp[i] + max(dp[i], dp[i+1])
    print(max(dp))