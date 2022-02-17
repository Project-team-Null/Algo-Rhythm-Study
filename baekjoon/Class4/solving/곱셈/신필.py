
def re_calc(a, b, c):
    if b == 1:
        return a % c

    result = re_calc(a, b // 2, c)

    if b % 2 == 0:  # 짝수
        return (result ** 2) % c
    else:  # 홀수
        return ((result ** 2) * (a % c)) % c


def solution(a, b, c):
    return re_calc(a, b, c)


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    # print(pow(a,b,c)) # python 내장 함수 사용
    print(solution(a, b, c))
