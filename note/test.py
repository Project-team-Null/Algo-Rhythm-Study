from sys import stdin
import numpy as np

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def select(arr, p, r, i):
    if p == r: return arr[p]
    q = partition(arr, p, r)
    k = q - p + 1
    if i < k: return select(arr, p, q-1, i)
    elif i == k: return arr[q]
    else: return select(arr, q+1, r, i-k)


if __name__ == '__main__':
    read = stdin.readline
    rand_arr = [0] + list(np.random.randint(1, 101, 20))
    sorted_arr = sorted(rand_arr)
    print(rand_arr[1:])
    print(sorted_arr[1:])
    while True:
        input = int(read())
        if input == -1: break
        print(select(rand_arr, 1, 20, input))