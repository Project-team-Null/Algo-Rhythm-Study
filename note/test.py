from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    arr = [i+1 for i in range(n)]
    start = 0
    while arr[start] != arr[-1]:
        arr.append(arr[start+1])
        start += 2
    print(arr[start])