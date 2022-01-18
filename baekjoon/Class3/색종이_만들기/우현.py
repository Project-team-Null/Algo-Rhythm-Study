from sys import stdin
from collections import deque


def is_done(p, n, board):
    temp = board[p[1]][p[0]]
    for i in range(p[0], p[0] + n):
        for j in range(p[1], p[1] + n):
            if board[j][i] != temp:
                return -1
    return 1 if temp == 1 else 0


def solution(board, n):
    white_blue = [0, 0]
    points = deque([(0, 0), (0, n//2), (n//2, 0), (n//2, n//2)])
    length = 4
    while length:
        for _ in range(length):
            p = points.popleft()
            temp = is_done(p, n//2, board)
            if temp == -1:
                points.append(p)
                points.append((p[0], p[1] + n//4))
                points.append((p[0] + n//4, p[1]))
                points.append((p[0] + n//4, p[1] + n//4))
            else:
                white_blue[temp] += 1
        n //= 2
        length = len(points)

    # 모든 색이 같을 경우에 대한 예외처리
    for i in range(2):
        if white_blue[i] == 0 and white_blue[1 - i] != 0:
            white_blue[i] = 0
            white_blue[1 - i] = 1

    return white_blue


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    board = [list(map(int, read().split())) for _ in range(n)]
    ans = solution(board, n)
    print(ans[0], ans[1], sep='\n')
