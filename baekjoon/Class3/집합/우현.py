from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    v = set()
    for _ in range(n):
        command = read().split()
        if len(command) == 1:
            if command[0] == "all":
                v = set([i for i in range(1, 21)])
            elif command[0] == "empty":
                v = set()
        else:
            cmd, num = command[0], command[1]
            command.clear()
            num = int(num)
            if cmd == "add":
                v.add(num)
            elif cmd == "check":
                print(1 if num in v else 0)
            elif cmd == "remove":
                v.discard(num)
            else:
                v.remove(num) if num in v else v.add(num)
