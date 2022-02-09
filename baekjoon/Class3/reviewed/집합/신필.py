import sys

input = sys.stdin.readline


def solution(s, cmd, num=0):

    def all_s():
        s.clear()
        s.update(range(1, 20 + 1))

    num = int(num)
    if cmd == 'add':
        s.add(num)
    elif cmd == 'remove':
        s.discard(num)
    elif cmd == 'check':
        print(int(s.__contains__(num)))
    elif cmd == 'toggle':
        s.remove(num) if num in s else s.add(num)
    elif cmd == 'all':
        all_s()
    elif cmd == 'empty':
        s.clear()


if __name__ == '__main__':
    n = int(input())
    s = set()
    for i in range(n):
        cmds = input().split()
        solution(s, *cmds)
