
def solution(n):
    queen = [-1]*n
    result = 0

    def is_able(x, y):
        for i in range(x):
            dx = x - i
            dy = abs(y - queen[i])
            if dy == 0 or dx == dy:
                return False
        return True

    def dfs(y):
        cnt = 0
        if y == n:
            return 1
        else:
            for i in range(n//2 if y == 0 else n):
                if is_able(y, i):
                    queen[y] = i
                    cnt += dfs(y+1)
            return cnt
    if n == 1:
        result = 1
    elif n % 2 == 0:
        result = 2 * dfs(0)
    else:
        result = 2 * dfs(0)
        queen[0] = n//2
        result += dfs(1)
    return result


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
