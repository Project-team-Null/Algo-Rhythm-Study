import sys
input = sys.stdin.readline


def solution(arr, n, m, b):
    min_v = 257
    max_v = 0
    result = {}
    for i in arr:
        for j in i:
            min_v = min(min_v, j)
            max_v = max(max_v, j)

    for height in range(min_v, max_v+1):
        case_1 = 0
        case_2 = 0
        for y in arr:
            for x in y:
                if x > height:
                    case_1 += x - height
                elif x < height:
                    case_2 += height - x
        if case_2 <= b + case_1:
            result[case_1 * 2 + case_2] = height
    return min(result.items())


if __name__ == "__main__":
    n, m, b = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    time, height = solution(arr, n, m, b)
    print(time, height)
