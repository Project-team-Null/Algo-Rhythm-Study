from sys import stdin
from collections import deque

if __name__ == '__main__':
    read = stdin.readline
    k = int(read().rstrip())
    stk = deque()
    for _ in range(k):
        cur = int(read().rstrip())
        if cur == 0:
            stk.pop()
        else:
            stk.append(cur)
    print(sum(stk))