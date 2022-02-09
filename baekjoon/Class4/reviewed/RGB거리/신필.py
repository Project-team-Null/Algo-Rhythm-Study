
def solution(h_list):
    dp = [[] for _ in range(len(h_list))]
    dp[0] = h_list[0]
    for h in range(1, len(h_list)):
        for c in range(3):
            prev_min = min(dp[h - 1][c - 1], dp[h - 1][(c + 1) % 3])
            dp[h].append(h_list[h][c] + prev_min)
    return min(dp[-1])


if __name__ == "__main__":
    n = int(input())
    h_list = []
    for _ in range(n):
        h_list.append(list(map(int, input().split())))
    print(solution(h_list))
