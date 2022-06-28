from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    
    str1 = read().rstrip()
    l1 = len(str1)

    str2 = read().rstrip()
    l2 = len(str2)

    ctable = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
    btable = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                ctable[i][j] = ctable[i-1][j-1] + 1
                btable[i][j] = 1
            else:
                ctable[i][j] = max(ctable[i-1][j], ctable[i][j-1])
                if ctable[i-1][j] >= ctable[i][j-1]:
                    btable[i][j] = 2
                else:
                    btable[i][j] = 4
    
    ans = ''
    idx1, idx2 = l1, l2
    while ctable[idx1][idx2] != 0:
        if btable[idx1][idx2] == 1:
            ans += str2[idx2 - 1]
            idx1 -= 1
            idx2 -= 1
        elif btable[idx1][idx2] == 2:
            idx1 -= 1
        else:
            idx2 -= 1
    
    print(ctable[i][j])
    if ctable[i][j] != 0:
        print(ans[::-1])