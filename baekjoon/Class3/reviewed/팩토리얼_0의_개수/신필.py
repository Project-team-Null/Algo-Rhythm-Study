
import math


def solution(n):
    input_v = str(math.factorial(n))
    length = len(input_v)
    i = 1
    while length > i:
        if input_v[-1 * i] != "0":
            return i - 1
        i += 1
    return i - 1


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
