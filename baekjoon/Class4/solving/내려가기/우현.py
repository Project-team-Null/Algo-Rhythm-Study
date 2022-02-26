from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    max_dp = [0, 0, 0]
    min_dp = [0, 0, 0]
    for i in range(n):
        input0, input1, input2 = map(int, input().split())
        max_dp = [input0 + max(max_dp[:2]),
                  input1 + max(max_dp),
                  input2 + max(max_dp[1:])]
        min_dp = [input0 + min(min_dp[:2]),
                  input1 + min(min_dp),
                  input2 + min(min_dp[1:])]
    print(max(max_dp), min(min_dp))
