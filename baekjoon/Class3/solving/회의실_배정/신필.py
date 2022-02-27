import sys

input = sys.stdin.readline


def solution(meet_list):
    meet_list.sort()
    cur_end = 0
    cnt = 0
    for meet in meet_list:
        end, start = meet
        if start >= cur_end:
            cnt += 1
            cur_end = end

    return cnt


if __name__ == "__main__":
    n = int(input())
    meet_list = []
    for _ in range(n):
        start, end = map(int, input().split())
        meet_list.append((end, start))

    print(solution(meet_list))
