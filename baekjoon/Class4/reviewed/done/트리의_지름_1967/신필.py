
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def solution(nodes):

    def bfs(start):
        que = deque([start])
        dist = defaultdict(int)
        dist[start] = 0

        while que:
            cur = que.popleft()
            for frm, frm_w in nodes[cur]:
                if frm not in dist:
                    dist[frm] = dist[cur] + frm_w
                    que.append(frm)

        max_d = [0, 0]
        for i, v in dist.items():
            if v > max_d[1]:
                max_d = [i, v]

        return max_d

    r_node = bfs(1)
    l_node = bfs(r_node[0])

    return l_node[1]


if __name__ == "__main__":
    n = int(input())
    nodes = defaultdict(list)
    for _ in range(n - 1):
        p, v, w = map(int, input().split())
        nodes[p].append((v, w))
        nodes[v].append((p, w))
    print(solution(nodes))
