if __name__ == '__main__':
    n = input()
    int_n = int(n)
    m = int(input())
    if m != 0: ref = input().split()
    else: ref = []

    ans = abs(int_n - 100)
    for i in range(1000001):
        broken = False
        click = 0
        for num in str(i):
            if num in ref: 
                broken = True
                break
            click += 1
        if not broken:
            ans = min(ans, abs(int_n - i) + click)
    
    print(ans)