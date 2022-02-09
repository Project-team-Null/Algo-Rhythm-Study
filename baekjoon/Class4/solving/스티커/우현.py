from sys import stdin
read = stdin.readline


def solution():
    n = int(read())
    top = list(map(int, read().split()))
    bot = list(map(int, read().split()))
    dp = [(0, 0)] * n
    dp[0] = (top[0], bot[0])
    for i in range(1, n):
        dp_top = max(top[i] + dp[i - 1][1], dp[i - 1][0])
        dp_bot = max(bot[i] + dp[i - 1][0], dp[i - 1][1])
        dp[i] = (dp_top, dp_bot)
    return max(dp[-1])


if __name__ == "__main__":
    t = int(read())
    for _ in range(t):
        print(solution())
