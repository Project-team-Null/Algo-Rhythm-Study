from itertools import combinations
from sys import stdin
input = stdin.readline


def solution():
    n = int(input())
    x_lst = []
    y_lst = []
    for i in range(n):
        x, y = map(int, input().split())
        x_lst.append(x)
        y_lst.append(y)
    min_dist = float('inf')
    for arr in combinations(range(n), n // 2):
        x_sum = sum(x_lst)
        y_sum = sum(y_lst)
        for idx in arr:
            x_sum -= x_lst[idx] * 2
            y_sum -= y_lst[idx] * 2
        dist = (x_sum**2 + y_sum**2)**(1/2)
        if dist < min_dist:
            min_dist = dist
    return min_dist


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        print(solution())
