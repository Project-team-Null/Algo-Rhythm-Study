from sys import stdin

def solve(n, w, arr, dp):
    for i in range(2, n+1):
        inner = 2 - (arr[i-1][0] + arr[i][0] <= w)
        outer = 2 - (arr[i-1][1] + arr[i][1] <= w)
        cross = 2 - (arr[ i ][0] + arr[i][1] <= w)

        dp[i][0] = min(dp[i-1][2] + 1, dp[i-1][1] + inner)
        dp[i][1] = min(dp[i-1][2] + 1, dp[i-1][0] + outer)
        dp[i][2] = min(dp[i][0] + 1, dp[i][1] + 1, dp[i-1][2] + cross, dp[i-2][2] + inner + outer)


if __name__ == '__main__':
    read = stdin.readline
    t = int(input())
    for _ in range(t):
        n, w = map(int, read().split())
        arr = [list(map(int, read().split())) for _ in range(2)]
        arr = [[0,0]] + list(map(list, zip(*arr)))
        dp = [[0 for _ in range(3)] for _ in range(n+1)]
        ans = float('inf')

        if n == 1:
            print(1 if sum(arr[1]) <= w else 2)
            continue

        dp[1][0] = dp[1][1] = 1
        dp[1][2] = 2 - (arr[1][0] + arr[1][1] <= w)
        solve(n, w, arr, dp)
        ans = min(ans, dp[n][2])

        dp[0][2] = float('inf')
        if arr[n][0] + arr[1][0] <= w:
            dp[1][0] = 1
            dp[1][1] = float('inf')
            dp[1][2] = 2
            solve(n, w, arr, dp)
            ans = min(ans, dp[n][1])

        if arr[n][1] + arr[1][1] <= w:
            dp[1][0] = float('inf')
            dp[1][1] = 1
            dp[1][2] = 2
            solve(n, w, arr, dp)
            ans = min(ans, dp[n][0])

        if arr[n][0] + arr[1][0] <= w and arr[n][1] + arr[1][1] <= w:
            dp[1][0] = dp[1][1] = float('inf')
            dp[1][2] = 2
            solve(n, w, arr, dp)
            ans = min(ans, dp[n-1][2])

        print(ans)