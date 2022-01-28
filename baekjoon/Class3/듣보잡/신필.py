import sys
input = sys.stdin.readline  # 이거 안넣어서 느렸음 ㅋ


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    not_listen = set([])
    not_see = []
    not_see_listen = []
    for _ in range(n):
        not_listen.add(input().rstrip())
    for _ in range(m):
        p1 = input().rstrip()
        not_see.append(p1)
        if p1 in not_listen:
            not_see_listen.append(p1)
    print(len(not_see_listen))
    for nsl in sorted(not_see_listen):
        print(nsl)


# def solution(a, b):
#     return a & b


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     not_listen = set([])
#     not_see = set([])
#     for _ in range(n):
#         not_listen.add(input())
#     for _ in range(m):
#         not_see.add(input())
#     not_see_listen = solution(not_listen, not_see)
#     print(len(not_see_listen))
#     for nsl in sorted(list(not_see_listen)):
#         print(nsl)
