import re


def solution1(n, m, s):  # 50점
    token = "I" + "OI" * n
    cnt = 0
    i = 0
    while i < m:
        i = s.find(token, i)
        if i == -1:
            break
        else:
            cnt += 1
            i += 2
    return cnt


'''
find n!
x - 2*(n-1) <= m 인 n을 찾아라
n  <= (x - m) / 2  + 1
n = (x-m) // 2 + 1
'''


def solution2(n, m, s):
    q = re.compile("(I(OI)+)")
    cnt = 0
    for pattern, _ in q.findall(s):
        pattern_len = len(pattern)
        token_len = 2 * n + 1
        if pattern_len >= token_len:
            cnt += (pattern_len - token_len) // 2 + 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    s = input()
    print(solution2(n, m, s))
