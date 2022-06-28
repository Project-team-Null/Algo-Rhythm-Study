from sys import stdin

def get_palindrome(seq, dp):
    for i in range(1, n+1):
        dp[i][i] = 1
        if i < n and seq[i] == seq[i+1]:
            dp[i][i+1] = 1

    for r in range(2, n):
        for i in range(1, n-r+1):
            j = i + r
            if seq[i] == seq[j] and dp[i+1][j-1]:
                dp[i][j] = 1


if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    seq = [0] + list(map(int, read().split()))
    
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    get_palindrome(seq, dp)

    m = int(read())
    for _ in range(m):
        frm, to = map(int, read().split())
        print(dp[frm][to])