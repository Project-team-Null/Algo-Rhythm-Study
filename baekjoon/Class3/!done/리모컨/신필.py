
def is_able(str_n, arr):
    for j in arr:
        if j in str_n:
            return False
    return True


def solution(arr, n):
    min_cnt = abs(100 - n)
    for i in range(1000000):
        if is_able(str(i), arr):
            min_cnt = min(min_cnt, len(str(i)) + abs(n-i))
    return min_cnt


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    arr = []
    if m != 0:
        arr = input().split()
    print(solution(arr, n))
