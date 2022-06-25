from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    dp = [0] * n
    dp[0] = 1
    marker = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                marker[i] = j
    lst = []
    max_dp = max(dp)
    idx = dp.index(max_dp)
    print(max_dp)
    while idx != -1:
        lst.append(arr[idx])
        idx = marker[idx]
    for i in range(max_dp - 1, -1, -1):
        print(lst[i], end=' ')
