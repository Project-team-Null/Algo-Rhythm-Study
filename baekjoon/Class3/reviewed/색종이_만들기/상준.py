from sys import stdin
from collections import deque

def same_color(paper, y, x, n):
    temp = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            temp += paper[i][j]
    if temp == n**2: return 1
    elif temp == 0: return 0
    else: return -1


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, read().rstrip().split())))

    stk = deque()
    stk.append([(0,0), n])
    white, blue = 0, 0
    while len(stk) != 0:
        pos, leng = stk.pop()
        check = same_color(paper, pos[0], pos[1], leng)
        if check == 1: blue += 1
        elif check == 0: white += 1
        else:
            stk.append([(pos[0], pos[1]), leng//2])
            stk.append([(pos[0], pos[1] + leng//2), leng//2])
            stk.append([(pos[0] + leng//2, pos[1]), leng//2])
            stk.append([(pos[0] + leng//2, pos[1] + leng//2), leng//2])
    print(white)
    print(blue)