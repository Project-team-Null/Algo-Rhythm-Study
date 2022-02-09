from sys import stdin
from collections import deque


def solution(dic, n):
    queue = deque()
    visited = set([i for i in range(1, n + 1)])
    cnt = 0
    while visited:
        queue.append(visited.pop())
        while queue:
            node = queue.popleft()
            for i in dic[node]:
                if i in visited:
                    visited.remove(i)
                    queue.append(i)
        cnt += 1
    return cnt


if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    dic = {}
    for i in range(1, n + 1):
        dic[i] = []
    for _ in range(m):
        from_n, to_n = map(int, read().split())
        dic[from_n].append(to_n)
        dic[to_n].append(from_n)

    print(solution(dic, n))
