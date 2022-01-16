from sys import stdin

def solution(arr, n):
    for i in range(n - 1):
        idx = n - i - 1
        for j in range(idx):
            arr[idx - 1][j] += max(arr[idx][j], arr[idx][j + 1])
    return arr[0][0]


if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, read().split()))
    
    print(solution(arr, n))