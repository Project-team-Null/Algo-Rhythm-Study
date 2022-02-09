import heapq
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        max_heap = []
        min_heap = []
        visited = set()
        cnt = 0
        k = int(input())
        for _ in range(k):
            cmd, n = input().split()
            n = int(n)
            if cmd == 'I':
                heapq.heappush(max_heap, (-n, cnt))
                heapq.heappush(min_heap, (n, cnt))
                cnt += 1
            elif cmd == 'D':
                if n == -1 and min_heap:  # 최소삭제
                    while min_heap and min_heap[0][1] in visited:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited.add(min_heap[0][1])
                        heapq.heappop(min_heap)
                elif n == 1 and max_heap:  # 최대삭제
                    while max_heap and max_heap[0][1] in visited:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited.add(max_heap[0][1])
                        heapq.heappop(max_heap)

        while min_heap and min_heap[0][1] in visited:
            heapq.heappop(min_heap)
        while max_heap and max_heap[0][1] in visited:
            heapq.heappop(max_heap)

        if min_heap and max_heap:
            print(-1 * max_heap[0][0], min_heap[0][0])
        else:
            print('EMPTY')
