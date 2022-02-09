from sys import stdin
from collections import deque

def solution(n):
    queue = deque([0])
    queue.append(1)
    for i in range(2, n):
        m = queue.popleft() + queue[0]
        queue.append(m % 1000000007)
    queue.popleft()
    return queue.popleft()


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    
    print(solution(n % 1000000007))