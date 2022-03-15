
from itertools import permutations


def solution2(n, m, nums):
    for arr in permutations(nums, m):
        print(*arr)


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    solution2(n, m, nums)
