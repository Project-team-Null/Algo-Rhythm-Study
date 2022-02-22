
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solution(n, nodes):

    min_node = (float('inf'), float('inf'))

    def get_kb(start):
        visited = {}
        deq = deque([(start, 0)])
        while deq:
            cur, depth = deq.popleft()
            visited[cur] = depth
            for to in nodes[cur]:
                if to not in visited:
                    deq.append((to, depth + 1))
        return sum(visited.values())

    for node in range(1, n + 1):
        kb = get_kb(node)
        if kb < min_node[1]:
            min_node = (node, kb)
    return min_node[0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    nodes = defaultdict(list)
    for _ in range(m):
        frm, to = map(int, input().split())
        nodes[frm].append(to)
        nodes[to].append(frm)
    print(solution(n, nodes))


# 옛날 코드
# def soultion(dic,n):
#     # 각 점에서 모든 점까지의 깊이 합이 최소인 점을 찾자
#     result = []

#     def bfs(start):
#         que = deque([start])
#         dist = {start:0}
#         while que:
#             prev = que.popleft()
#             for node in dic[prev]:
#                 if node not in dist:
#                     dist[node] = dist[prev] + 1
#                     que.append(node)
#         return sum([i for i in dist.values()])

#     for i in range(1,n+1):
#         result.append(bfs(i))

#     return result.index(min(result)) + 1
