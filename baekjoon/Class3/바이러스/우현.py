from sys import stdin
from collections import deque

def solution(dic):
    queue = deque([1])
    visited = set()
    visited.add(1)
    while queue:
        node = queue.popleft()
        for i in dic[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                
    return len(visited) - 1


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    m = int(read())
    dic = {}
    for i in range(1, n + 1):
        dic[i] = []
    for i in range(1, m + 1):
        a, b = map(int, read().split())
        dic[a].append(b)
        dic[b].append(a)
    print(solution(dic))