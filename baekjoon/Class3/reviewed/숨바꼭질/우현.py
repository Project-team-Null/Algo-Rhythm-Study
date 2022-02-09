from sys import stdin
from collections import deque

def solution(n, m):
    # 숫자가 작아지는 쪽으로는 -1밖에 없음
    if n >= m:
        return n - m
    
    # BFS
    queue = deque()
    queue.append((n, 0))
    visited = set()
    visited.add(n)
    while queue:
        node = queue.popleft()
        for i in [node[0] + 1, node[0] - 1, node[0] * 2]:
            if i == m:
                return node[1] + 1
            if i not in visited and i >= 0 and i <= 100000:
                visited.add(i)
                queue.append((i, node[1] + 1))


if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    
    print(solution(n, m))