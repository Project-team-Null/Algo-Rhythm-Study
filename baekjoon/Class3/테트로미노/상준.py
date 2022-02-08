from sys import stdin

tetro = [
    # square
    [(0,1), (1,0), (1,1)],
    # long
    [(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    # F U
    [(0,1), (0,2), (1,1)],
    [(0,1), (0,2), (-1,1)],
    [(0,1), (-1,1), (1,1)],
    [(0,1), (-1,0), (1,0)],
    # zigzag
    [(1,0), (1,1), (2,1)],
    [(0,1), (-1,1), (-1,2)],
    [(-1,0), (-1,1), (-2,1)],
    [(0,1), (1,1), (1,2)],
    # L
    [(1,0), (2,0), (2,1)],
    [(0,1), (0,2), (-1,2)],
    [(0,1), (1,1), (2,1)],
    [(1,0), (0,1), (0,2)],
    [(1,0), (2,0), (2,-1)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (1,0), (2,0)],
    [(0,1), (0,2), (1,2)],
]

def get_sum(board, y, x, n, m):
    ret = 0
    for i in range(len(tetro)):
        temp = board[y][x]
        for j in range(3):
            ny = y + tetro[i][j][0]
            nx = x + tetro[i][j][1]
            if 0 <= ny < n and 0 <= nx < m:
                temp += board[ny][nx]
            else: 
                temp = 0
                break
        ret = max(ret, temp)
    return ret

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    board = [list(map(int, read().rstrip().split())) for _ in range(n)]
    
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, get_sum(board, i, j, n, m))
    print(ans)