def queen_attack(pos_y, x, y):
    for j in range(x):
        dx = x - j
        dy = abs(y - pos_y[j])
        if dy == 0 or dx == dy: return True
    return False


def search(pos_y, n, x):
    if x == n: return 1
    to = n
    if x == 0: to = n//2
    ret = 0
    for y in range(to):
        if not queen_attack(pos_y, x, y):
            pos_y[x] = y
            ret += search(pos_y, n, x+1)
    return ret


if __name__ == '__main__':
    n = int(input())
    pos_y = [-1] * n
    if n == 1: print(1)
    elif n % 2 == 0: print(2 * search(pos_y, n, 0))
    else:
        ans = 2 * search(pos_y, n, 0)
        pos_y[0] = n//2
        ans += search(pos_y, n, 1)
        print(ans)