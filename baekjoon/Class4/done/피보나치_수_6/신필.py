
def solution1(n):  # 음수,제곱계산으로 수가 틀리는듯
    sqrt5 = 5 ** (1 / 2)
    ans = 1 / sqrt5 * (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n)
    return int(ans) % 1000000007


def calc_2x2_matrix(a, b):
    mod = 1000000007
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= mod
    return result


def solution2(n):
    result = [[1, 0], [0, 1]]  # 초기화
    tmp = [[1, 1], [1, 0]]  # base
    k = 0

    while 2 ** k <= n:
        if n & (1 << k) != 0:  # n이 2^k을 포함하는지 판별
            result = calc_2x2_matrix(result, tmp)
        tmp = calc_2x2_matrix(tmp, tmp)
        k += 1

    return result[1][0]


if __name__ == "__main__":
    n = int(input())
    print(solution2(n))

# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법
