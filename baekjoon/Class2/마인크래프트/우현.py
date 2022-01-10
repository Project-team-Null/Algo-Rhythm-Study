if __name__ == '__main__':
    n, m, inv = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))    
    arr = sum(arr, [])

    tot = sum(arr)
    
    height = [i for i in range(min(arr), max(arr) + 1)]
    minc = float('inf')

    ret = (0, 0)
    for k in height:
        cost = 0
        if tot + inv < k * n * m:
            continue
        for i in range(n * m):
            gap = arr[i] - k
            if gap > 0:
                cost += 2 * gap
            else:
                cost -= gap
        if cost <= minc:
            minc = cost
            ret = (cost, k)
    
    print(ret[0], ret[1])