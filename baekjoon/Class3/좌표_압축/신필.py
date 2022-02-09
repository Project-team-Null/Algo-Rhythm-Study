import sys
input = sys.stdin.readline


def solution(arr, n):
    dic = {}
    index = 0
    for i in sorted(arr):
        if i not in dic:
            dic[i] = index
            index += 1

    return map(lambda x: dic[x], arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solution(arr, n))
