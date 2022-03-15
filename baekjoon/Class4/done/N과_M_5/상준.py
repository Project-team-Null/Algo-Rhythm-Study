from sys import stdin

def find_sequence(n, m, arr, ref):
    if m == 0:
        print(*arr)
        return
    for i in range(1, n+1):
        if ref[i] not in arr:
            find_sequence(n, m-1, arr + [ref[i]], ref)

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    ref = [0] + list(map(int, read().rstrip().split()))
    ref.sort()
    find_sequence(n, m, [], ref)