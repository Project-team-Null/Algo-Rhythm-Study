def solve(n):
    l = [[1,0], [0,1]]
    for i in range(2, n+1):
        l.append([ l[i-2][0] + l[i-1][0] , l[i-2][1] + l[i-1][1] ])
    return l[n]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = solve(n)
        print(ans[0], ans[1])