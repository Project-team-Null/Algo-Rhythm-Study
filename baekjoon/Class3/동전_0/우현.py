from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n, k = map(int, read().split())
    lst = [int(read()) for _ in range(n)]

    cnt = 0
    for i in reversed(lst):
        if k >= i:
            cnt += k // i
            k %= i
    print(cnt)
