from sys import stdin
import heapq


def solution():
    m = int(read())
    heap_min = []
    heap_max = []
    for _ in range(m):
        cmd, num = read().rstrip().split()
        num = int(num)
        print(cmd, num)
        if cmd == 'I':
            heapq.heappush(heap_min, num)
            heapq.heappush(heap_max, -num)
        elif num == 1:
            heapq.heappop(heap_max)
        else:
            heapq.heappop(heap_min)
    for i in range(len(heap_max)):
        heap_max[i] *= -1
    arr = set(heap_max) & set(heap_min)
    if arr:
        print("-------", max(arr), min(arr), "-------")
        return max(arr), min(arr)
    else:
        return 0, 1


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    for _ in range(n):
        ans = solution()
        if ans[0] >= ans[1]:
            print(ans[0], ans[1])
        else:
            print("EMPTY")
