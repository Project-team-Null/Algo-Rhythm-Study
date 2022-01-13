from collections import defaultdict, deque


def solution(nodes, v):

    def dfs(start_node):
        visited = {}

        def r_dfs(cur_node):
            visited[cur_node] = cur_node
            for next_node in sorted(nodes[cur_node]):
                if next_node not in visited:
                    r_dfs(next_node)
        r_dfs(start_node)
        return visited.keys()

    def bfs(start_node):
        visited = {}
        que = deque([start_node])
        visited[start_node] = start_node
        while que:
            cur_node = que.popleft()
            for next_node in sorted(nodes[cur_node]):
                if next_node not in visited:
                    que.append(next_node)
                    visited[next_node] = next_node
        return visited.keys()

    print(*dfs(v))
    print(*bfs(v))


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    nodes = defaultdict(list)
    for i in range(m):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    solution(nodes, v)
