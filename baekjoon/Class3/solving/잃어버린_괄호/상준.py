from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    exp_str = read().rstrip()
    exp_list = []
    temp = ""
    for char in exp_str:
        if char == '-' or char == '+':
            exp_list.append(int(temp))
            exp_list.append(char)
            temp = ""
        else:
            temp = temp + char
    exp_list.append(int(temp))

    ans = 0
    minus = False
    for exp in exp_list:
        if exp == '-': minus = True
        elif exp == '+': pass
        else:
            if not minus: ans += exp
            else: ans -= exp
    print(ans)