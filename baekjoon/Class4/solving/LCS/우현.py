from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    str1 = '_' + read().rstrip()
    str2 = '_' + read().rstrip()
    len_str1 = len(str1) - 1
    len_str2 = len(str2) - 1
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(max(dp[-1]))

    # # LCS 표 출력
    # print(*list(str2))
    # for i in range(1, n + 1):
    #     dp[i][0] = str1[i]
    #     print(*dp[i][:])
