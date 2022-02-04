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

if __name__ == '__main__':
    print(get_next(1))