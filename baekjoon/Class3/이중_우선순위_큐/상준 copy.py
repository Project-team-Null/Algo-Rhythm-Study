from sys import stdin
from collections import defaultdict
import heapq


if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        k = int(read().rstrip())
        min_dct, max_dct = defaultdict(int), defaultdict(int)
        min_heap, max_heap = [], []
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
                if num == 1:
                    temp = -heapq.heappop(max_heap)
                    while min_dct[temp]:
                        min_dct[temp] -= 1
                        temp = -heapq.heappop(max_heap)
                    max_dct[temp] += 1
                elif num == -1:
                    temp = heapq.heappop(min_heap)
                    while max_dct[temp]:
                        max_dct[temp] -= 1
                        temp = heapq.heappop(min_heap)
                    min_dct[temp] += 1

        ans = [0, 0]
        if size == 0:
            print("EMPTY")
        else:
            temp = -heapq.heappop(max_heap)
            while min_dct[temp]:
                min_dct[temp] -= 1
                temp = -heapq.heappop(max_heap)
            ans[0] = temp
            temp = heapq.heappop(min_heap)
            while max_dct[temp]:
                max_dct[temp] -= 1
                temp = heapq.heappop(min_heap)
            ans[1] = temp
            print(ans[0], ans[1])
