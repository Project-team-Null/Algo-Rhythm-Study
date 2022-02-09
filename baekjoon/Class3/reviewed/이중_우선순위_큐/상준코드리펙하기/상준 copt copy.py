from sys import stdin
from collections import defaultdict
import heapq

min_dct, max_dct = defaultdict(int), defaultdict(int)
min_heap, max_heap = [], []

def sync(num, ans):
    heap = max_heap if num == 1 else min_heap
    dct1 = min_dct if num == 1 else max_dct
    dct2 = max_dct if num == 1 else min_dct
    temp = -num * heapq.heappop(heap)
    while dct1[temp]:
        dct1[temp] -= 1
        temp = -num * heapq.heappop(heap)
    if not ans: dct2[temp] += 1
    return temp


if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        k = int(read().rstrip())
        size = 0
        for _ in range(k):
            cmd, num = read().rstrip().split()
            num = int(num)
            if cmd == 'I':
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
                size += 1
            elif cmd == 'D' and size != 0:
                size -= 1
                sync(num, 0)

        ans = [0, 0]
        if size == 0:
            print("EMPTY")
        else:
            print(sync(1, 1), sync(-1, 1))
        
        min_dct.clear()
        max_dct.clear()
        max_heap.clear()
        min_heap.clear()