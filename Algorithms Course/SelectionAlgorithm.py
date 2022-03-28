from sys import stdin
import numpy as np
from copy import deepcopy
import time

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


def insertion_sort(arr, p, r):
    for j in range(p+1, r+1):
        key = arr[j]
        i = j - 1
        while i > p-1 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key


def partition_ls(arr, p, r, pivot_value):
    i = p - 1
    for j in range(p, r+1):
        if arr[j] <= pivot_value:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    return i


def linear_select(arr, p, r, i):
    if r - p <= 4:
        insertion_sort(arr, p, r)
        return arr[p+i-1]

    medians = [0]
    for j in range(p, r+1, 5):
        end = min(j+4, r)
        mid = j + (end-j+1)//2
        insertion_sort(arr, j, end)
        medians.append(arr[mid])
    
    n = len(medians) - 1
    k = n // 2 if n % 2 == 0 else n // 2 + 1
    pivot_value = linear_select(medians, 1, n, k)
    
    q = partition_ls(arr, p, r, pivot_value)
    s = q - p + 1
    if i < s: return linear_select(arr, p, q-1, i)
    if i == s: return arr[q]
    else: return linear_select(arr, q+1, r, i-s)


if __name__ == '__main__':
    read = stdin.readline
    n = 1000
    rand_arr = [0] + list(np.random.randint(1, 10001, n))
    sorted_arr = deepcopy(rand_arr)
    insertion_sort(sorted_arr, 1, n)
    while True:
        input = int(read())
        if input == -1: break
        if input > n:
            print("wrong input")
            continue
        #print(sorted_arr[1:])
        start1 = time.time()
        print(select(rand_arr, 1, n, input))
        print(time.time() - start1)
        start2 = time.time()
        print(linear_select(rand_arr, 1, n, input))
        print(time.time() - start2)