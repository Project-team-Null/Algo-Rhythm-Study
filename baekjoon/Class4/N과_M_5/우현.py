from itertools import permutations
from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    lst = sorted(list(map(int, read().split())))
    for arr in permutations(lst, m):
        print(*arr)
