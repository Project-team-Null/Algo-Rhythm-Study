from sys import stdin
from math import sqrt

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    arr = [float('inf')] * (n+1)
    for i in range(1, int(sqrt(n))+1):
        arr[i**2] = 1
    for i in range(1, n+1):
        if arr[i] == float('inf'):
            for j in range(1, int(sqrt(i))+1):
                arr[i] = min(arr[i], arr[i-j**2] + 1)
    print(arr[n])