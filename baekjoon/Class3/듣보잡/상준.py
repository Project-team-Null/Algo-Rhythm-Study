from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    no_listen = set()
    for _ in range(n):
        name = read().rstrip()
        no_listen.add(name)
    
    no_listen_no_look = []
    for _ in range(m):
        name = read().rstrip()
        if name in no_listen:
            no_listen_no_look.append(name)
    
    no_listen_no_look.sort()
    print(len(no_listen_no_look))
    for name in no_listen_no_look:
        print(name)