from sys import stdin
from collections import deque

def bfs(n, k):
    que = deque([(n)])
    time = [-1] * 100001
    time[n] = 0
    while len(que) != 0:
        cur = que.popleft()
        if cur == k: return time[k]
        for i, next in enumerate([cur*2, cur-1, cur+1]):
            if 0 <= next <= 100000 and time[next] == -1:                
                time[next] = time[cur] if i == 0 else time[cur] + 1
                que.append(next)


if __name__ == '__main__':
    read = stdin.readline
    n, k  = map(int, read().rstrip().split())
    print(bfs(n, k))