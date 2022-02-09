from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int , read().rstrip().split())
    memo = dict()
    for _ in range(n):
        site, pwd = read().rstrip().split()
        memo[site] = pwd
    for _ in range(m):
        print(memo[read().rstrip()])