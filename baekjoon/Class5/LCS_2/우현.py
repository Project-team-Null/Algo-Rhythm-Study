import sys

read = sys.stdin.readline

if __name__ == "__main__":
    str1 = "_" + read().strip()
    str2 = "_" + read().strip()

    n = len(str1) - 1
    m = len(str2) - 1

    dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[-1][-1]
    print(lcs_len)

    lcs = ""
    i, j = n, m
    while lcs_len:
        if dp[i - 1][j] == lcs_len - 1 and dp[i][j - 1] == lcs_len - 1:
            lcs = str1[i] + lcs
            i -= 1
            j -= 1
            lcs_len -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    print(lcs)
