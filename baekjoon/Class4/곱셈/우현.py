from sys import stdin

# A = c(A // c) + (A % c)
# A % c = A - c(A // c)
# (A % c)^2 = A^2 - 2Ac(A // c) + c^2 * (A // c)^2
# ((A % c)^2) % c = A^2 % c - 0 + 0

# ########################################################
# A^2을 c로 나눈 나머지 == (A를 c로 나눈 나머지)^2을 c로 나눈 나머지
# ########################################################

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