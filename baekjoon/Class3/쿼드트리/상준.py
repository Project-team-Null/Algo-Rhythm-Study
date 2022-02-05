from sys import stdin
ans = ""

def dfs(board, pos, lnth):
    global ans
    temp = board[pos[0]][pos[1]]
    for i in range(pos[0], pos[0]+lnth):
        for j in range(pos[1], pos[1]+lnth):
            if board[i][j] != temp:
                ans += "("
                lnth //= 2
                for k in range(2):
                    for l in range(2):
                        dfs(board, (pos[0] + k*lnth, pos[1] + l*lnth), lnth)
                ans += ")"
                return
    ans += temp

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    board = [read().rstrip() for _ in range(n)]
    dfs(board, (0,0), n)
    print(ans)