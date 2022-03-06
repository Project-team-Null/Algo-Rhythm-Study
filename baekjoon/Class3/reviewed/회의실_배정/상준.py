from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    time = []
    for _ in range(n):
        time.append(tuple(map(int, read().rstrip().split())))
    time.sort(key=lambda x:(x[1],x[0]), reverse=True)

    ans = 0
    start = 0
    while len(time) != 0:
        frm, to = time.pop()
        if frm >= start:
            ans += 1
            start = to
    print(ans)