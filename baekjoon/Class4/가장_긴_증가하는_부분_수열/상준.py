from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    seq = list(map(int, read().rstrip().split()))
    ans = [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                ans[i+1] = max(ans[i+1], ans[j+1]+1)
    print(max(ans)+1)