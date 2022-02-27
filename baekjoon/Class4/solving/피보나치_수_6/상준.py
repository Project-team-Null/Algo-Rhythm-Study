from sys import stdin

def matrix_product_2x2(m1, m2):
    ret = [[0, 0], [0, 0]]
    mod = 1000000007
    ret[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % mod
    ret[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % mod
    ret[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % mod
    ret[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % mod
    return ret


def matrix_power(m, n):
    if n == 1: return m
    mid = matrix_power(m, n//2)
    ret = matrix_product_2x2(mid, mid)
    if n % 2 == 0: return ret
    else: return matrix_product_2x2(ret, m)


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    base = [[1, 1],
            [1, 0]]
    print(matrix_power(base, n)[1][0])