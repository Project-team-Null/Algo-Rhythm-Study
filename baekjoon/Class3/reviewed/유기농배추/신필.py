
import sys
from collections import deque


def solution(bechu_set):
    result = 0
    UDLR = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def bfs(start_x, start_y):
        que = deque([(start_x, start_y)])
        while que:
            x, y = que.popleft()
            for dir_x, dir_y in UDLR:
                cur_x, cur_y = x + dir_x, y + dir_y
                if (cur_x, cur_y) in bechu_set:
                    bechu_set.remove((cur_x, cur_y))
                    que.append((cur_x, cur_y))

    while bechu_set:
        result += 1
        x, y = bechu_set.pop()
        bfs(x, y)

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        bechu_set = set([])
        for _ in range(k):
            x, y = map(int, input().split())
            bechu_set.add((x, y))
        print(solution(bechu_set))


#### 예전 풀이 (시간 비슷)####
sys.setrecursionlimit(10000)


def dfs(bechu, y, x, i, j):
    if j < 0 or i < 0 or j >= x or i >= y:
        return 0
    if bechu[i][j] == 1:
        bechu[i][j] = 0
        dfs(bechu, y, x, i-1, j)
        dfs(bechu, y, x, i+1, j)
        dfs(bechu, y, x, i, j-1)
        dfs(bechu, y, x, i, j+1)
        return 1
    return 0


def solution2(bechu, x, y):
    cnt = 0
    for i in range(y):
        for j in range(x):
            cnt += dfs(bechu, y, x, i, j)
    return cnt
