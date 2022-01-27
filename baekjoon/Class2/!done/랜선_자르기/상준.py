from sys import stdin

def count(lan, num):
    ret = 0
    for l in lan:
        ret += l // num
    return ret

def bin_search(lan, n, lo, hi):
    if lo > hi: return hi
    mid = (lo + hi) // 2
    cnt = count(lan, mid)
    if cnt >= n: return bin_search(lan, n, mid+1, hi)
    elif cnt < n: return bin_search(lan, n, lo, mid-1)

if __name__ == '__main__':
    read = stdin.readline
    k, n = map(int, read().rstrip().split())
    lan = []
    for _ in range(k):
        lan.append(int(read().rstrip()))
    lan.sort()

    ans = bin_search(lan, n, 1, lan[k-1])
    print(ans)