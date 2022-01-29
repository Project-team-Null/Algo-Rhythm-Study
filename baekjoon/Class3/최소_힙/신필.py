
import heapq
import sys

input = sys.stdin.readline


class Heap:
    def __init__(self) -> None:
        self.que = []

    def up_heap():
        pass

    def down_heap():
        pass

    def heap_push(num):
        pass

    def heap_pop():
        pass


def solution(cmd_list):
    heap = []
    for cmd in cmd_list:
        if cmd == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, cmd)


if __name__ == "__main__":
    n = int(input())
    cmd_list = []
    for _ in range(n):
        cmd_list.append(int(input()))
    solution(cmd_list)
