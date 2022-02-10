from sys import stdin
from collections import defaultdict
from collections import deque

def find_all(truth, graph, n):
    ret = set()
    for num in truth:
        if num not in ret:
            que = deque([num])
            visited = set()
            while len(que) != 0:
                cur = que.popleft()
                if cur not in visited:
                    visited.add(cur)
                    for i in range(1, n+1):
                        if i != cur and graph[cur][i]: que.append(i)
#                   for keys in graph[cur].keys():
#                       que.append(keys)
            ret.update(visited)
    return ret


if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
#   graph = [defaultdict(int) for _ in range(n+1)]
    truth = list(map(int, read().rstrip().split()))[1:]
    parties = []
    for i in range(m):
        party = list(map(int, read().rstrip().split()))
        parties.append(party[1:])
        for i in range(1, party[0]):
            for j in range(i+1, party[0]+1):
                graph[party[i]][party[j]] = 1
                graph[party[j]][party[i]] = 1
    
    ref = find_all(truth, graph, n)

    ans = 0
    for party in parties:
        in_truth = 0
        for person in party:
            if person in ref:
                in_truth = 1
                break
        if not in_truth: ans += 1
    print(ans)