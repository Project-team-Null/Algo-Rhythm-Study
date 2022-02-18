if __name__ == '__main__':
    eq = input() + '_'
    result = 0
    num = 0
    signal = 1
    for char in eq:
        if '0' <= char <= '9':
            num *= 10
            num += int(char)
        else:
            result += num * signal
            num = 0
        if char == '-':
            signal = -1
    print(result)
