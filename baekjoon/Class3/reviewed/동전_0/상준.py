from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, k = map(int, read().rstrip().split())
    val = [int(read().rstrip()) for _ in range(n)]
    
    ans = 0
    for i in range(n-1, -1, -1):
        if val[i] > k: continue
        div = k // val[i]
        ans += div
        k -= div * val[i]
    print(ans)