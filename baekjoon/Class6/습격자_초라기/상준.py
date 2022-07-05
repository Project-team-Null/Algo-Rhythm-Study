from sys import stdin

ref = [[0, 4], [0, 3], [1, 3], [1, 2], [2, 3], [3, 3], [4, 2]]

def double_attack(n, w, arr, dp, case):
    if case == 0:
        return min(dp[n-1]) + 2
    elif case == 1:
        if arr[n][0] + arr[n][1] <= w:
            return min(dp[n-1]) + 1
    elif case == 2:
        if arr[n-1][0] + arr[n][0] <= w:
            return min(dp[n-1][0], dp[n-1][3]) + 1
    elif case == 3:
        if arr[n-1][1] + arr[n][1] <= w:
            return min(dp[n-1][0], dp[n-1][2]) + 1
    elif case == 4:
        if arr[n-1][0] + arr[n][0] <= w and arr[n-1][1] + arr[n][1] <= w:
            return dp[n-1][0]
    return float('inf')


def check(arr, iter, frm, to):
    if iter == 0: return True
    if iter == 1 and arr[frm][0] + arr[frm][1] <= w: return True
    if iter == 2 and arr[to][0] + arr[to][1] <= w: return True
    if iter == 3 and arr[frm][0] + arr[frm][1] <= w and arr[to][0] + arr[to][1] <= w: return True
    if iter == 4 and arr[frm][0] + arr[to][0] <= w: return True
    if iter == 5 and arr[frm][1] + arr[to][1] <= w: return True
    if iter == 6 and arr[frm][0] + arr[to][0] <= w and arr[frm][1] + arr[to][1] <= w: return True
    return False


def solve(n, w, arr, iter):
    if check(arr, iter, 0, 1):
        dp = [[float('inf') for _ in range(5)] for _ in range(n)]
        dp[1][ref[iter][0]] = ref[iter][1]

        for i in range(2, n):
            for j in range(5):
                dp[i][j] = double_attack(i, w, arr, dp, j)
        
        if iter == 0 or iter == 2:
            ret = min(dp[n-1])
            if arr[0][0] + arr[n-1][0] <= w and arr[0][1] + arr[n-1][1] <= w: ret = min(ret, dp[n-1][0] - 2)
            if arr[0][1] + arr[n-1][1] <= w: ret = min(ret, dp[n-1][2] - 1, dp[n-1][0] - 1)
            if arr[0][0] + arr[n-1][0] <= w: ret = min(ret, dp[n-1][3] - 1, dp[n-1][0] - 1)
            return ret
        elif iter == 1 or iter == 3 or iter == 6: return min(dp[n-1])
        elif iter == 4:
            ret = min(dp[n-1])
            if arr[0][1] + arr[n-1][1] <= w: ret = min(ret, dp[n-1][0] - 1, dp[n-1][2] - 1)
            return ret
        else: 
            ret = min(dp[n-1])
            if arr[0][0] + arr[n-1][0] <= w: ret = min(ret, dp[n-1][0] - 1, dp[n-1][3] - 1)
            return ret
    return float('inf')


if __name__ == '__main__':
    read = stdin.readline
    t = int(read())
    for _ in range(t):
        n, w = map(int, read().split())
        arr = [list(map(int, read().split())) for _ in range(2)]
        arr = list(map(list, zip(*arr)))
        if n == 1:
            print(1 if sum(*arr) <= w else 2)
            continue
        elif n == 2:
            if arr[0][0] + arr[1][0] <= w and arr[0][1] + arr[1][1] <= w: print(2)
            elif arr[0][0] + arr[0][1] <= w and arr[1][0] + arr[1][1] <= w: print(2)
            elif arr[0][0] + arr[1][0] > w and arr[0][1] + arr[1][1] > w and arr[0][0] + arr[0][1] > w and arr[1][0] + arr[1][1] > w: print(4)
            else: print(3)
        else:
            ans = float('inf')
            for iter in range(7):
                ans = min(ans, solve(n, w, arr, iter))
            print(ans)
