from sys import stdin
import heapq

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    heap = []
    for _ in range(n):
        init, end = map(int, read().split())
        heapq.heappush(heap, (end, init))
    time_table = set()
    cnt = 0
    last_end = -1
    while heap:
        end, init = heapq.heappop(heap)
        if init < last_end:
            continue
        temp = set()
        for i in range(init, end + 1):
            if i in time_table and i != init:
                break
            temp.add(i)
            if i == end:
                time_table |= temp
                cnt += 1
        last_end = end
    print(cnt)
