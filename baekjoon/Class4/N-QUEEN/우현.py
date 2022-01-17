def solution(n, col=0, last=list()):
    cnt = 0
    board = [i for i in range(n)]
    
    if col == 0:
        board = [i for i in range(int(n/2))]
    
    for i in range(col):
        if last[i] in board:
            board.remove(last[i])
        if last[i] + (col - i) in board:
            board.remove(last[i] + (col - i))
        if last[i] - (col - i) in board:
            board.remove(last[i] - (col - i))

    if col == n - 1 and board != []:
        return 1
    
    for row in board:
        temp_last = last[:]
        temp_last.append(row)
        cnt += solution(n, col + 1, temp_last)
    
    return cnt


if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    else:
        val = 2 * solution(n)
        if n % 2 == 1:
            val += solution(n, 1, [int(n/2)])
        print(val)
