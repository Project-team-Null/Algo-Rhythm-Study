
def solution(lst, k):
    dp = [0] * (k + 1)
    for w, v in lst:
        for i in range(k, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    return dp[-1]


if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = []
    dp = [0] * (k + 1)
    for i in range(n):
        w, v = map(int, input().split())
        if w <= k:
            lst.append((w, v))
    print(solution(lst, k))
