if __name__ == '__main__':
    n, r, c = map(int, input().split())
    arr = [0 for _ in range(n + 1)]
    i = 0
    num = n
    
    while n:
        r -= 2**(n - 1)
        c -= 2**(n - 1)
        n -= 1
        if r >= 0 and c >= 0:
            arr[i] = 3
        elif r >= 0 and c < 0:
            arr[i] = 2
            c += 2**n
        elif r < 0 and c >= 0:
            arr[i] = 1
            r += 2**n
        else:
            arr[i] = 0
            r += 2**n
            c += 2**n
        i += 1
            
    cnt = 0

    for i in range(num):
        cnt += pow(4, num - i - 1) * arr[i]
    
    print(cnt)
