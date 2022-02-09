import sys
input = sys.stdin.readline


def solution(arr):
    dic = {}
    index = 0
    for num in sorted(arr):
        if num not in dic:
            dic[num] = index
            index += 1

    return map(lambda x: dic[x], arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solution(arr))
