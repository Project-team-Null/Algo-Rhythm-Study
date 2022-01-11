# import sys
from collections import deque
# input = sys.stdin.readline


def solution(funcs, arr):
    deq = deque(arr)
    reverse_flag = False
    for func in funcs:
        if func == "R":
            reverse_flag = not reverse_flag
        elif func == "D":
            if not deq:
                return "error"
            deq.pop() if reverse_flag else deq.popleft()

    result = deq.reverse() if reverse_flag else list(deq)
    return str(result).replace(" ", "")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        arr_string = input()
        arr = []
        if len(arr_string) > 2:
            arr = list(map(int, arr_string[1:-1].split(",")))
        print(solution(p, arr))
