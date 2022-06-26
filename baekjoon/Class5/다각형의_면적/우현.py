from sys import stdin
read = stdin.readline


def integral(x1, y1, x2, y2):
    base = x2 - x1
    if y1 == y2:
        return base * y1
    if y1*y2 >= 0:
        return base * (y1 + y2) / 2
    else:
        denom = abs(y1) + abs(y2)
        area = 0.5 * base * abs(y1 / denom) * y1 + 0.5 * \
            base * abs(y2 / denom) * y2
        return area


if __name__ == "__main__":
    n = int(read())
    sum = 0
    x1, y1 = map(int, read().split())
    x0, y0 = x1, y1
    for _ in range(n - 1):
        x2, y2 = map(int, read().split())
        sum += integral(x1, y1, x2, y2)
        x1, y1 = x2, y2
    sum += integral(x1, y1, x0, y0)

    if sum < 0:
        sum *= -1

    print("%.1f" % sum)
