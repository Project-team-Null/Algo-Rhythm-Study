
def solution(n):
    queen = [-1]*n

    def is_able(x):
        for i in range(x):
            if queen[i] == queen[x] or x - i == abs(queen[x] - queen[i]):
                return False
        return True

    def dfs(y):
        cnt = 0
        if y == n:
            return 1
        else:
            for i in range(n):
                queen[y] = i
                if is_able(y):
                    cnt += dfs(y+1)
            return cnt

    return dfs(0)


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
