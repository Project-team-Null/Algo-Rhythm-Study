import sys

input = sys.stdin.readline


def solution(n, arr):
    result = [0, 0, 0]

    def r_search(start, size):
        s_x, s_y = start
        if size == 1:
            result[arr[s_y][s_x] + 1] += 1
            return

        for y in range(s_y, s_y + size):
            for x in range(s_x, s_x + size):
                if arr[y][x] != arr[s_y][s_x]:
                    n_size = size // 3
                    for i in range(s_y, s_y + size, n_size):
                        for j in range(s_x, s_x + size, n_size):
                            r_search((j, i), n_size)
                    return

        result[arr[s_y][s_x] + 1] += 1

    r_search((0, 0), n)
    return result


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    print(*solution(n, arr), sep='\n')
