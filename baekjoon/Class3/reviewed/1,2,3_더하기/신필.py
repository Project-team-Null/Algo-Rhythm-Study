
def solution(arr):
    dp = [0, 1, 2, 4] + [-1]*7

    def dfs(n):
        if dp[n] != -1:
            return dp[n]
        dp[n] = dfs(n-3) + dfs(n-2) + dfs(n-1)
        return dp[n]
    return map(dfs, arr)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    result = solution(arr)
    for i in result:
        print(i)
