from sys import stdin

def solution(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i in [1, 2]:
            dp[i] = i
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] += dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    for _ in range(n):
        print(solution(int(read())))