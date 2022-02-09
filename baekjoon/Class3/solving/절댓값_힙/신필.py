
import heapq
import sys

input = sys.stdin.readline


class Heap:
    length = 0

    def __init__(self, is_max) -> None:
        self.que = [0]
        self.__is_max = is_max

    def compare(self, a, b):
        if self.__is_max == "abs":
            return a < b if abs(a) == abs(b) else abs(a) < abs(b)
        return a > b if self.__is_max else a < b

    def swap(self, a, b):
        self.que[a], self.que[b] = self.que[b], self.que[a]

    def up_heap(self, index):
        if 1 >= index:
            return
        p = index // 2
        if self.compare(self.que[index], self.que[p]):
            self.swap(index, p)
            self.up_heap(p)

    def down_heap(self, index):
        if 2 * index > self.length:
            return
        l, r = 2 * index, 2 * index + 1
        if r > self.length:
            target = l
        else:
            target = l if self.compare(self.que[l], self.que[r]) else r
        if not self.compare(self.que[index], self.que[target]):
            self.swap(index, target)
            self.down_heap(target)

    def push(self, num):
        self.length += 1
        self.que.append(num)
        self.up_heap(self.length)

    def pop(self):
        if self.length == 0:
            return 0
        self.swap(self.length, 1)
        result = self.que.pop()
        self.length -= 1
        self.down_heap(1)
        return result


def solution1(cmd_list):
    plus_heap = []
    minus_heap = []
    for cmd in cmd_list:
        if cmd == 0:
            if not plus_heap and not minus_heap:
                print(0)
            elif not plus_heap:
                print(-heapq.heappop(minus_heap))
            elif not minus_heap:
                print(heapq.heappop(plus_heap))
            elif plus_heap[0] >= minus_heap[0]:
                print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))

        else:
            if cmd < 0:
                heapq.heappush(minus_heap, -cmd)
            else:
                heapq.heappush(plus_heap, cmd)


def solution2(cmd_list):
    heap = Heap("abs")
    for cmd in cmd_list:
        if cmd == 0:
            print(heap.pop())
        else:
            heap.push(cmd)


if __name__ == "__main__":
    n = int(input())
    cmd_list = []
    for _ in range(n):
        cmd_list.append(int(input()))
    solution1(cmd_list)
