from sys import stdin

def fact(n):
    if n == 0: return 1
    elif n == 1: return 1
    return n * fact(n-1)

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    fact_n = str(fact(n))[::-1]
    ans = 0
    for num in fact_n:
        if num == '0': ans += 1
        else: break
    print(ans)