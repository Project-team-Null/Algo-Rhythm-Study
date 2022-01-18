from collections import deque


def solution(n, k):
    dp = [float('inf')]*(100001)

    def bfs(n):
        que = deque([n])
        while que:
            x = que.popleft()
            for i in [x*2, x+1, x-1]:
                if 0 <= i <= (100000) and dp[i] > dp[x] + 1:
                    dp[i] = dp[x] + 1
                    que.append(i)
    dp[n] = 0
    bfs(n)
    return dp[k]


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))
