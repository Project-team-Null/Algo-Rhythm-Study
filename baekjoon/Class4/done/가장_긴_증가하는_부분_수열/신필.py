
def solution(arr, n):
    dp = [1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(arr, n))
