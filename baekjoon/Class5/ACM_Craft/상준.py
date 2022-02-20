from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def total_time(w, graph, delay, dp):
    if dp[w] != -1: return dp[w]
    temp = [0]
    for prev in graph[w]:
        temp.append(total_time(prev, graph, delay, dp))
    dp[w] = delay[w] + max(temp)
    return dp[w]


if __name__ == '__main__':
    read = stdin.readline
    t = int(read().rstrip())
    for _ in range(t):
        n, k = map(int, read().rstrip().split())
        delay = [0] + list(map(int, read().rstrip().split()))
        dp = [-1] * (n+1)
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            frm, to = map(int, read().rstrip().split())
            graph[to].append(frm)
        w = int(read().rstrip())
        print(total_time(w, graph, delay, dp))