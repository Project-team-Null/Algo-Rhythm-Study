from sys import stdin

# a = bn + c
# a % b = a - bn                    (= c)
# (a % b)^2 = a^2 - 2abn + (bn)^2   (= c^2)
# ((a % b)^2) % b = a^2 % b - 0 + 0

# #########################################################
# a^2을 b로 나눈 나머지 = (a를 b로 나눈 나머지)^2을 b로 나눈 나머지 #
# #########################################################

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