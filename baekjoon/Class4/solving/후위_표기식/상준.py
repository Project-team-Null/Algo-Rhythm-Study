from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    infix = read().rstrip()
    stk = []
    ans = ''
    for char in infix:
        if char == '(': stk.append(char)
        elif char == ')': 
            while stk[-1] != '(':
                ans += stk.pop()
            stk.pop()
        elif char == '*' or char == '/':
            while stk and (stk[-1] =='*' or stk[-1] == '/'):
                ans += stk.pop()
            stk.append(char)
        elif char == '+' or char == '-':
            while stk and stk[-1] != '(':
                ans += stk.pop()
            stk.append(char)
        else: ans += char
    while stk:
        ans += stk.pop()
    print(ans)