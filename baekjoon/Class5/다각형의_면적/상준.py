from sys import stdin

def integral(x1, y1, x2, y2):
    base = x2 - x1
    if (y1 * y2 >= 0):
        return 0.5 * (y1 + y2) * base
    elif y1 == y2:
        return base * y1
    else:
        denom = abs(y1) + abs(y2)
        return 0.5 * base * abs(y1/denom) * y1 + 0.5 * base * abs(y2/denom) * y2

if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    area = 0
    x1, y1 = map(int, read().split())
    x0, y0 = x1, y1
    for i in range(n):
        x2, y2 = map(int, read().split()) if i != n-1 else (x0, y0)
        area += integral(x1, y1, x2, y2)
        x1, y1 = x2, y2
    
    print("%.1f" % abs(area))