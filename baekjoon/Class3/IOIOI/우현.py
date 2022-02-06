from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read())
    m = int(read())
    s = read().rstrip()

    ans = 0
    cnt = 0
    i = 1

    while i < m - 1:
        if s[i - 1: i + 2] == "IOI":
            cnt += 1
            if cnt == n:
                cnt -= 1
                ans += 1
            i += 1
        else:
            cnt = 0
        i += 1

    print(ans)
