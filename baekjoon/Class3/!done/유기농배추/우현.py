def bfs(x, y, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and board[q][w] == 1:
                board[q][w] = 0
                queue.append([q, w])
                
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, n, k = map(int, input().split())
        board = [[0] * m for i in range(n)]
        cnt = 0
        for j in range(k):
            a, b = map(int, input().split())
            board[b][a] = 1
        for q in range(n):
            for w in range(m):
                if board[q][w] == 1:
                    board[q][w] = 0
                    bfs(q, w, board)
                    cnt += 1
        print(cnt)