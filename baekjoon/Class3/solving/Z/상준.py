from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, r, c = map(int, read().rstrip().split())
    ans = 0
    while n > 0:
        quad = 0
        if c >= 2**(n-1):
            quad += 1
            c -= 2**(n-1)
        if r >= 2**(n-1):
            quad += 2
            r -= 2**(n-1)
        ans += 2**(2*n-2) * quad
        n -= 1
    print(ans)