from sys import stdin
input = stdin.readline


def solution(board, n):
    max_num = 0
    move_mode = [1, 2, 3, 4]  # top, bottom, left, right

    def move_board(board, mode):
        for i in range(n):
            temp = []
            for j in range(n):
                if board[j][i] != 0:
                    temp.append(board[j][i])
            idx = 0
            while idx < len(temp) - 1:
                if temp[idx] == temp[idx + 1]:
                    temp[idx] *= 2
                    temp[idx + 1] = 0
                    idx += 2
                else:
                    idx += 1
            idx = 0
            for j in range(len(temp)):
                if temp[j] != 0:
                    board[idx][i] = temp[j]
                    idx += 1
            for j in range(idx, n):
                board[j][i] = 0

    def solve(board, t):
        if checker(board) or t == 5:
            return
        for mode in move_mode:
            solve(move_board(board, mode), t + 1)

    return max_num


if __name__ == "__main__":
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
