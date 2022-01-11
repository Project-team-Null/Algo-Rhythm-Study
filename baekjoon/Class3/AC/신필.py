from collections import deque


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
    if reverse_flag:
        deq.reverse()
    return "[" + ",".join(deq) + "]"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        arr_string = input()
        arr = []
        if len(arr_string) > 2:
            arr = arr_string[1:-1].split(",")
        print(solution(p, arr))
