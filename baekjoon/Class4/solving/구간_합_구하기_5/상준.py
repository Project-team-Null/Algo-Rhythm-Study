from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().split())
    board = [[0] * (n+1)]
    board_sum = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(n):
        board.append([0] + list(map(int, read().split())))
    for i in range(1, n+1):
        temp = 0
        for j in range(1, n+1):
            temp += board[i][j]
            board_sum[i][j] = board_sum[i-1][j] + temp

    for _ in range(m):
        x1, y1, x2, y2 = map(int, read().split())
        print(board_sum[x2][y2] - board_sum[x2][y1-1] - board_sum[x1-1][y2] + board_sum[x1-1][y1-1])