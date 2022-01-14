
def solution(n):
    dp = [0, 0]
    for i in range(2, n+1):
        min_v = dp[i - 1] + 1
        if i % 3 == 0:
            min_v = min(min_v, dp[i // 3] + 1)
        if i % 2 == 0:
            min_v = min(min_v, dp[i // 2] + 1)
        dp.append(min_v)
    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))


# 전에 풀었던 코드가 재밌어서 첨부함 속도는 solution1이 월등함
def solution2(x):
    arr = [0]*(x+1)
    def cmd_3(x): return arr[x // 3] if x % 3 == 0 else float('inf')
    def cmd_2(x): return arr[x // 2] if x % 2 == 0 else float('inf')

    for i in range(2, x+1):
        arr[i] = min(cmd_2(i), cmd_3(i), arr[i-1]) + 1

    return arr[x]
