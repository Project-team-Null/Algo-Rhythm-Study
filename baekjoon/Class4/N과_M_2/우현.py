from itertools import combinations

if __name__ == "__main__":
    n, m = map(int, input().split())
    for arr in combinations(range(1, n + 1), m):
        print(*arr)
