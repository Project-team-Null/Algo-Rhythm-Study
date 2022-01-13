def solution(rgb, n):
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1] = [rgb[0][0], rgb[0][1], rgb[0][2]]
    for i in range(2, n + 1):
        r = rgb[i - 1][0] + min(dp[i - 1][1], dp[i - 1][2])
        g = rgb[i - 1][1] + min(dp[i - 1][0], dp[i - 1][2])
        b = rgb[i - 1][2] + min(dp[i - 1][0], dp[i - 1][1])
        dp[i] = [r, g, b]
    return min(dp[n])

if __name__ == '__main__':
    n = int(input())
    rgb = []
    
    for i in range(n):
        rgb.append(list(map(int, input().split())))
        
    print(solution(rgb, n))