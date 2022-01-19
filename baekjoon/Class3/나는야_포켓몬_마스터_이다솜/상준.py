from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    name_list = []
    name_dict = {}
    for i in range(n):
        name = read().rstrip()
        name_list.append(name)
        name_dict[name] = i + 1
    for _ in range(m):
        prob = read().rstrip()
        if prob.isnumeric(): print(name_list[int(prob) - 1])
        else: print(name_dict[prob])