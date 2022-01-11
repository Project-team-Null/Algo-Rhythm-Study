if __name__ == '__main__':
    n = int(input())
    arr = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            arr[i] = 0
        elif i == 2:
            arr[i] = 1
        elif i == 3:
            arr[i] = 1
        else:
            temp = [arr[i - 1] + 1]
            if not i % 2: temp.append(arr[int(i / 2)] + 1)
            if not i % 3: temp.append(arr[int(i / 3)] + 1)
            arr[i] = min(temp)
    print(arr[n])
            