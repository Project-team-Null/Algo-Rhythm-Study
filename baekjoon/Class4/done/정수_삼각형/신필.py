import sys
input = sys.stdin.readline


def solution(arr, n):
    max_v = 0
    dp = [[0]*(i+1) for i in range(n)]
    dp[0][0] = arr[0][0]

    def search_tree(i, j):
        if dp[i][j] == 0:
            if j < i:
                dp[i][j] = search_tree(i-1, j) + arr[i][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], search_tree(i-1, j-1) + arr[i][j])
        return dp[i][j]
    for j in range(n):
        search_tree(n-1, j)

    return max(dp[n-1])


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(arr, n))
