from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    truth = set(list(map(int, read().rstrip().split()))[1:])
    parties = []
    able = []
    for _ in range(m):
        party = set(list(map(int, read().rstrip().split()))[1:])
        parties.append(party)
        able.append(1)
    
    for _ in range(m):
        for i, party in enumerate(parties):
            if truth & party:
                able[i] = 0
                truth |= party
    print(sum(able))