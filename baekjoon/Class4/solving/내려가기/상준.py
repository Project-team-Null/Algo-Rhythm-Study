from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    max_dp = [0, 0, 0]
    min_dp = [0, 0, 0]
    for _ in range(n):
        x, y, z = map(int, read().rstrip().split())
        temp1 = [x + max(max_dp[0], max_dp[1]), x + min(min_dp[0], min_dp[1])]
        temp2 = [y + max(max_dp[0], max_dp[1], max_dp[2]), y + min(min_dp[0], min_dp[1], min_dp[2])]
        temp3 = [z + max(max_dp[1], max_dp[2]), z + min(min_dp[1], min_dp[2])]
        max_dp = [temp1[0], temp2[0], temp3[0]]
        min_dp = [temp1[1], temp2[1], temp3[1]]
    print(max(max_dp), min(min_dp))