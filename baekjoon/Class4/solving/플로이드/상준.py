from sys import stdin
import copy

def floydwarshall(graph, n):
    dp = copy.deepcopy(graph)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    m = int(read().rstrip())
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, read().rstrip().split())
        graph[a][b] = min(graph[a][b], c)
    
    ans = floydwarshall(graph, n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(ans[i][j] if ans[i][j] != float('inf') else 0, end = " ")
        print()