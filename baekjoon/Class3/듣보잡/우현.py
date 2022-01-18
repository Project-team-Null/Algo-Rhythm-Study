from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    hear = set()
    see = set()
    
    for _ in range(n):
        hear.add(read().rstrip())
    for _ in range(m):
        see.add(read().rstrip())
    
    hear_see = sorted(list(hear & see))
    print(len(hear_see))
    for i in hear_see:
        print(i)