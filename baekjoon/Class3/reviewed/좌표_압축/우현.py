from sys import stdin

if __name__ == "__main__":
    read = stdin.readline

    n = int(read())
    numbers = list(map(int, read().split()))
    arr = sorted(list(set(numbers)))
    dic = {arr[i]: i for i in range(len(arr))}

    for i in numbers:
        print(dic[i], end=' ')
