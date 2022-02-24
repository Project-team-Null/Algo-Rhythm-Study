if __name__ == "__main__":
    n, k = map(int, input().split())
    ans = 0
    bin_n = bin(n)[2:]
    while bin_n.count('1') > k:
        for i in range(len(bin_n)):
            if bin_n[len(bin_n) - 1 - i] == '1':
                n += 2**i
                ans += 2**i
                break
        bin_n = bin(n)[2:]
    print(ans)
