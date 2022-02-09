from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    s = set()
    default_full = [i for i in range(1, 21)]
    default_empty = []
    m = int(read().rstrip())
    for _ in range(m):
        cmd = list(read().rstrip().split())
        if cmd[0] == 'add':
            s.add(int(cmd[1]))
        elif cmd[0] == 'remove':
            x = int(cmd[1])
            if x in s: s.remove(x)
        elif cmd[0] == 'check':
            x = int(cmd[1])
            print(1) if x in s else print(0)
        elif cmd[0] == 'toggle':
            x = int(cmd[1])
            if x in s: s.remove(x)
            else: s.add(x)
        elif cmd[0] == 'all':
            s = set(default_full)
        elif cmd[0] == 'empty':
            s = set(default_empty)