from sys import stdin
import heapq

if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        k = int(read().rstrip())
        min_dct = {}
        max_dct = {}
        min_heap = []
        max_heap = []
        size = 0
        for _ in range(k):
            cmd, num = read().rstrip().split()
            num = int(num)
            if cmd == 'I':
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
                size += 1
            elif cmd == 'D':
                if size != 0:
                    if num == 1:
                        while True:
                            temp = -heapq.heappop(max_heap)
                            if min_dct.get(temp, 0) == 0:
                                if max_dct.get(temp, 0) != 0:
                                    max_dct[temp] += 1
                                else: max_dct[temp] = 1
                                break
                            else:
                                min_dct[temp] -= 1
                        size -= 1
                    elif num == -1:
                        while True:
                            temp = heapq.heappop(min_heap)
                            if max_dct.get(temp, 0) == 0:
                                if min_dct.get(temp, 0) != 0:
                                    min_dct[temp] += 1
                                else: min_dct[temp] = 1
                                break
                            else:
                                max_dct[temp] -= 1
                        size -= 1
        ans = [0, 0]
        if size == 0: print("EMPTY")
        else:
            while True:
                temp = -heapq.heappop(max_heap)
                if min_dct.get(temp, 0) == 0:
                    ans[0] = temp
                    break
                else:
                    min_dct[temp] -= 1
            while True:
                temp = heapq.heappop(min_heap)
                if max_dct.get(temp, 0) == 0:
                    ans[1] = temp
                    break
                else:
                    max_dct[temp] -= 1
            print(ans[0], ans[1])