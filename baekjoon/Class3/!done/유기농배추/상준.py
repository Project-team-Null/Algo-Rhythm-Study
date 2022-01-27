def find_next(field, i, j, m, n):
    ret = []
    for k in range(-1, 2, 2):
        if i+k >= 0 and i+k < n:
            if field[i+k][j]: ret.append((i+k, j))
        if j+k >= 0 and j+k < m: 
            if field[i][j+k]: ret.append((i, j+k))
    return ret


def dfs_field(field, i, j, m, n):
    stack = [(i, j)]
    while len(stack) != 0:
        pos_y, pos_x = stack.pop()
        if field[pos_y][pos_x]:
            field[pos_y][pos_x] = 0
            next = find_next(field, pos_y, pos_x, m, n)
            for child in next:
                stack.append(child)


def solve(field, m, n):
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]:
                dfs_field(field, i, j, m, n)
                count += 1
    return count
            

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        field = [ [0] * (m) for _ in range(n) ]
        for _ in range(k):
            x, y = map(int, input().split())
            field[y][x] = 1
        
        print(solve(field, m, n))