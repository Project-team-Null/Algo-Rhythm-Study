from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    arr = sorted(list(map(int, read().split())))
    for i in range(n - 1):
        arr[i + 1] += arr[i]
    print(sum(arr))
