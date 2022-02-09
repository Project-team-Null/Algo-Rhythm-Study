from sys import stdin
from collections import defaultdict
import heapq
read = stdin.readline


def solution():
    k = int(read())
    dct = {-1: defaultdict(int), 1: defaultdict(int)}
    heap = [[], '_', []]

    def func(num):
        temp = -num * heapq.heappop(heap[num + 1])
        while dct[num][temp]:
            dct[num][temp] -= 1
            temp = -num * heapq.heappop(heap[num + 1])
        return temp

    size = 0
    for _ in range(k):
        cmd, num = read().rstrip().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(heap[0], num)
            heapq.heappush(heap[2], -num)
            size += 1
        elif cmd == 'D' and size != 0:
            size -= 1
            temp = func(num)
            dct[-num][temp] += 1

    if size == 0:
        print("EMPTY")
    else:
        print(func(1), func(-1))


if __name__ == '__main__':
    t = int(read())

    for _ in range(t):
        solution()
