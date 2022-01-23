import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    dic = {}
    for i in range(1, n+1):
        pokemon = input().rstrip()
        dic[pokemon] = str(i)
        dic[str(i)] = pokemon
    for _ in range(m):
        print(dic[input().rstrip()])
