from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    eq = read().rstrip()
    priority = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '(': 2,
        ')': 2
    }
    stack = []
    for c in eq:
        if c == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        elif c in priority.keys():
            while stack and priority[c] <= priority[stack[-1]] and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(c)
        else:
            print(c, end='')
    while stack:
        print(stack.pop(), end='')
