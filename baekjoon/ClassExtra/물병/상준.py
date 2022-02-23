from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, k = map(int, read().rstrip().split())
    ans = 0
    while bin(n).count('1') > k:
        n += 1
        ans += 1
    print(ans)