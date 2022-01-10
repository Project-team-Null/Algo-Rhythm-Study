if __name__ == '__main__':
    lst = []
    len = 0
    arr = [[]]
    
    while 1:
        lst = list(map(int,input().split()))
        if lst[0] == 0: break
        arr.append(lst)
        len += 1
    
    for i in range(1, len + 1):
        arrsum = 0
        long = max(arr[i])
        for j in range(3):
            arrsum += arr[i][j]**2
        if arrsum - 2 * long**2 == 0:
            print("right")
        else:
            print("wrong")
        