
def solution(k, n, arr):
    dp = [0]*(k+1)
    for i in range(n):
        w, v = arr[i]
        if w <= k:
            for j in range(k, 0, -1):
                if j + w <= k and dp[j] != 0:
                    dp[j+w] = max(dp[j+w], dp[j] + v)
            dp[w] = max(dp[w], v)

    return max(dp)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        w, v = map(int, input().split())
        arr.append((w, v))
    print(solution(k, n, arr))
