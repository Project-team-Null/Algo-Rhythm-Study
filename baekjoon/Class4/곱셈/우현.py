from sys import stdin

def solution(a, b, c):
    if b == 0: return 1
    elif b == 1: return a % c
    
    temp = solution(a, b//2, c)
    
    if b % 2 == 1:
        return (temp**2 * a) % c
    else:
        return (temp**2) % c


if __name__ == "__main__":
    read = stdin.readline
    a, b, c = map(int, read().split())
    print(solution(a, b, c))