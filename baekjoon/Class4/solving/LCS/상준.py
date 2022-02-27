from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    str1 = read().rstrip()
    str2 = read().rstrip()
    LCS = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
    ans = 0
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                LCS[i+1][j+1] = LCS[i][j] + 1
            else:
                LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
            ans = max(ans, LCS[i+1][j+1])
    print(ans)