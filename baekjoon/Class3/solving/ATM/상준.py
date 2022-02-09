from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    time = list(map(int, read().rstrip().split()))
    time.sort()
    tot = time[0]
    for i in range(1, len(time)):
        time[i] += time[i-1]
        tot += time[i]
    print(tot)