
def sum_list(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]


def solution(arr):
    dp = [(1, 0), (0, 1)] + [0]*(41-2)
    result = []

    def fibonacci(n):
        if dp[n] != 0:
            return dp[n]
        dp[n] = sum_list(fibonacci(n-1), fibonacci(n-2))
        return dp[n]
    for i in arr:
        result.append(fibonacci(i))
    return result


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    result = solution(arr)
    for z, o in result:
        print(z, o)
