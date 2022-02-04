from sys import stdin
from collections import deque

def get_next(n):
    ret = []
    s = str(n)
    if len(s) != 4: s = "0"*(4-len(s))+s
    ret.append((n*2)%10000)
    ret.append(n-1 if n != 0 else 9999)
    ret.append(int(s[1:]+s[0]))
    ret.append(int(s[-1]+s[:-1]))
    return ret


def bfs(a, b):
    dslr = 'DSLR'
    que = deque([(a, '')])
    visited = set()
    while len(que) != 0:
        n, ans = que.popleft()
        if n == b: return ans
        if n not in visited:
            visited.add(n)
            child = get_next(n)
            for i in range(4):
                que.append((child[i], ans+dslr[i]))


if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        a, b = map(int, read().rstrip().split())
        print(bfs(a, b))