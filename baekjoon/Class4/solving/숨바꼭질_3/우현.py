from collections import deque


def bfs(n, k):
    queue = deque([n])
    visited = [-1] * 100001
    visited[n] = 0
    while queue:
        num = queue.popleft()
        if num == k:
            return visited[num]
        if num <= 50000 and visited[num * 2] == -1:
            visited[num * 2] = visited[num]
            queue.append(num * 2)
        if 1 <= num and visited[num - 1] == -1:
            visited[num - 1] = visited[num] + 1
            queue.append(num - 1)
        if num <= 99999 and visited[num + 1] == -1:
            visited[num + 1] = visited[num] + 1
            queue.append(num + 1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(bfs(n, k))
