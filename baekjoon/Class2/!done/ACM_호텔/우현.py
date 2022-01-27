if __name__ == '__main__':
    case = int(input())
    
    arr = [[0] for _ in range(case)]
    
    for i in range(case):
        arr[i] = list(map(int,input().split()))
    
    for i in range(case):
        w = arr[i][2]//arr[i][0] + 1
        h = arr[i][2] % arr[i][0]
        if h == 0:
            w -= 1
            h = arr[i][0]
        print(h*100 + w)