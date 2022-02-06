from sys import stdin
from collections import deque
from collections import defaultdict


def bfs(board, v, k):
    queue = deque([(k, 0)])
    length = [float('inf')] * (v + 1)
    length[k] = 0
    while queue:
        cur_pos, cnt = queue.popleft()
        for pos in board[cur_pos]:
            w = board[cur_pos][pos]
            if cnt + w < length[pos]:
                length[pos] = cnt + w
                queue.append((pos, length[pos]))
    return length[1:]


if __name__ == "__main__":
    read = stdin.readline
    v, e = map(int, read().split())
    k = int(read())
    board = defaultdict(lambda: defaultdict(lambda: 11))
    for _ in range(e):
        n_from, n_to, w = map(int, read().split())
        board[n_from][n_to] = min(board[n_from][n_to], w)
    for i in bfs(board, v, k):
        print(i)
