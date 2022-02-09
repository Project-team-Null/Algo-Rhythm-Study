from sys import stdin
from collections import defaultdict
import heapq


def solution(k):
    min_dct, max_dct = defaultdict(int), defaultdict(int)
    min_heap, max_heap = [], []
    size = 0

    def heap_pop(heap, dct, direction=1):
        temp = direction * heapq.heappop(heap)
        while dct[temp]:
            dct[temp] -= 1
            temp = direction * heapq.heappop(heap)
        return temp

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
                max_dct[heap_pop(max_heap, min_dct, -1)] += 1
            elif num == -1:
                min_dct[heap_pop(min_heap, max_dct)] += 1

    return "EMPTY" if size == 0 else f"{heap_pop(max_heap,min_dct,-1)} {heap_pop(min_heap,max_dct)}"


if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        k = int(read().rstrip())
        print(solution(k))
