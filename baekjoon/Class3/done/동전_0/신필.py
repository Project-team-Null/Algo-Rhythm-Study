import sys

input = sys.stdin.readline


def solution(m, arr):
    arr.sort()
    cnt = 0
    while arr:
        cur = arr.pop()
        if cur <= m:
            div, mod = divmod(m, cur)
            m = mod
            cnt += div
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solution(m, arr))
