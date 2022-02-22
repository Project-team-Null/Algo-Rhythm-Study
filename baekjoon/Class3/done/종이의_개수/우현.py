from sys import stdin


# BFS로 해결 시 메모리초과 -> DFS로 해결
def solution(board, n):
    lst = [(0, 0, n)]
    cnt = [0, 0, 0]
    length = len(lst)

    def check(i, j, n):
        temp = board[i][j]
        for row in range(n):
            for col in range(n):
                if board[i + row][j + col] != temp:
                    return 2
        return temp

    def divider(i, j, n):
        temp = []
        for row in range(3):
            for col in range(3):
                temp.append((i + row * n // 3, j + col * n // 3, n // 3))
        return temp

    while lst:
        i, j, size = lst.pop()
        temp = check(i, j, size)
        if -1 <= temp <= 1:
            cnt[temp + 1] += 1
        else:
            lst += divider(i, j, size)
    return cnt


if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    board = []
    for i in range(n):
        board.append(list(map(int, read().split())))
    print(*solution(board, n), sep='\n')
