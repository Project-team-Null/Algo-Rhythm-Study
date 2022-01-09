
def solution(a, b, c):
    return "right" if c**2 == a**2 + b**2 else "wrong"


if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        if 0 in arr:
            break
        arr.sort()
        print(solution(*arr))
