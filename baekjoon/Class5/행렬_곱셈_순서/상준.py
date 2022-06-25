from sys import stdin

def get_minimum(n, size):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for r in range(1, n):
        for i in range(1, n-r+1):
            j = i + r
            temp = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + size[i-1]*size[k]*size[j]
                if q < temp: temp = q
            dp[i][j] = temp
    
    return dp[1][n]

if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    size = []
    for i in range(n):
        r, c = map(int, read().split())
        if i == 0:
            size.append(r)
        size.append(c)
    
    print(get_minimum(n, size))