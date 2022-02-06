from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    m = int(read().rstrip())
    s = read().rstrip()
    ref = "I" + "OI" * n
    
    cnt = 0
    itr = 0
    for i in range(len(s)):
        if s[i] == ref[itr]: itr += 1
        else:
            if s[i] == 'O': itr = 0
            else: itr = 1
        if itr == 2*n+1:
            cnt += 1
            itr -= 2
    print(cnt)