from sys import stdin
import heapq

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    heap = []
    
    for _ in range(n):
        m = int(read())
        if m != 0:
            heapq.heappush(heap, m)
        else:
            try:
                print(heapq.heappop(heap))
            except:
                print(0)