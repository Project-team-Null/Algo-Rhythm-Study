import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, b = map(int, input().split())
    arr = []
    for i in range(n):
        arr += list(map(int, input().split()))
    
    mini = min(arr)
    maxi = max(arr)

    ans = float("inf")
    h = 0
    for height in range(mini, maxi + 1):
        req = 0
        cost = 0
        for i in range(n*m):
            gap = height - arr[i]
            req += gap
            if gap < 0: cost -= 2 * gap
            else : cost += gap
        if req > b:
            continue
        if cost <= ans:
            ans = cost
            h = height
    print(ans, h)