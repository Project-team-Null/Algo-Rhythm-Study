from sys import stdin
import math


def solution_bt(arr, n):
    # Using Back tracking, for Pypy3 only
    length = sum(arr) // n
    while True:
        cnt = 0
        maxi = -1
        next_len = 0
        for val in arr:
            cnt += val // length
            next_len = val // ((val // length) + 1)
            if next_len > maxi:
                maxi = next_len
            if cnt >= n:
                return length
        length = maxi


def solution_bs(arr, n):
    # Using Binary search, for python3
    max_length = sum(arr) // n
    length = max_length
    visited = set()
    m = int(math.log2(length)) + 2
    temp = max_length
    for _ in range(m):
        cnt = 0
        visited.add(length)
        for val in arr:
            cnt += val // length
        if temp % 2 == 1:
            temp += 1
        temp //= 2
        if cnt >= n:
            if length + 1 in visited:
                return length
            length += temp
        else:
            length -= temp
    return length


if __name__ == "__main__":
    read = stdin.readline
    k, n = map(int, read().split())
    arr = [0] * k
    for i in range(k):
        arr[i] = int(read())
    print(solution_bs(arr, n))
