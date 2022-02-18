from sys import stdin


def matrix_power(mat, n):
    if n <= 1:
        return mat
    elif n % 2 == 0:
        return matrix_power(matrix_multi(mat, mat), n//2)
    else:
        return matrix_multi(matrix_power(mat, n - 1), mat)


def matrix_multi(a, b):
    temp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += a[i][k] * b[k][j]
            temp[i][j] %= 1000000007
    return temp


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    print(matrix_power([[1, 1], [1, 0]], n - 1)[0][0])
