def solve():
    h, w, n = map(int, input().split())
    if n % h == 0: floor, room = h, n // h
    else: floor, room = n % h, (n // h) + 1
    print("%d%02d" % (floor, room))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()