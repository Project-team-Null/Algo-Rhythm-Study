from sys import stdin

def dfs(board, pos, lnth, ans):
    temp = board[pos[0]][pos[1]]
    for i in range(pos[0], pos[0]+lnth):
        for j in range(pos[1], pos[1]+lnth):
            if board[i][j] != temp:
                lnth //= 3
                for k in range(3):
                    for l in range(3):
                        dfs(board, (pos[0] + k*lnth, pos[1] + l*lnth), lnth, ans)
                return
    ans[temp+1] += 1


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    board = [list(map(int, read().rstrip().split())) for _ in range(n)]
    ans = [0, 0, 0]
    dfs(board, (0, 0), n, ans)
    for a in ans:
        print(a)