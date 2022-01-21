from sys import stdin
import heapq


def solution():
    m = int(read())
    heap_min = []
    heap_max = []
    is_in = [0] * (m + 1)

    for i in range(m):
        cmd, num = read().rstrip().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(heap_min, (num, i))
            heapq.heappush(heap_max, (-num, i))
            is_in[i] = 1

        else:
            if num == 1:
                while heap_max and not is_in[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                if heap_max:
                    is_in[heap_max[0][1]] = 0
                    heapq.heappop(heap_max)
            else:
                while heap_min and not is_in[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                if heap_min:
                    is_in[heap_min[0][1]] = 0
                    heapq.heappop(heap_min)

    while heap_max and not is_in[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not is_in[heap_min[0][1]]:
        heapq.heappop(heap_min)

    if heap_max and heap_min:
        return -heap_max[0][0], heap_min[0][0]
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
