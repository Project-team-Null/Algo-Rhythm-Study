

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        cnt = list(range(1, n + 1))
        for x in range(k):
            for y in range(1, n):
                cnt[y] += cnt[y - 1]
        print(cnt[-1])
