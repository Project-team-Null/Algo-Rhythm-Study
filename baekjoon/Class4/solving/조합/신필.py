

import math


def solution1(n, m):
    return math.comb(n, m)


def solution2(n, m):
    result = n
    m = n - m if m > n // 2 else m
    for i in range(1, m):
        result = result * (n - i) // (i + 1)
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution2(n, m))
