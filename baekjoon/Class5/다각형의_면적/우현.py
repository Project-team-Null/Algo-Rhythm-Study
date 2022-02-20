from sys import stdin
import math
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    for _ in range(n - 2):
        input()
    p = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    theta = (n - 2) * math.pi / (n * 2)
    a = math.tan(theta) * (p / 2)
    print(round((n * p * a / 2), 1))
