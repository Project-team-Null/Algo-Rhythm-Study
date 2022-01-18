from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n, m = map(int, read().split())
    dic = {}
    reverse_dic = {}
    question = []
    for i in range(1, n + 1):
        temp = read().rstrip()
        dic[i] = temp
        reverse_dic[temp] = i
    
    for i in range(m):
        temp = read().rstrip()
        if temp.isdigit():
            print(dic[int(temp)])
        else:
            print(reverse_dic[temp])