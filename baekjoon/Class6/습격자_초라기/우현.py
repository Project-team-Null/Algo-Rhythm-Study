import sys


def solution(board, n, w):
    init_check = (board[0][0] + board[1][0] <= w)

    if n == 1:
        if init_check:
            return 1
        else:
            return 2

    if n == 2:
        if board[0][0] + board[1][0] <= w and board[0][1] + board[1][1] <= w:
            return 2
        if board[1][1] + board[1][0] <= w and board[0][0] + board[0][1] <= w:
            return 2
        if board[0][0] + board[1][0] <= w and board[0][1] + board[1][1] > w:
            return 3
        if board[0][0] + board[1][0] > w and board[0][1] + board[1][1] <= w:
            return 3
        if board[1][1] + board[1][0] <= w and board[0][0] + board[0][1] > w:
            return 3
        if board[1][1] + board[1][0] > w and board[0][0] + board[0][1] <= w:
            return 3
        return 4

    dp = [[(float('inf'), -1) for _ in range(5)] for __ in range(n)]

    if init_check:
        dp[1][0] = (3, 4)
    else:
        dp[1][0] = (4, 0)
    check_0, check_1 = False, False
    if board[0][0] + board[0][1] <= w:
        check_0 = True
        dp[1][1] = (3, 1)
    if board[1][0] + board[1][1] <= w:
        check_1 = True
        dp[1][2] = (3, 2)
    if check_0 and check_1:
        dp[1][3] = (2, 3)
    if board[0][1] + board[1][1] <= w:
        if init_check:
            dp[1][4] = (2, 4)
        else:
            dp[1][4] = (3, 0)

    for i in range(2, n):
        v, m = min(dp[i - 1])
        dp[i][0] = (v + 2, m)
        check_0, check_1 = False, False
        if board[0][i - 1] + board[0][i] <= w:
            check_0 = True
            v, m = min(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = (v + 1, m)
        if board[1][i - 1] + board[1][i] <= w:
            check_1 = True
            v, m = min(dp[i - 1][0], dp[i - 1][1])
            dp[i][2] = (v + 1, m)
        if check_0 and check_1:
            dp[i][3] = dp[i][0]
        if board[0][i] + board[1][i] <= w:
            v, m = min(dp[i - 1])
            dp[i][4] = (v + 1, m)

    if board[0][n - 1] + board[0][0] <= w:
        if dp[n - 1][0][1] == 0 or dp[n - 1][0][1] == 2:
            dp[n - 1][0] = (dp[n - 1][0][0] - 1, 0)
        if dp[n - 1][2][1] == 0 or dp[n - 1][2][1] == 2:
            dp[n - 1][2] = (dp[n - 1][2][0] - 1, 0)
    if board[1][n - 1] + board[1][0] <= w:
        if dp[n - 1][0][1] == 0 or dp[n - 1][0][1] == 1:
            dp[n - 1][0] = (dp[n - 1][0][0] - 1, 0)
        if dp[n - 1][1][1] == 0 or dp[n - 1][1][1] == 1:
            dp[n - 1][1] = (dp[n - 1][1][0] - 1, 0)

    return min(dp[n - 1])[0]


if __name__ == "__main__":
    read = sys.stdin.readline
    t = int(read())
    for case in range(t):
        n, w = map(int, read().split())
        board = [[0 for _ in range(n)] for __ in range(2)]
        board[0] = list(map(int, read().split()))
        board[1] = list(map(int, read().split()))
        print(solution(board, n, w))
