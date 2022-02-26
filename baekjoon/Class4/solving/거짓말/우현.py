from sys import stdin
from collections import defaultdict
input = stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    known = list(map(int, input().split()))

    if len(known) == 1:
        print(m)

    else:
        known = set(known[1:])
        party = defaultdict(set)
        for i in range(m):
            party[i] = set(list(map(int, input().split()))[1:])
        for _ in range(m):
            for i in range(m):
                if party[i] & known != set():
                    known |= party[i]
        cnt = 0
        for i in range(m):
            if party[i] & known == set():
                cnt += 1
        print(cnt)
