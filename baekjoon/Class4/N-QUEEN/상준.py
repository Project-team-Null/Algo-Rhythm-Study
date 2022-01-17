def queen_attack(pos_y, x, y):
    if x == 0: return False
    for j in range(x):
        dx = x - j
        dy = abs(y - pos_y[j])
        if dy == 0 or dx == dy: return True
    return False


def search(pos_y, n, x):
    if x == n: return 1
    ret = 0
    for y in range(n):
        if not queen_attack(pos_y, x, y):
            pos_y[x] = y
            ret += search(pos_y, n, x+1)
    return ret


if __name__ == '__main__':
    n = int(input())
    pos_y = [-1] * n
    print(search(pos_y, n, 0))