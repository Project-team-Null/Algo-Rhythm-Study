from sys import stdin

def find_sequence(frm, n, m, arr):
    if m == 0:
        print(*arr)
        return
    for i in range(frm+1, n-m+2):
        find_sequence(i, n, m-1, arr+[i])

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    find_sequence(0, n, m, [])