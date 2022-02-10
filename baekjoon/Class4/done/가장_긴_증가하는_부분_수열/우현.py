from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        temp = set([1])
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                temp.add(dp[j] + 1)
        dp[i] = max(temp)
    print(max(dp))
