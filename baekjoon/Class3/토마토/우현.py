from sys import stdin
from collections import deque


def solution(board, n, m):
    queue = deque()
    visited = set()
    tot = [0, 0]

    for j in range(m):
        for i in range(n):
            if board[j][i] == 1:
                queue.append((i, j))
                visited.add((i, j))
                tot[1] += 1
            elif board[j][i] == 0:
                tot[0] += 1

    cost = 0
    length = len(queue)

    while length:
        for _ in range(length):
            pos = queue.popleft()
            for x, y in neighbor(pos, n, m):
                if (x, y) not in visited and board[y][x] == 0:
                    visited.add((x, y))
                    queue.append((x, y))
        cost += 1
        length = len(queue)

    return -1 if len(visited) != sum(tot) else cost - 1


def neighbor(pos, n, m):
    lst = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        px = pos[0] + dx[i]
        py = pos[1] + dy[i]
        if 0 <= px < n and 0 <= py < m:
            lst.append((px, py))
    return lst


if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    board = [[] for _ in range(m)]
    for i in range(m):
        board[i] = list(map(int, read().split()))

    print(solution(board, n, m))
