from collections import deque


def solution(n, m, h, arr):
    ripen = []
    adjacency = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    is_in_box = lambda i, j, k: 0 <= i < h and 0 <= j < m and 0 <= k < n

    def bfs():
        que = deque(ripen)
        last_day = 0
        while que:
            c_i, c_j, c_k, cnt = que.popleft()
            for i, j, k in adjacency:
                n_i, n_j, n_k = i + c_i, j + c_j, k + c_k
                if is_in_box(n_i, n_j, n_k) and arr[n_i][n_j][n_k] == 0:
                    arr[n_i][n_j][n_k] = 1
                    que.append((n_i, n_j, n_k, cnt + 1))
                    last_day = max(last_day, cnt + 1)
        return last_day

    def is_all_ripen():
        for i in range(h):
            for j in range(m):
                for k in range(n):
                    if arr[i][j][k] == 0:
                        return False
        return True

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] == 1:
                    ripen.append((i, j, k, 0))

    result = bfs()
    return result if is_all_ripen() else -1


if __name__ == "__main__":
    n, m, h = map(int, input().split())
    arr = []
    for _ in range(h):
        arr.append([list(map(int, input().split())) for _ in range(m)])

    print(solution(n, m, h, arr))
