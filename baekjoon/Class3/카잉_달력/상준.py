from sys import stdin
import math

if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        m, n, x, y = map(int, read().rstrip().split())
        lcm = math.lcm(m, n)
        ans = x
        while True:
            if ans > lcm: break
            if ans % n == y or (ans % n == 0 and n == y): break
            else: ans += m
        print(ans if ans <= lcm else -1)