import sys
input = sys.stdin.readline


def solution(arr, n):
    max_v = 0
    l, r = 1, max(arr)
    while l <= r:
        m = (l + r) // 2
        cnt = 0
        for i in arr:
            cnt += i // m
        if cnt < n:
            r = m - 1
        else:
            max_v = max(max_v, m)
            # 옛날풀이 max_v = m
            l = m + 1

    return max_v


if __name__ == "__main__":
    k, n = map(int, input().split())
    arr = []
    for i in range(k):
        arr.append(int(input()))
    print(solution(arr, n))
